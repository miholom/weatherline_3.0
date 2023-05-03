from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU
from aiogram import F


router: Router = Router()


# Хэндлер для сообщений, которые не попали в другие хэндлеры
@router.message()
async def send_answer(message: Message):
    if message.text:
        await message.answer(text=LEXICON_RU['other_answer'])
    else:
        pass