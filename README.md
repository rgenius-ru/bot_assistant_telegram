# Хардкорная разработка под Телеграм. Бот-модератор своими руками
Это репозиторий для [серии статей на Хабре](https://habr.com/ru/post/553968/) — 
туториала по созданию своего бота-модератора групп в Телеграме.

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
