from telethon import events, utils, client
from telethon.tl.custom import Message
from app import bot
from app import dialogue as dlg
from app import commands as comm


@bot.on(events.ChatAction(func=lambda e: e.is_group and e.user_added and e.user_id == bot.me.id))
async def on_join(event: events.ChatAction.Event):
    await event.respond('Приветствую, господа!')


@bot.on(events.ChatAction(func=lambda e: (e.user_added or e.user_joined) and e.user_id != bot.me.id))
async def greet(event: events.ChatAction.Event):
    await event.respond('Приветик!')


@bot.on(events.NewMessage())
async def any_message(event: Message):
    print(event.date, event.text)

    # if ignore(message):
    #     return

    response = comm.on_command(event.text)  # Проверка на команду, и ответ на неё

    if not response:  # Если ответа нет
        response = dlg.start_dialogue(event.text)  # Запуск диалога

    await event.respond(response)
