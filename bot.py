import discord
import os

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True  # bật nếu cần đọc chat

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Bot đã online: {client.user}")
    await client.change_presence(
        activity=discord.Game(name="AFK 24/7")
    )

client.run(TOKEN)
