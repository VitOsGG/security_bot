from aiogram import types


b1 = types.KeyboardButton(text="Подключиться_к_системе")
b2 = types.KeyboardButton(text="Включить_видеонаблюдение")
b3 = types.KeyboardButton(text="Выключить_видеонаблюдение")

kb_contact = types.ReplyKeyboardMarkup(resize_keyboard=True)

kb_contact.row(b1)

kb_camera = types.ReplyKeyboardMarkup(resize_keyboard=True)

kb_camera.row(b2).add(b3)

