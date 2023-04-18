from aiogram import types
from Bot_and_headlers import bot
import os
import asyncio
import shutil


async def send_photo(photo_file):
    # Отправка фото в чат
    with open(photo_file, 'rb'):
        photo = types.InputFile(photo_file)
        await bot.send_photo(chat_id=613882626, photo=photo)


async def send_photos_for_user():
    # Отправка всех фото из папки в чат
    old_folder_path = r"Z:\\IT_files\\PycharmProjects\\Web_camera\\Object_detected\\"
    new_folder_path = r"Z:\\IT_files\\PycharmProjects\\Web_camera\\Object_detected_collect\\"

    while True:
        photos = [p for p in os.listdir(old_folder_path) if p.endswith('.jpg')]
        for photo in photos:
            photo_file = os.path.join(old_folder_path, photo)
            await send_photo(photo_file)
            await asyncio.sleep(1)  # задержка между отправками фото
            old_path = os.path.join(old_folder_path, photo)
            new_path = os.path.join(new_folder_path, photo)
            shutil.move(old_path, new_path)
            await asyncio.sleep(1)

    # import shutil
    # import os
    #
    # old_folder_path = r"Z:\IT_files\PycharmProjects\Web_camera\Object_detected\\"
    # new_folder_path = r"Z:\IT_files\PycharmProjects\Web_camera\Object_detected_collect\\"
    #
    # # Получаем список всех фото в директории old_folder_path
    # photos = [f for f in os.listdir(old_folder_path) if f.endswith('.jpg')]
    #
    # # Перемещаем каждое фото в новую директорию new_folder_path
    # for photo in photos:
    #     old_path = os.path.join(old_folder_path, photo)
    #     new_path = os.path.join(new_folder_path, photo)
    #     shutil.move(old_path, new_path)
    #
    # while True:
    #     if os.path.exists(directory):
    #         photos = [f for f in os.listdir(directory) if f.endswith('.jpg')]
    #         photo_file = os.path.join(directory, photo)
    #         await send_photo(photo_file)
    #         await asyncio.sleep(2)  # задержка между отправками фото
    #         shutil.move(directory, file_destination)
    #         await asyncio.sleep(2)
    #     else:
    #         # файл не существует
