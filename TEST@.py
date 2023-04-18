import time
import shutil
import os

old_folder_path = r"Z:\\IT_files\\PycharmProjects\\Web_camera\\Object_detected\\"
new_folder_path = r"Z:\\IT_files\\PycharmProjects\\Web_camera\\Object_detected_collect\\"

while True:
    photos = [f for f in os.listdir(old_folder_path) if f.endswith('.jpg')]
    for photo in photos:
        # await send_photo(photo_file)
        # await asyncio.sleep(2)  # адержка между отправками фото
        old_path = os.path.join(old_folder_path, photo)
        new_path = os.path.join(new_folder_path, photo)
        shutil.move(old_path, new_path)
        time.sleep(3)

