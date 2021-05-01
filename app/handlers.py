from telethon import events
from telethon.tl.custom import Message
from telethon.tl.types import InputMediaDice
from app import bot
from random import choice


@bot.on(events.ChatAction(func=lambda e: e.is_group and e.user_added and e.user_id == bot.me.id))
async def on_join(event: events.ChatAction.Event):
    await event.respond('Приветствую, господа!')


@bot.on(events.NewMessage(func=lambda e: e.text.lower() in [
                                         "привет",
                                         "прив",
                                         "hi",
                                         "hello",
                                         "здарова"
                          ]))
async def hi(event: Message):
    answers = [
        "привет",
        "как дела?",
        "уже виделись",
        "...",
        "здарова",
    ]
    await event.respond(choice(answers))


@bot.on(events.NewMessage(func=lambda e: e.text.lower() == 'ты кто?'))
async def who_are_you(event: Message):
    await event.respond('Я умный, красивый, в меру упитанный мужчина в полном расцвете сил!')


@bot.on(events.NewMessage(func=lambda e: e.text.lower() == '/dice'))
async def send_dice(event: Message):
    await bot.send_message(event.chat.id, file=InputMediaDice('?'))


@bot.on(events.ChatAction(func=lambda e: (e.user_added or e.user_joined) and e.user_id != bot.me.id))
async def greet(event: events.ChatAction.Event):
    await event.respond('Приветик!')


@bot.on(events.NewMessage(func=lambda e: e.text.lower() == '/img'))
async def send_cat(event: Message):
    await bot.send_message(event.chat.id, file='Media/Images/Vector.gif')
