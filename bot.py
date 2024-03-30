import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from config import YOUR_TELEGRAM_BOT_TOKEN, TARGET_CHAT_ID
from send_prompt import send_prompt, tokenizer, model


bot = Bot(YOUR_TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
	await message.answer(f"Привет, {hbold(message.from_user.full_name)}!")

@dp.message()
async def handle_message(message: types.Message):
	answer = send_prompt(message.text)
	await message.reply(answer, parse_mode='HTML')

		
async def main() -> None:
	await dp.start_polling(bot, debug=True)

if __name__ == "__main__":
	logging.basicConfig(stream=sys.stdout)
	asyncio.run(main())