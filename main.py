import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Додаємо CORS, як було в твоєму JS коді (Access-Control-Allow-Origin: *)
CORS(app)

@app.route('/', methods=['GET', 'POST', 'OPTIONS'])
def http_entry():
    # Якщо це OPTIONS запит (pre-flight), повертаємо 204
    if request.method == 'OPTIONS':
        return '', 204

    # Отримуємо ім'я з параметрів URL або з тіла JSON
    name = request.args.get('name')
    if not name and request.is_json:
        name = request.json.get('name')
    
    if not name:
        name = 'world'

    # Формуємо відповідь
    response = {
        'hello': name,
        'runtime': 'python-flask',
        # Регіон беремо зі змінних середовища Render або ставимо unknown
        'region': os.environ.get('RENDER_REGION', 'unknown') 
    }
    
    return jsonify(response)

if __name__ == '__main__':
    # Render передає порт через змінну оточення PORT
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
