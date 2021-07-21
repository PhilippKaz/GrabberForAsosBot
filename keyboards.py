from aiogram import Bot, types
from currency import *

#Фукнция для выбора языка
def language_button_settings():
    keyboard_language = types.ReplyKeyboardMarkup(resize_keyboard=True)
    CALLBACK_BUTTON_RUS = u'\U0001F1F7' + u'\U0001F1FA' + " Русский"
    CALLBACK_BUTTON_ENG = u'\U0001F1FA' + u'\U0001F1F8' + " English"
    buttons = [CALLBACK_BUTTON_RUS,
               CALLBACK_BUTTON_ENG]
    keyboard_language.add(*buttons)
    return keyboard_language


#Фукнция для выбора валюты
def currency_button_settings():
    keyboard_currency = types.ReplyKeyboardMarkup(resize_keyboard=True)
    CALLBACK_BUTTON_AUD = "AUD"
    CALLBACK_BUTTON_EUR = "EUR"
    CALLBACK_BUTTON_GBP = "GBP"
    CALLBACK_BUTTON_RUB = "RUB"
    CALLBACK_BUTTON_USD = "USD"
    CALLBACK_BUTTON_SEK = "SEK"
    CALLBACK_BUTTON_DKK = "DKK"
    CALLBACK_BUTTON_PLN = "PLN"
    CALLBACK_BUTTON_SGD = "SGD"
    CALLBACK_BUTTON_CHF = "CHF"
    CALLBACK_BUTTON_HKD = "HKD"
    CALLBACK_BUTTON_ILS = "ILS"
    CALLBACK_BUTTON_CAD = "CAD"
    CALLBACK_BUTTON_CNY = "CNY"
    CALLBACK_BUTTON_NZD = "NZD"
    CALLBACK_BUTTON_NOK = "NOK"
    CALLBACK_BUTTON_AED = "AED"
    CALLBACK_BUTTON_SAR = "SAR"
    CALLBACK_BUTTON_TWD = "TWD"
    CALLBACK_BUTTON_UAH = "UAH"
    CALLBACK_BUTTON_KZT = "KZT"
    CALLBACK_BUTTON_AZN = "AZN"
    buttons = [
                CALLBACK_BUTTON_AUD,
                CALLBACK_BUTTON_EUR,
                CALLBACK_BUTTON_GBP,
                CALLBACK_BUTTON_RUB,
                CALLBACK_BUTTON_USD,
                CALLBACK_BUTTON_SEK,
                CALLBACK_BUTTON_DKK,
                CALLBACK_BUTTON_PLN,
                CALLBACK_BUTTON_SGD,
                CALLBACK_BUTTON_CHF,
                CALLBACK_BUTTON_HKD,
                CALLBACK_BUTTON_ILS,
                CALLBACK_BUTTON_CAD,
                CALLBACK_BUTTON_CNY,
                CALLBACK_BUTTON_NZD,
                CALLBACK_BUTTON_NOK,
                CALLBACK_BUTTON_AED,
                CALLBACK_BUTTON_SAR,
                CALLBACK_BUTTON_TWD,
                CALLBACK_BUTTON_UAH,
                CALLBACK_BUTTON_KZT,
                CALLBACK_BUTTON_AZN
            ]

    keyboard_currency.add(*buttons)
    return keyboard_currency

