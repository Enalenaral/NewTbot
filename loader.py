from aiogram import Bot, Dishatcher, types
import config

bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")
dp = Dishatcher(bot)
