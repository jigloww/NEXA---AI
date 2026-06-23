import os
import tempfile
import unittest

import database.database as database_module

from services.memory_service import MemoryService
from services.profile_memory_service import (
    ProfileMemoryService
)


class MultiUserMemoryTestCase(
    unittest.TestCase
):

    def setUp(self):

        self.temp_dir = (
            tempfile.TemporaryDirectory()
        )
        self.original_database_name = (
            database_module.DATABASE_NAME
        )
        database_module.DATABASE_NAME = (
            os.path.join(
                self.temp_dir.name,
                "test_nexa.db"
            )
        )

        self.memory = MemoryService()

    def tearDown(self):

        database_module.DATABASE_NAME = (
            self.original_database_name
        )
        self.temp_dir.cleanup()

    def test_conversation_context_is_scoped_per_user(
        self
    ):

        self.memory.add_message(
            "User",
            "Halo dari user A",
            user_id="user-a",
            chat_id="chat-a"
        )
        self.memory.add_message(
            "User",
            "Halo dari user B",
            user_id="user-b",
            chat_id="chat-b"
        )

        context_a = self.memory.get_context(
            user_id="user-a",
            chat_id="chat-a"
        )
        context_b = self.memory.get_context(
            user_id="user-b",
            chat_id="chat-b"
        )

        self.assertIn(
            "Halo dari user A",
            context_a
        )
        self.assertNotIn(
            "Halo dari user B",
            context_a
        )
        self.assertIn(
            "Halo dari user B",
            context_b
        )
        self.assertNotIn(
            "Halo dari user A",
            context_b
        )

    def test_profile_memory_is_scoped_per_user(
        self
    ):

        profile_memory = (
            ProfileMemoryService(
                self.memory
            )
        )

        profile_memory.handle(
            "nama saya Andi",
            user_id="user-a",
            chat_id="chat-a"
        )
        profile_memory.handle(
            "nama saya Sinta",
            user_id="user-b",
            chat_id="chat-b"
        )

        response_a = profile_memory.handle(
            "siapa nama saya",
            user_id="user-a",
            chat_id="chat-a"
        )
        response_b = profile_memory.handle(
            "siapa nama saya",
            user_id="user-b",
            chat_id="chat-b"
        )

        self.assertEqual(
            response_a,
            "Nama Anda adalah Andi."
        )
        self.assertEqual(
            response_b,
            "Nama Anda adalah Sinta."
        )


if __name__ == "__main__":
    unittest.main()
