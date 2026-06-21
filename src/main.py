import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from agents.master_agent import MasterAgent

agent = MasterAgent()

print("=" * 40)
print("      NEXA AI Assistant")
print("=" * 40)

while True:

    user_input = input("\nAnda : ")

    if user_input.lower() in [
        "exit",
        "quit",
        "keluar"
    ]:
        print("\nNEXA : Sampai jumpa!")
        break

    try:

        response = agent.chat(
            user_input
        )

        print(
            f"\nNEXA : {response}"
        )

    except Exception as e:

        print(
            f"\nError : {e}"
        )