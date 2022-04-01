# markups.py
from operator import truediv
from tkinter.tix import Tree
from turtle import width
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton('🏠 Bosh menu')
btnOtherMain = KeyboardButton('⬅ Qaytish')
btnFoodMain = KeyboardButton('⬅ Qaytish')

# Main Menu :
btnUzbek = KeyboardButton('🇺🇿 O`zbekcha')
btnRus = KeyboardButton('🇷🇺 Русский')
btnEng = KeyboardButton('🇬🇧English')
btnOther = KeyboardButton('➡ Other')
#mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnRandom, btnFood, btnOther)

lang = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(btnUzbek, btnRus, btnEng)


# Other Menu :
btnInfo = KeyboardButton('📚 Information')
btnMoney = KeyboardButton('📈 Exchange Rate')
otherMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnInfo, btnMoney, btnMain)

# Sub Other Menu:
subOtherMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnOtherMain)

# menu uzbek:
btnjismoniy= KeyboardButton('👪Jismoniy shaxslar')
btnqaytishplastik= KeyboardButton('⬅ Asosiy menyu')
#jismoniy 

btnkredit= KeyboardButton('💼Kreditlar')
btnpulotqazma= KeyboardButton('💸Pul o`tkazmalari')
btnomonat= KeyboardButton('💰Omonatlar')
btn= KeyboardButton('👪Jismoniy shaxslar')
##########################################
btnplastik= KeyboardButton('💳Plastik kartalar')
btnuzcard=KeyboardButton('UZCARD')
btnhumo=KeyboardButton('HUMO')
btnvisaclas=KeyboardButton('VISA CLASSIC')
btnuhumomastercard=KeyboardButton('HUMO MASTERCARD')
btnmiruzcard=KeyboardButton('МИР-Uzcard')
btnkobeyjing=KeyboardButton('KOBEYJING')
btnorqagaplastik = KeyboardButton('◀️ Orqaga')
##########################################
btnkorpot= KeyboardButton('🏭Korporativ mijozlarga')
btnmanzillar= KeyboardButton('📍Manzillar')
btnvalyuta= KeyboardButton('💵Valyuta kurslari')
btnyangilik= KeyboardButton('🌎 Yangiliklar')
btnboglanish= KeyboardButton('🏦 Bog`lanish')
btntil=KeyboardButton('🌏 Til')
btnqaytish = KeyboardButton('⚙️ Sozlamalar')


btnsozlamalar=ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(btntil, btnMain)
btnkartalar=ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(btnuzcard, btnhumo, btnvisaclas, btnuhumomastercard, btnmiruzcard, btnkobeyjing, btnorqagaplastik, btnMain)
btnjismoniyasos= ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(btnplastik, btnkredit, btnpulotqazma, btnomonat, btnMain)
btnuzb = ReplyKeyboardMarkup(resize_keyboard= True, row_width=2).add(btnjismoniy,  btnkorpot, btnmanzillar,  btnvalyuta, btnyangilik, btnboglanish, btnqaytish)



