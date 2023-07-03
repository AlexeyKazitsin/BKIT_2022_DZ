from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import random

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/description')
b3 = KeyboardButton('/digit')
kb.add(b1).insert(b2).add(b3)

HELP_COMMAND = """
<b>/help</b> - <em>Список команд</em>
<b>/start</b> - <em>Запуск бота</em>
<b>/description</b> - <em>Описание бота</em>
<b>/digit</b> - <em>Генерация случайного числа</em>"""


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_COMMAND,
                           parse_mode="HTML")
    await message.delete()


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Приветствую!",
                           parse_mode="HTML",
                           reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['description'])
async def desc_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Этот бот умеет генерировать случайное число в промежутке от 1 до 1000!",
                           parse_mode="HTML")
    await message.delete()


@dp.message_handler(commands=['digit'])
async def digit_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           random.randint(1, 1000))
    await message.delete()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
