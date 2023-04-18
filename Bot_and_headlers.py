import asyncio
import threading
from aiogram import Bot, Dispatcher, types
import Script_for_send_photo
from Script_for_camera_detected import camera_on_detected
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from Button import kb_contact, kb_camera
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=MemoryStorage())


# создание класса состояний FSM
class LoginForm(StatesGroup):
    password = State()


# обработчик команды /start
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer("Добрый день!\nЭто частный бот системы видеонаблюдения.\n"
                         "Для подключения необходимо ввести код доступа.", reply_markup=kb_contact)


# обработчик сообщений с паролем
@dp.message_handler(state=LoginForm.password)
async def process_password(message: types.Message, state: FSMContext):
    # если пароль верный
    if message.text == '676869':
        await message.answer("Добро пожаловать в систему!", reply_markup=kb_camera)
        await state.finish()
    # если пароль неверный
    else:
        await message.answer("Неверный код. Введите код доступа:")
        # переход в состояние ввода пароля
        await LoginForm.password.set()


# обработчик команды /login
@dp.message_handler(Text(equals="Подключиться_к_системе"), state='*')
async def cmd_login(message: types.Message):
    # отправка запроса на ввод пароля
    await message.answer("Введите код доступа:")
    await LoginForm.password.set()


@dp.message_handler(lambda message: message.text == "Выключить_видеонаблюдение")
async def turn_off_camera(message: types.Message):
    await message.answer("Система видеонаблюдения выключена")
    os._exit(0)


def start_loop(f):
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(f())
    loop.close()


@dp.message_handler(lambda message: message.text == "Включить_видеонаблюдение")
async def turn_on_camera(message: types.Message):
    # запускаем два потока

    t1 = threading.Thread(target=start_loop, args=(camera_on_detected,))
    t2 = threading.Thread(target=start_loop, args=(Script_for_send_photo.send_photos_for_user,))
    t1.start()
    t2.start()
    await message.answer("Система видеонаблюдения включена")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
