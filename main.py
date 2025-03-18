from aiogram import Bot, Dispatcher, executor, types
from data.config import BOT_TOKEN
from handlers import start, menu, ravza, food, hotel, faq, bozor

import asyncio  # <-- Keep-alive uchun kerak

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

# Handlers ro'yxatdan o'tkazish
start.register_handlers_start(dp)
menu.register_handlers_menu(dp)
ravza.register_handlers_ravza(dp)
hotel.register_handlers_hotel(dp)
food.register_handlers_food(dp)
faq.register_handlers_faq(dp)
bozor.register_handlers_bozor(dp)

# 🔄 Yashirin keep-alive funksiyasi
async def keep_alive():
    while True:
        await asyncio.sleep(600)  # Har 10 daqiqada ishga tushadi
        print("🔄 Bot alive ping...")  # Faqat logda chiqadi, foydalanuvchiga emas

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(keep_alive())  # Keep-alive task ishga tushdi
    executor.start_polling(dp, skip_updates=True)
