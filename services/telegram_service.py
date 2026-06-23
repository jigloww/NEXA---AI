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

    if not update.message:
        return

    user_message = (
        update.message.text
    )
    user_id = str(
        update.effective_user.id
    )
    chat_id = str(
        update.effective_chat.id
    )

    response = agent.chat(
        user_message,
        user_id=user_id,
        chat_id=chat_id
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
