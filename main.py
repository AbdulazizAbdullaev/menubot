# main.py

import logging
from aiogram import Bot, Dispatcher, executor, types
from telegram import ReplyMarkup
import markups as nav
import random

TOKEN = '5268667834:AAGBRRnbYM6ZvUMVdJuyzcUFjfwguo07J5A'

# logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, f'Salom {message.from_user.first_name}', reply_markup = nav.lang)
    
@dp.message_handler()
async def bot_message(message: types.Message):
    # await bot.send_message(message.from_user.id, message.text)
    if message.text == '🇺🇿 O`zbekcha':
        await bot.send_message(message.from_user.id, 'Menyu', reply_markup = nav.btnuzb)
       
        
    elif message.text == '👪Jismoniy shaxslar':
        await bot.send_message(message.from_user.id, '👪Jismoniy shaxslar', reply_markup = nav.btnjismoniyasos)
    elif message.text == '💳Plastik kartalar':
        await bot.send_message(message.from_user.id, "💳Plastik kartalar", reply_markup = nav.btnkartalar)     

    elif message.text == '🏠 Bosh menu':
        await bot.send_message(message.from_user.id, "🏠 Bosh menu", reply_markup = nav.btnuzb) 

    
    elif message.text == '◀️ Orqaga':
        await bot.send_message(message.from_user.id, "◀️ Orqaga", reply_markup = nav.btnjismoniyasos) 


    elif message.text == '➡ Other':
        await bot.send_message(message.from_user.id, "➡ Other", reply_markup = nav.otherMenu) 
    
    elif message.text == '⚙️ Sozlamalar':
        await bot.send_message(message.from_user.id, '⚙️ Sozlamalar', reply_markup = nav.btnsozlamalar)

    elif message.text == '🌏 Til':
        await bot.send_message(message.from_user.id, '🌏 Til', reply_markup = nav.lang)
 

    elif message.text == '📚 Information':
        await bot.send_message(message.from_user.id, "📚 Information", reply_markup = nav.subOtherMenu)
        
    elif message.text == '📈 Exchange Rate':
        await bot.send_message(message.from_user.id, "📈 Exchange Rate") 
        
    else:
        await message.reply('No data')
    
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)