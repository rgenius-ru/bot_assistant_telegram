from telethon import events

from app import bot


@bot.on(events.ChatAction(func=lambda e: e.is_group and e.user_added and e.user_id == bot.me.id))
async def on_join(event: events.ChatAction.Event):
    await event.respond('Приветствую, господа!')
