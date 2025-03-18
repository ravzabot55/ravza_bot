# main.py (asosiy fayl)
from aiogram import Bot, Dispatcher, executor, types
from data.config import BOT_TOKEN
from handlers import start, menu, ravza, food, hotel, faq, bozor

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

# Har bir bo'limni ro'yxatdan o'tkazamiz
start.register_handlers_start(dp)
menu.register_handlers_menu(dp)
ravza.register_handlers_ravza(dp)
hotel.register_handlers_hotel(dp)
food.register_handlers_food(dp)
faq.register_handlers_faq(dp)
bozor.register_handlers_bozor(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
