import discord
import os

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True  # cần để đọc tin nhắn !test

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # test bot
    if message.content == "!test":
        await message.channel.send("bot cua toi day")

    # (chuẩn bị sẵn) lệnh vào voice sau này
    if message.content.startswith("!join"):
        if message.author.voice:
            channel = message.author.voice.channel
            await channel.connect()
            await message.channel.send("Da vao voice!")
        else:
            await message.channel.send("Ban khong o trong voice!")

client.run(TOKEN)
