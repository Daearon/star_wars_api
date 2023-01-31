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

logging.basicConfig(level=logging.INFO, filename="calculation_log.log",
                    format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s - %(message)s",
                    datefmt='%d-%m-%Y %H:%M:%S')

logger = logging.getLogger(__name__)

CHOICE, FIRST_COMPLEX, SECOND_COMPLEX, FIRST_RATIONAL, SECOND_RATIONAL, \
OPERATION_CHOICE_COMPLEX, OPERATION_CHOICE_RATIONAL = range(7)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    reply_keyboard = [["Комплексное число", "Рациональное число"]]
    await update.message.reply_text(
        "С каким типом чисел мы будем работать?",
        reply_markup = ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Какой тип числа?"
        )
    )
    return CHOICE


async def choice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    logger.info("Выбор типа числа: %s: %s", user.first_name, update.message.text)
    text = update.message.text
    context.user_data["number_type"] = text
    user_choice = text

    if user_choice == "Комплексное число":
        await update.message.reply_text("Введите через пробел два целых числа (например, 2 6): ")
        return FIRST_COMPLEX
    if user_choice == "Рациональное число":
        await update.message.reply_text("Введите через пробел два целых числа (например, 2 6): ")
        return FIRST_RATIONAL


async def first_complex(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    logger.info("Пользователь ввел число: %s: %s", user.first_name, update.message.text)
    get_complex = update.message.text
    if ' ' in get_complex and (get_complex.replace(' ', '')).isdigit():
        get_complex = get_complex.split(' ')
        complex_one = complex(int(get_complex[0]), int(get_complex[1]))
        context.user_data["complex_one"] = complex_one
        await update.message.reply_text(f"Первое комплексное число - {complex_one}\n"
                                        f" Введите через пробел ещё два целых числа (например, 2 6): ")
        return SECOND_COMPLEX
    else:
        await update.message.reply_text("Нужно ввести числа")


async def second_complex(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    logger.info("Пользователь ввел число: %s: %s", user.first_name, update.message.text)
    get_second_complex = update.message.text
    if ' ' in get_second_complex and (get_second_complex.replace(' ', '')).isdigit():
        get_second_complex = get_second_complex.split(' ')
        complex_two = complex(int(get_second_complex[0]), int(get_second_complex[1]))
        context.user_data["complex_two"] = complex_two
        await update.message.reply_text(f"Второе комплексное число - {complex_two}")
    else:
        await update.message.reply_text('Нужно ввести числа')
    reply_keyboard = [["+", "-", "*", "/", "**", "sqrt"]]
    await update.message.reply_text(
        "Какую математическую операцию выберете?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Какая операция?"
        )
    )
    return OPERATION_CHOICE_COMPLEX


async def operation_choice_complex(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    logger.info("Пользователь выбрал операцию %s: %s", user.first_name, update.message.text)
    complex_one = context.user_data.get('complex_one')
    complex_two = context.user_data.get('complex_two')
    text = update.message.text
    context.user_data["operation_type"] = text
    result = 0
    user_choice = text
    if user_choice == '+':
        result = complex_one + complex_two
    if user_choice == '-':
        result = complex_one - complex_two
    if user_choice == '*':
        result = complex_one * complex_two
    if user_choice == '/':
        try:
            result = complex_one / complex_two
        except ZeroDivisionError:
            await update.message.reply_text("Разделить на ноль не получится")
    if user_choice == '**':
        result = complex_one ** complex_two
    if user_choice == '**':
        result = complex_one ** 0.5
    await update.message.reply_text(f"Ваш результат - {result}")
    return ConversationHandler.END


async def first_rational(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    logger.info("Пользователь ввел число: %s: %s", user.first_name, update.message.text)
    get_rational = update.message.text
    if ' ' in get_rational and (get_rational.replace(' ', '')).isdigit():
        get_rational = get_rational.split(' ')
        rational_one = float(int(get_rational[0]) / int(get_rational[1]))
        context.user_data["rational_one"] = rational_one
        await update.message.reply_text(f"Первое рациональное число - {rational_one}\n"
                                        f" Введите через пробел ещё два целых числа (например, 2 6): ")
        return SECOND_RATIONAL
    else:
        await update.message.reply_text("Нужно ввести числа")


async def second_rational(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    logger.info("Пользователь ввел число: %s: %s", user.first_name, update.message.text)
    get_second_rational = update.message.text
    if ' ' in get_second_rational and (get_second_rational.replace(' ', '')).isdigit():
        get_second_rational = get_second_rational.split(' ')
        rational_two = float(int(get_second_rational[0]) / int(get_second_rational[1]))
        context.user_data["rational_two"] = rational_two
        await update.message.reply_text(f"Второе комплексное число - {rational_two}")
    else:
        await update.message.reply_text('Нужно ввести числа')
    reply_keyboard = [["+", "-", "*", "/", "**", "sqrt"]]
    await update.message.reply_text(
        "Какую математическую операцию выберете?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Какая операция?"
        )
    )
    return OPERATION_CHOICE_RATIONAL


async def operation_choice_rational(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    logger.info("Пользователь выбрал операцию %s: %s", user.first_name, update.message.text)
    rational_one = context.user_data.get('rational_one')
    rational_two = context.user_data.get('rational_two')
    text = update.message.text
    context.user_data["operation_type"] = text
    result = 0
    user_choice = text
    if user_choice == '+':
        result = rational_one + rational_two
    if user_choice == '-':
        result = rational_one - rational_two
    if user_choice == '*':
        result = rational_one * rational_two
    if user_choice == '/':
        try:
            result = rational_one / rational_two
        except ZeroDivisionError:
            await update.message.reply_text("Разделить на ноль не получится")
    if user_choice == '**':
        result = rational_one ** rational_two
    if user_choice == '**':
        result = rational_one ** 0.5
    await update.message.reply_text(f"Ваш результат - {result}")
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
            CHOICE: [MessageHandler(filters.Regex("^(Комплексное число|Рациональное число)$"), choice)],
            FIRST_COMPLEX: [MessageHandler(filters.TEXT, first_complex)],
            SECOND_COMPLEX: [MessageHandler(filters.TEXT, second_complex)],
            OPERATION_CHOICE_COMPLEX: [MessageHandler(filters.TEXT, operation_choice_complex)],
            FIRST_RATIONAL: [MessageHandler(filters.TEXT, first_rational)],
            SECOND_RATIONAL: [MessageHandler(filters.TEXT, second_rational)],
            OPERATION_CHOICE_RATIONAL: [MessageHandler(filters.TEXT, operation_choice_rational)]
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    application.add_handler(conv_handler)

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()