from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes
)

from agents.master_agent import MasterAgent

agent = MasterAgent()


async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(
        "Halo, saya NEXA AI."
    )


async def chat(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user_message = (
        update.message.text
    )

    response = agent.chat(
        user_message
    )

    await update.message.reply_text(
        response
    )


def create_bot(token):

    app = Application.builder() \
        .token(token) \
        .build()

    app.add_handler(
        CommandHandler(
            "start",
            start
        )
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT,
            chat
        )
    )

    return app