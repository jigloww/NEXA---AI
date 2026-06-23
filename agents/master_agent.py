from services.llm_service import LLMService
from services.memory_service import MemoryService
from services.prompt_service import load_system_prompt

from services.profile_memory_service import ProfileMemoryService
from services.auto_memory_service import (
    AutoMemoryService
)

from agents.academic_agent import AcademicAgent
from agents.productivity_agent import ProductivityAgent
from agents.business_agent import BusinessAgent
from agents.investment_agent import InvestmentAgent


class MasterAgent:

    def __init__(self):
        self.memory = MemoryService()
        self.llm = LLMService()

        self.profile_memory = ProfileMemoryService(
            self.memory
        )
        self.auto_memory = (
            AutoMemoryService(
                self.memory
            )
        )

        self.academic = AcademicAgent()
        self.productivity = ProductivityAgent()
        self.business = BusinessAgent()
        self.investment = InvestmentAgent()

    def chat(
        self,
        user_message,
        user_id=None,
        chat_id=None
    ):

        user_lower = user_message.lower().strip()

        self.auto_memory.extract(
            user_message,
            user_id=user_id,
            chat_id=chat_id
        )

        # ==========================================
        # PROFILE MEMORY
        # ==========================================

        profile_response = self.profile_memory.handle(
            user_message,
            user_id=user_id,
            chat_id=chat_id
        )

        if profile_response:
            return profile_response

        # ==========================================
        # AUTO MEMORY EXTRACTION
        # ==========================================

        if user_lower.startswith("saya ingin menjadi "):

            goal = user_message[
                len("saya ingin menjadi "):
            ].strip()

            self.memory.save_memory(
                "career_goal",
                goal,
                user_id=user_id,
                chat_id=chat_id
            )

            return (
                f"Baik, saya akan mengingat bahwa target karier Anda adalah {goal}."
            )

        if user_lower.startswith("saya sedang belajar "):

            topic = user_message[
                len("saya sedang belajar "):
            ].strip()

            self.memory.save_memory(
                "current_learning",
                topic,
                user_id=user_id,
                chat_id=chat_id
            )

            return (
                f"Baik, saya akan mengingat bahwa Anda sedang belajar {topic}."
            )

        if user_lower.startswith("saya sedang membuat "):

            project = user_message[
                len("saya sedang membuat "):
            ].strip()

            self.memory.save_memory(
                "current_project",
                project,
                user_id=user_id,
                chat_id=chat_id
            )

            return (
                f"Baik, saya akan mengingat bahwa Anda sedang membuat {project}."
            )

        # ==========================================
        # AGENT ROUTER
        # ==========================================

        academic_keywords = [
            "kuliah",
            "tugas",
            "skripsi",
            "knn",
            "python",
            "flutter"
        ]

        productivity_keywords = [
            "jadwal",
            "target",
            "produktif",
            "to-do"
        ]

        business_keywords = [
            "bisnis",
            "startup",
            "usaha",
            "marketing",
            "monetisasi"
        ]

        investment_keywords = [
            "investasi",
            "saham",
            "reksadana",
            "etf",
            "keuangan"
        ]

        if any(
            keyword in user_lower
            for keyword in academic_keywords
        ):
            return self.academic.handle(
                user_message
            )

        if any(
            keyword in user_lower
            for keyword in productivity_keywords
        ):
            return self.productivity.handle(
                user_message
            )

        if any(
            keyword in user_lower
            for keyword in business_keywords
        ):
            return self.business.handle(
                user_message
            )

        if any(
            keyword in user_lower
            for keyword in investment_keywords
        ):
            return self.investment.handle(
                user_message
            )

        # ==========================================
        # SHORT TERM MEMORY
        # ==========================================

        self.memory.add_message(
            "User",
            user_message,
            user_id=user_id,
            chat_id=chat_id
        )

        context = self.memory.get_context(
            user_id=user_id,
            chat_id=chat_id
        )

        # ==========================================
        # LONG TERM MEMORY INJECTION
        # ==========================================

        memory_context = ""

        for key, value in self.memory.get_all_memories(
            user_id=user_id,
            chat_id=chat_id
        ):
            memory_context += (
                f"{key}: {value}\n"
            )

        system_prompt = load_system_prompt()

        prompt = f"""
{system_prompt}

Informasi yang Anda ketahui tentang pengguna:

{memory_context}

Riwayat Percakapan:

{context}

Jawablah sebagai NEXA.
"""

        response = self.llm.generate_response(
            prompt
        )

        self.memory.add_message(
            "NEXA",
            response,
            user_id=user_id,
            chat_id=chat_id
        )

        return response
