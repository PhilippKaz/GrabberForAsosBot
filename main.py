from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor

from config import token
from keyboards import *
from states.settings import Settings
from keyboards import *
from users import Users

bot = Bot(token=token)

dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'], state=None)
async def process_start_command(message: types.message):
    keyboard_language = language_button_settings()
    await message.answer("Выберите язык интерфейса\nSelect the interface language", reply_markup=keyboard_language)
    await Settings.stepSetLanguage.set()


@dp.message_handler(state=Settings.stepSetLanguage)
async def choose_language_user(message: types.Message, state: FSMContext):
    keyboard_currency = currency_button_settings()
    await message.answer("Выберите валюту конвертации", reply_markup=keyboard_currency)
    language_user = message.text
    await state.update_data(language=language_user)
    await Settings.stepSetCurrency.set()


@dp.message_handler(state=Settings.stepSetCurrency)
async def choose_currency_user(message: types.Message, state: FSMContext):
    currency_user = message.text
    await state.update_data(currency=currency_user)
    await Settings.stepFinishInitSetup.set()
    id_user = message.chat.id
    username = message.chat.username
    first_name = message.chat.first_name
    data_user = await state.get_data()
    if data_user['language'] == u'\U0001F1F7' + u'\U0001F1FA' + " Русский":
        language = "RU"
    elif data_user['language'] == u'\U0001F1FA' + u'\U0001F1F8' + " English":
        language = "EN"
    currency = data_user['currency']
    users = Users()
    users.insert_new_user(id_user, username, first_name, language, currency)




if __name__ == '__main__':
    executor.start_polling(dp)
