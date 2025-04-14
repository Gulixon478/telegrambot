from warnings import catch_warnings

import aiogram.types
from aiogram import Bot,Dispatcher,Router,F
from aiogram.filters import Command
from aiogram.types import Message
from asyncio import run
from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from pymsgbox import buttonsFrame
from aiogram.types import CallbackQuery
from os import getenv
from dotenv import load_dotenv
import sys
import logging
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
load_dotenv()


def get_inline() -> InlineKeyboardMarkup:
    inline=InlineKeyboardBuilder()
    inline.button(text="Korea",callback_data="Korea")
    inline.button(text="Soudiya Arabiston",callback_data="Soudiya Arabiston")
    inline.button(text="Japan",callback_data="Japan")
    inline.button(text="China",callback_data="China")
    inline.button(text="Shveysariya",callback_data="Shveysariya")

    inline.adjust(2)
    return inline.as_markup()
def tozalash() -> InlineKeyboardMarkup:
    inline=InlineKeyboardBuilder()
    inline.button(text="Ha",callback_data="Ha")
    inline.button(text="Yo'q",callback_data="Yo'q")
    return inline.as_markup()
#
# def get_ha_yoq() -> ReplyKeyboardMarkup:
#     kb=ReplyKeyboardBuilder()
#     kb.button(text="Ha")
#     kb.button(text="Yoq")
#     kb.adjust(2)

    return kb.as_markup(resize_keyboard=True)

dp=Dispatcher()
tokinim=getenv("BOT_TOKEN")
global tanlov
#@dp.startup()
my_router=Router()

dp.include_router(my_router)
@my_router.startup()
async def bot_ishlaganda(bot:Bot):
    await bot.send_message(chat_id=getenv("MY_ID"),text="Bot ishladi")

@my_router.shutdown()
async def bot_toxtaganda(bot:Bot):
    await bot.send_message(chat_id=getenv("MY_ID"),text="Bot toxtadi")

@my_router.message(Command('start'))
#router  yordamida xabar berish
async def start_bosilganda(m:Message):
    await m.answer("Xush kelibsiz")
    await m.answer("Sizga qaysi davlat yoqadi?",reply_markup=get_inline())

@my_router.callback_query(F.data=="Korea")
async def Korea_tanlanganda(call:CallbackQuery):
    await call.message.edit_text("Yaxshi tanlov qildingiz")
    await call.message.edit_reply_markup(reply_markup=tozalash())
    await call.message.answer("🇰🇷")

@my_router.callback_query(F.data=="Soudiya Arabiston")
async def Soudiya_Arabiston_tanlanganda(call:CallbackQuery):
    await call.message.edit_text("Bu ham yaxshi tanlov")
    await call.message.edit_reply_markup(reply_markup=tozalash())
    await call.message.answer("🇸🇦")


@my_router.callback_query(F.data=="Japan")
async def Japan_tanlanganda(call:CallbackQuery):
    await call.message.edit_text("Siz haqiqatdan Japannii tanlamoqchimisz?")
    await call.message.edit_reply_markup(reply_markup=tozalash())
    await call.message.answer("🇯🇵")


@my_router.callback_query(F.data=="China")
async def China_tanlanganda(call:CallbackQuery):
    await call.message.edit_text("Siz haqiqatdan Chinani tanlamoqchimisz?")
    await call.message.edit_reply_markup(reply_markup=tozalash())
    await call.message.answer("🇨🇳")


@my_router.callback_query(F.data=="Shveysariya")
async def Shveysariya_tanlanganda(call:CallbackQuery):
    await call.message.edit_text("Siz haqiqatdan Shveysariya tanlamoqchimisz?")
    await call.message.edit_reply_markup(reply_markup=tozalash())
    await call.message.answer("🇨🇭")


@my_router.callback_query(F.data == "Yo'q")
async def ha_tanlanganda(call:CallbackQuery):
    await call.message.edit_text("Biror bir davlatni tanlang?: ")
    await call.message.edit_reply_markup(reply_markup=get_inline())

@my_router.callback_query(F.data == "Ha")
async def ha_tanlanganda(call:CallbackQuery):
   # await call.message.edit_reply_markup(reply_markup=get_inline())
    await call.message.delete_reply_markup()
    await call.message.delete()
    global tanlov
    matn=str(tanlov)
    await call.message.answer(f"{matn}ni tanladingiz")
    r=getenv("ADMINS")
    for i in r:
      await call.bot.send_message(chat_id=i, text=f"{call.from_user.full_name}ni tanladi")


#
# @my_router.message(F.text.lower()=="ha")
# async def ha_tanlanganda(m:Message):
#     await m.answer("ooo buyuk vatanparvar",\
#                    reply_markup=aiogram.types.ReplyKeyboardRemove())
#
# @my_router.message(F.text.lower()=="yoq")
# async def yoq_tanlanganda(j:Message):
#     await j.answer("Siz to'g'ri yo'ldasz",\
#                    reply_markup=aiogram.types.ReplyKeyboardRemove())

@my_router.message()
async def xabar_kelganda(m:Message,bot:Bot):
    await m.copy_to(chat_id=m.from_user.id)#
    await m.copy_to(chat_id="6402500187")#
    await m.answer(chat_id="6402500187",\
                   text=f"{m.from_user.full_name}\
                    sizning botingizga '{m.text}' deb yozdi")

async def main():
    botim=Bot(token=tokinim,default=DefaultBotProperties(parse_mode=ParseMode.HTML))
   # dp.startup.register(bot_ishlaganda)
    await dp.start_polling(botim)
if __name__=="__main__":
   logging.basicConfig(level=logging.INFO,\
format="%(asctime)s - %(name)s - %(levelname)s - %(message)s ",\
handlers=[
           logging.FileHandler("bot.log"),
           logging.StreamHandler(sys.stdout)
     ])
   run(main())