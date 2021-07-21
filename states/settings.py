from aiogram.dispatcher.filters.state import StatesGroup, State

class Settings(StatesGroup):
    stepSetLanguage = State()
    stepSetCurrency = State()
    stepFinishInitSetup = State()