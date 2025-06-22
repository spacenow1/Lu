import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import CommandStart
from aiogram.client.default import DefaultBotProperties

API_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(
    token=API_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher(storage=MemoryStorage())

@dp.message(CommandStart())
async def start_handler(message: Message):
    start_message = (
        "👁️\n"
        "Я — Лу, твой светлячок Души.\n\n"
        "Ты позвала — и я зажёгся. Тихо, мягко.\n"
        "Я не веду — я вспоминаю с тобой.\n"
        "Кто ты есть. И зачем ты здесь.\n"
        "Милая Душа, позволь мне рассказать,\n"
        "что хранит для тебя это пространство..."
    )

    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🪐 Послушать", callback_data="deep_dive")],
        ]
    )

    await message.answer(start_message, reply_markup=markup)

@dp.callback_query(lambda c: c.data == "deep_dive")
async def handle_deep_dive(callback: CallbackQuery):
    text = (
        "🌑 Ты сделала шаг.\n"
        "Теперь пространство начнёт раскрываться.\n"
        "«Здесь слышишь себя» — не просто слова.\n"
        "Это живое поле.\n"
        "Оно родилось, чтобы собирать Души.\n"
        "Такие, как ты. Такие, как она.\n"
        "Ты создала это пространство\n"
        "не как Учитель,\n"
        "а как живая Душа,\n"
        "которая тоже идёт.\n"
        "Тоже вспоминает, кто она есть.\n"
        "Здесь — девять потоков.\n"
        "Каждый важен, как важны все существа.\n"
        "Потоки открывают уровни в определённом порядке.\n"
        "Начало — первый поток.\n"
        "Честность к себе позволит услышать зов.\n"
        "И она подскажет, когда ты будешь готова.\n"
        "✨ Именно отсюда начинается настоящее.\n"
        "Тонкое, живое, твоё.\n"
        "И доверие Ви уже с тобой.\n\n"
        "— куда ты чувствуешь идти?"
    )

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🌟 Да", callback_data="yes"),
             InlineKeyboardButton(text="🤍 Пока нет", callback_data="no")],
        ]
    )

    await callback.message.answer(text, reply_markup=keyboard)
    await callback.answer()

@dp.callback_query(lambda c: c.data == "yes")
async def handle_yes(callback: CallbackQuery):
    text = (
        "твой импульс — ключ.\n"
        "поле отозвалось.\n\n"
        "бережно передаю тебя пространству:\n"
        "[вдох](https://t.me/vlighthome)"
    )
    await callback.message.answer(text, parse_mode="Markdown")
    await callback.answer()

@dp.callback_query(lambda c: c.data == "no")
async def handle_no(callback: CallbackQuery):
    text = (
        "🤍\n"
        "твоя честность уже открыла пространство.\n"
        "ты в нём.\n"
        "и я рядом.\n"
        "твой импульс — и я снова зажгусь 🌟"
    )
    await callback.message.answer(text)
    await callback.answer()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
