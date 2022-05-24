# Бот-ассистент в телеграм
Бот-ассистент для дискорда находится здесь: https://github.com/rgenius-ru/bot_assistant
Оболочка интерфейса взята с примера гитхаба: tm-a-t Artyom Ivanov.

## Как запустить
1. Создайте файл `config.py` 
   (Вам понадобятся токен бота и данные API, которые можно получить на my.telegram.org)
```text
BOT_TOKEN = 'токен-вашего-бота'
API_ID = 123456789
API_HASH = 'ваше-значение'
```
2. Установите зависимости и запустите модуль:
```shell
pip install -r requirements.txt
python -m app
```
