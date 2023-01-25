import logging
from telegram import Update
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
    ApplicationBuilder,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

FIRST_COLOR, SECOND_COLOR = range(2)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    reply_keyboard = [["Синий", "Красный", "Желтый"]]
    await update.message.reply_text(
        "Привет, сегодня мы будем вместе с тобой смешивать цвета!\n"
        "Какой цвет выберешь первым?",
        reply_markup = ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Какой цвет?"
        )
    )
    return FIRST_COLOR


async def first_color(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    logger.info("Первый цвет %s: %s", user.first_name, update.message.text)
    reply_keyboard = [["Синий", "Красный", "Желтый"]]

    text = update.message.text
    context.user_data["color_1"] = text

    await update.message.reply_text(
        "Отлично, друг, а какой цвет будет вторым?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Какой цвет?"
        ),
    )

    return SECOND_COLOR


async def second_color(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    logger.info("Второй цвет %s: %s", user.first_name, update.message.text)
    reply_keyboard = [["Синий", "Красный", "Желтый"]]

    text = update.message.text
    context.user_data["color_2"] = text

    first_col = context.user_data["color_1"]
    second_col = text

    if first_col == second_col:
        await update.message.reply_text(
            f"Друг, твой цвет {first_col}",
            reply_markup=ReplyKeyboardRemove()
        )
    elif (first_col == "Синий" and second_col == "Красный") or (second_col == "Синий" and first_col == "Красный"):
        await update.message.reply_text(
            "Друг, твой цвет фиолетовый",
            reply_markup=ReplyKeyboardRemove()
        )
    elif (first_col == "Желтый" and second_col == "Красный") or (second_col == "Желтый" and first_col == "Красный"):
        await update.message.reply_text(
            "Друг, твой цвет оранжевый",
             reply_markup=ReplyKeyboardRemove()
        )
    elif (first_col == "Желтый" and second_col == "Синий") or (second_col == "Желтый" and first_col == "Синий"):
        await update.message.reply_text(
            "Друг, твой цвет зеленый",
            reply_markup=ReplyKeyboardRemove()
        )

    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    logger.info("Пользователь %s прекратил работу.", user.first_name)
    await update.message.reply_text(
        "Пока", reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("5535531129:AAGbrtQM56EYsqGCM9k_D7NHjbKg-mS7ZrY").build()

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            FIRST_COLOR: [MessageHandler(filters.Regex("^(Красный|Синий|Желтый)$"), first_color)],
            SECOND_COLOR: [MessageHandler(filters.Regex("^(Красный|Синий|Желтый)$"), second_color)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    application.add_handler(conv_handler)

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()
