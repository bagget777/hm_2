from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.storage import FSMContext
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from config import token
import sqlite3, logging

bot = Bot(token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)

Keyboard_buttons = [
    KeyboardButton('/backend'),
    KeyboardButton('/frontend'),
    KeyboardButton('/android'),
    KeyboardButton('/ios'),
    KeyboardButton('ui/ux'),
    KeyboardButton('привет')
]
Keyboard_one = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(*Keyboard_buttons)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer("Здравствуйте\nВыберите направление", reply_markup=Keyboard_one)
    
@dp.message_handler(commands = ['start'])
async def start(message:types.Message):
    await message.answer(f'Здраствуйте {message.from_user.full_name}\nВыберите направление:\n/backend\n/frontend\n/uiux\n/android\n/ios')

@dp.message_handler(commands = ['backend'])
async def back(message:types.Message):
    await message.answer(f'Backend — это внутренняя часть сайта и сервера и т.д\nСтоимость 10000 сом в месяц\nОбучение: 5 месяц')
    
@dp.message_handler(commands = ['frontend'])
async def back(message:types.Message):
    await message.answer(f'Fronted — это внешняя часть сайта и сервера и т.д\nСтоимость 10000 сом в месяц\nОбучение: 5 месяц')
    
@dp.message_handler(commands = ['uiux'])
async def back(message:types.Message):
    await message.answer(f'UIUX — это дизайн сайта и сервера и т.д\nСтоимость 10000 сом в месяц\nОбучение: 5 месяц')
    
@dp.message_handler(commands = ['android'])
async def back(message:types.Message):
    await message.answer(f'Android — это создание приложения для устройств на операционной системе Android\nСтоимость 10000 сом в месяц\nОбучение: 5 месяц')
    
@dp.message_handler(commands = ['ios'])
async def back(message:types.Message):
    await message.answer(f'IOS — это это создание приложения для устройств на операционной системе IOS\nСтоимость 10000 сом в месяц\nОбучение: 5 месяц')
    
executor.start_polling(dp)