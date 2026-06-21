import os
import sys

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from dotenv import load_dotenv

load_dotenv()

from services.telegram_service import (
    create_bot
)

token = os.getenv(
    "TELEGRAM_BOT_TOKEN"
)

bot = create_bot(
    token
)

print(
    "NEXA Telegram Bot Running..."
)

bot.run_polling()
