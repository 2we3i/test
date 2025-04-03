import os

# Определяем путь до data.json
BASE_DIR = os.path.dirname(os.path.abspath(website/templates/index.html))  # Находим путь к website/
DATA_PATH = os.path.join(BASE_DIR, "../data.json")  # Подключаем data.json

@app.route('/')
def index():
    try:
        with open(DATA_PATH, 'r', encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {"messages": [], "online_count": 0}  # Если файла нет, загружаем пустые данные
    
    return render_template('index.html', 
                          messages=data.get("messages", []), 
                          online_count=data.get("online_count", 0), 
                          invite_link=INVITE_LINK)
