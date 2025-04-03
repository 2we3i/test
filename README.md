
```markdown
# Discord Messages

Веб-приложение для отображения последних 3 сообщений из канала Discord, количества участников онлайн и кнопки для присоединения к серверу.

## Особенности
- Отображение последних 3 сообщений из указанного канала.
- Показ количества участников онлайн.
- Кнопка "Присоединиться" с ссылкой на сервер.
- Конфиденциальные данные в `.env`.

## Структура проекта
```
discord-messages/
├── templates/
│   └── index.html
├── .env
├── bot.py
├── app.py
├── data.json
├── requirements.txt
└── README.md
```

## Требования
- Python 3.8+
- Discord Bot Token
- Intents: `Message Content Intent`, `Server Members Intent`

## Установка

1. Склонируйте репозиторий:
   ```
   git clone <repository_url>
   cd discord-messages
   ```
2. Установите зависимости:
   ```
   pip install -r requirements.txt
   ```
3. Настройте `.env`:
   ```
   DISCORD_TOKEN=your_bot_token_here
   CHANNEL_ID=your_channel_id_here
   INVITE_LINK=https://discord.gg/your_invite_link_here
   ```

## Запуск

1. Запустите бота:
   ```
   python bot.py
   ```
2. Запустите веб-сервер:
   ```
   python app.py
   ```
3. Откройте `http://localhost:5000`.

## Использование
- Сообщения из канала появляются на сайте.
- Онлайн обновляется при новом сообщении.
- Кнопка ведёт на сервер.

## Примечания
- Бот мониторит только канал из `CHANNEL_ID`.
- `data.json` создаётся автоматически.
- Добавьте `.env` и `data.json` в `.gitignore`.
```
