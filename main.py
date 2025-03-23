from flask import Flask, request
import csv
import os
from datetime import datetime

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def receive_webhook():
    data = request.form.to_dict()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"form_{timestamp}.csv"

    # Убедимся, что папка существует
    os.makedirs("data", exist_ok=True)
    filepath = os.path.join("data", filename)

    # Сохраняем в CSV
    with open(filepath, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(data.keys())
        writer.writerow(data.values())

    return {"status": "ok", "saved": filename}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
