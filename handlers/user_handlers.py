from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import CallbackQuery, Message
from keyboards.keyboards import create_pagination_keyboard
from lexicon.lexicon_ru import LEXICON_RU
from services.services import weather, TIME
import logging
import time as time_
from datetime import datetime

router: Router = Router()


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    user_name = message.from_user.first_name
    logging.info(f"{user_id} {user_full_name}", time_.asctime())
    text = LEXICON_RU['/start']
    await message.answer(text=text,
                        reply_markup=create_pagination_keyboard(
                        'wheather',
                        'always_weather',
                        'geolocation',
                        ))


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    user_name = message.from_user.first_name
    logging.info(f"{user_id} {user_full_name}", time_.asctime())
    text = LEXICON_RU['/help']
    await message.answer(text=text,
                        reply_markup=create_pagination_keyboard(
                        'wheather',
                        'always_weather',
                        'geolocation',
                        ))


# Этот хэндлер срабатывает на согласие пользователя играть в игру
@router.callback_query(Text(text='wheather'))
async def process_wheather_answer(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    user_full_name = callback.from_user.full_name
    user_name = callback.from_user.first_name
    logging.info(f"{user_id} {user_full_name} {user_name}", time_.asctime())
    text = f"{user_full_name}, {weather()}"
    await callback.message.answer(text=text,
                        reply_markup=create_pagination_keyboard(
                        'wheather',
                        'always_weather',
                        'geolocation',
                        ))
    

@router.callback_query(Text(text='geolocation'))
async def process_geolocation_answer(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    user_full_name = callback.from_user.full_name
    user_name = callback.from_user.first_name
    logging.info(f"{user_id} {user_full_name} {user_name}", time_.asctime())
    text = f"{user_full_name}, {weather()}"
    await callback.message.answer(text=text, request_location=True, 
                        reply_markup=create_pagination_keyboard(
                        'wheather',
                        'always_weather',
                        'geolocation',
                        ))
    

@router.callback_query(Text(text='always_weather'))
async def process_always_weather_answer(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    user_full_name = callback.from_user.full_name
    user_name = callback.from_user.first_name
    logging.info(f"{user_id} {user_full_name} {user_name}", time_.asctime())
    while True:
            now = datetime.now()
            dt_string = now.strftime("%H:%M:%S")
            for i in TIME:
                if dt_string == i:
                    time_.sleep(1)
                    text = f"{user_full_name}, {weather()}"
                    await callback.message.answer(text=text, 
                                        reply_markup=create_pagination_keyboard(
                                        'wheather',
                                        'always_weather',
                                        'geolocation',
                                        ))