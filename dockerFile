# Використовуємо легкий образ Python
FROM python:3.9-slim

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо файл з залежностями та встановлюємо їх
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо весь код у контейнер
COPY . .

# Відкриваємо порт (хоча Render ігнорує EXPOSE, це гарна практика)
EXPOSE 8080

# Запускаємо додаток через Gunicorn (це надійніше ніж просто python main.py)
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "main:app"]
