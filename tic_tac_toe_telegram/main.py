import logging

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s - %(message)s",
                    datefmt='%d-%m-%Y %H:%M:%S',
                    handlers = [logging.FileHandler("game_log.log"), logging.StreamHandler()])
logger = logging.getLogger(__name__)


token = "5535531129:AAGbrtQM56EYsqGCM9k_D7NHjbKg-mS7ZrY"
bot = Bot(token=token)
dp = Dispatcher(bot, storage=MemoryStorage())


initial_commands = [
    '/start',
    '/tic_tac_toe'
]

commands_markup = ReplyKeyboardMarkup()
for command in initial_commands:
    commands_markup.insert(KeyboardButton(command))

tic_tac_toe_markup = ReplyKeyboardMarkup()
for i in range(2):
    tic_tac_toe_markup.insert(str(i + 1))


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет! Сыграем в крестики-нолики?", reply_markup=commands_markup)


class TicTacToeState(StatesGroup):
    isWin = State()
    array = State()
    steps = State()
    playerType = State()
    x = State()
    y = State()


@dp.message_handler(commands=['tic_tac_toe'])
async def tic_tac_toe_start_game(message: types.Message, state: FSMContext):
    await message.answer("Для завершения игры вы можете ввести команду 'end' или 'finish' без /")
    await message.answer("Ход игрока x \nВведите строку: ", reply_markup=tic_tac_toe_markup)
    steps = 9
    playerType = 'x'
    isWin = True
    array = [
        ['1', '1', '1'],
        ['1', '1', '1'],
        ['1', '1', '1'],
    ]
    await state.update_data(array=array)
    await state.update_data(playerType=playerType)
    await state.update_data(steps=steps)
    await state.update_data(isWin=isWin)
    await TicTacToeState.x.set()


@dp.message_handler(state=TicTacToeState.x)
async def tic_tac_toe_y(message: types.Message, state: FSMContext):
    if message.text == "end" or message.text == "finish":
        await message.answer("Игра завершена, до новых встреч", reply_markup=commands_markup)
        await state.finish()
        return
    await message.answer("Введите столбец: ")
    await state.update_data(x=message.text)
    await TicTacToeState.y.set()


@dp.message_handler(state=TicTacToeState.y)
async def tic_tac_toe_main(message: types.Message, state: FSMContext):
    if message.text == "end" or message.text == "finish":
        await message.answer("Игра завершена, до новых встреч", reply_markup=commands_markup)
        await state.finish()
        return
    await state.update_data(y=message.text)
    data = await state.get_data()
    if (data['x'].isdigit() and data['y'].isdigit()):
        x = int(data['x'])
        y = int(data['y'])

        array = data['array']

        if (x < 1 or x > 3 or y < 1 or y > 3):
            await message.answer('Данные заполнены неправильно!\nВведите строку: ')
            await TicTacToeState.x.set()
        else:
            if (array[x - 1][y - 1] == '1'):
                playerType = data['playerType']
                array[x - 1][y - 1] = playerType
                steps = int(data['steps'])
                steps -= 1
                await state.update_data(steps=steps)
                await state.update_data(array=array)
            else:
                await message.answer('Клетка занята\nВведите строку: ')
                await TicTacToeState.x.set()

            field = ''
            for i in range(3):
                field_row = ''
                for t in range(3):
                    field_row += array[i][t] + ' '
                field += field_row + '\n'
            await message.answer(field)

            isWin = data['isWin']
            for i in range(3):
                if (array[i][0] == array[i][1] == array[i][2] == playerType):
                    isWin = False
                if (array[0][i] == array[1][i] == array[2][i] == playerType):
                    isWin = False
            if (array[0][0] == array[1][1] == array[2][2] == playerType or array[0][2] == array[1][1] == array[2][
                0] == playerType):
                isWin = False
            if (steps == 0 and isWin == True):
                await message.answer('Ничья', reply_markup=commands_markup)
                await state.finish()
            elif (isWin):
                if (playerType == 'x'):
                    await state.update_data(playerType='y')
                    await message.answer("Ход игрока y \nВведите строку: ")
                    await TicTacToeState.x.set()
                else:
                    await state.update_data(playerType='x')
                    await message.answer("Ход игрока x \nВведите строку: ")
                    await TicTacToeState.x.set()
            else:
                await message.answer("Победил игрок: " + playerType, reply_markup=commands_markup)
                await state.finish()
    else:
        await message.answer('Нужно указывать только цифры или столбцы\nВведите строку: ')
        await TicTacToeState.x.set()


if __name__ == '__main__':
    executor.start_polling(dp)