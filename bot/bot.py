import discord
import json
import os
from discord.ext import commands
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()

# Получаем значения из .env
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))  # ID канала как целое число

# Настраиваем intents
intents = discord.Intents.default()
# intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Инициализация JSON-файла
if not os.path.exists('../data.json'):
    with open('../data.json', 'w') as f:
        json.dump({"messages": [], "online_count": 0}, f)

@bot.event
async def on_ready():
    print(f'Бот {bot.user} запущен!')

@bot.event
async def on_message(message):
    # Проверяем, что сообщение из нужного канала
    if message.channel.id == CHANNEL_ID:
        with open('../data.json', 'r') as f:
            data = json.load(f)
        
        # Обновляем сообщения
        data["messages"].append(message.content)
        data["messages"] = data["messages"][-3:]  # Оставляем последние 3
        
        # Обновляем количество людей онлайн
        guild = message.guild
        online_count = sum(1 for member in guild.members if member.status != discord.Status.offline)
        data["online_count"] = online_count
        
        # Сохраняем данные
        with open('../data.json', 'w') as f:
            json.dump(data, f)

bot.run(TOKEN)
