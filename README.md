# security_bot
![Python](https://img.shields.io/badge/Python-3.11.0-yellow) ![aiogram](https://img.shields.io/badge/aiogram-blue) ![imageai](https://img.shields.io/badge/imageai-blue)
![tensorflow](https://img.shields.io/badge/tensorflow-blue) ![cv2](https://img.shields.io/badge/cv2-blue) ![asyncio](https://img.shields.io/badge/asyncio-blue) 
![threading](https://img.shields.io/badge/threading-blue) 


Данный проект - это система охраны вашего дома, офиса или другого помещения и имущества. Камера (например обычная веб-камера вашего ноутбука или компьютера)
включается и с помощью библиотеки компьютерного зрения фиксирует то, что вы хотите отслеживать и оправляет в чат телеграмм бота.

![1](https://user-images.githubusercontent.com/114734775/232852656-e83eb029-4308-4bb2-a9f7-6a681e4b5e81.jpg) ![2](https://user-images.githubusercontent.com/114734775/232806804-37ee6a2e-cbf0-4e36-beb2-b3ddf0936797.jpg)
![3](https://user-images.githubusercontent.com/114734775/232807481-daf59656-6e17-43d9-b077-ae949fb25b0f.jpg)

**Структура проекта:**
* Папка venv

  Не добавлена на GitHUB из-за большого размера (список всех библиотек хранится в документе requirements.txt)
    
* Папка File_for_study

  Пакет с файлом yolov3.pt. Не добавлена из-за большого размера. Файл необходим для обучения и доступен по ссылке в документации библиотеки компьютерного зрения imageai.

* Папка Object_detected
  
  Папка куда сохраняется фото зафиксированных камерой объектов.
  
* Папка Object_detected_collect

  Папка куда сохраняется фото зафиксированных камерой объектов после отпрвки их в чат (архив фото).
  
* Файл Bot_and_headlers

  Файл с хэндлирами и телом бота.
  
* Файл Script_for_camera_detected

  Файл с функцией, которая запускает камеру и опеределяет объекты.
  
* Файл Script_for_send_photo

  Файл с функцией, которая отправлется фото с объектами в чат и переносит фото в архив
  
* Файл Button

  Файл с кнопками для бота


  
  



