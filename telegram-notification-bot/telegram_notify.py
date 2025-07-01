
---

## telegram-notification-bot/telegram_notify.py

```python
from telethon import TelegramClient, events

api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'

client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(pattern='hello'))
async def handler(event):
    await event.reply('Hi! This is an automated reply from Shayan\'s bot.')

async def main():
    await client.start()
    print("Bot is running...")
    await client.run_until_disconnected()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
