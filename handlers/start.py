# handlers/start.py
from aiogram import types, Dispatcher
from keyboards.reply import tillar
from aiogram.dispatcher.filters import Command

# Foydalanuvchi start bosganda ishlaydigan funksiya
t_user_lang = {}

async def start_handler(message: types.Message):
    await message.answer("👇 Iltimos, tilni tanланг:", reply_markup=tillar)  # Faqat Til tanlash chiqadi

# Til tanlaganda ushlab qolamiz
async def language_selected(message: types.Message):
    user_id = message.from_user.id
    lang = message.text
    t_user_lang[user_id] = lang

    if lang == "🇺🇿 O'zbekcha":
        text = (
            "🕌 Ассалому алайкум муҳтарам зиёратчи!\n\n"
            "Сиз Равза, Макка ва Мадина хизмати ботидасиз.\n"
            "Бот орқали Равзага навбат олиш, меҳмонхона хизматлари ва таомлар ҳақида маълумот олишингиз мумкин.\n\n"
            "📌 Равза хизмати нархи: 5 SR\n"
            "Кимки биздан 5 SRга олиб, уни 10 SR ёки ундан юқори нархда сотса — биз рози эмасмиз.\n"
            "Биз зиёратчиларга енгиллик беришни истаймиз, мушкуллик келтиришни эмас.\n\n"
            "📜 Ҳадис:\nالمسلم أخو المسلم، لا يظلمه ولا يسلمه\n"
            "“Мусулмон — мусулмоннинг биродаридир. Унга зулм қилмайди ва ташлаб қўймайди.”\n"
            "📚 Ровий: Имом Бухорий\n\n"
            "📣 Муҳим эслатма:\n"
            "Гуруҳ раҳбарлари ва умра ширкати масъулларига:\n"
            "Мадинаи Мунавварага гуруҳингиз келишига 3–5 кун қолганда визаларни бизга юборинг.\n"
            "Сиз келгунингизгача шу сана учун навбат олиб қўйилади, иншаАллоҳ.\n\n"
            "👇 Қуйидаги меню орқали бўлимни танланг:"
        )
        from keyboards.reply import menu_uz
        await message.answer(text, reply_markup=menu_uz)

    elif lang == "🇷🇺 Русский":
        text = (
            "🕌 Уважаемый паломник, добро пожаловать!\n\n"
            "Вы находитесь в боте обслуживания Раудат и гостиниц в Мекке и Медине.\n"
            "Через бот вы можете записаться в Раудат.\n\n"
            "📌 Цена услуги Раудат: 5 SR\n"
            "📜 Хадис:\nالمسلم أخو المسلم، لا يظلمه ولا يسلمه\n"
            "📚 Передал Имам Бухари\n\n"
            "📣 Важно:\nПожалуйста, присылайте визы за 3–5 дней до прибытия группы."
        )
        from keyboards.reply import menu_ru
        await message.answer(text, reply_markup=menu_ru)

    elif lang == "🇸🇦 العربية":
        text = (
            "🕌 مرحبًا أيها الزائر الكريم!\n\n"
            "أنت الآن في بوت خدمة الروضة والفنادق في مكة والمدينة.\n"
            "يمكنك من خلال هذا البوت الحجز في الروضة فقط.\n\n"
            "📌 سعر خدمة الروضة: 5 ريال سعودي\n"
            "📜 الحديث:\nالمسلم أخو المسلم، لا يظلمه ولا يسلمه\n"
            "📚 رواه البخاري\n\n"
            "📣 تنبيه مهم:\nيرجى إرسال التأشيرات قبل 3-5 أيام من وصول المجموعة إلى المدينة المنورة."
        )
        from keyboards.reply import menu_ar
        await message.answer(text, reply_markup=menu_ar)

# Handlerlarni ro‘yxatdan o‘tkazamiz
def register_handlers_start(dp: Dispatcher):
    dp.register_message_handler(start_handler, Command("start"))
    dp.register_message_handler(language_selected, lambda message: message.text in ["🇺🇿 O'zbekcha", "🇷🇺 Русский", "🇸🇦 العربية"])
