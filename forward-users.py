BOT_TOKEN = "********"

from telethon import TelegramClient, events

API_ID = ********
API_HASH = "********"

client = TelegramClient('session', api_id=API_ID, api_hash=API_HASH).start(bot_token=BOT_TOKEN)

@client.on(events.NewMessage(
    chats="********",  # insert group username/ id here
    from_users=[********,"********"]   # insert a user to monitor here
))
async def _(event):
    await event.message.forward_to(********) # insert the username/ id for the receiver chat/channel

with client:
    client.run_until_disconnected()
