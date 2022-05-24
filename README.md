# Бот-ассистент в телеграм
Бот-ассистент для дискорда находится здесь: https://github.com/rgenius-ru/bot_assistant

Оболочка интерфейса взята с примера гитхаба: tm-a-t Artyom Ivanov.

## Как запустить
1. Создайте файл `.env` со следующим содержимым:
```text
# Токен и API бота, которые можно получить на my.telegram.org
TELEGRAM_BOT_TOKEN=токен-твоего-бота
TELEGRAM_API_ID=123456789
TELEGRAM_API_HASH=твоё-значение

# Логин и пароль базы данных mongodb
mongo_login=твой-логин
mongo_pass=твой-пароль
```
2. Установите зависимости и запустите модуль:
```shell
pip install -r requirements.txt
python -m app
```
