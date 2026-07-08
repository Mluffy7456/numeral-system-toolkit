import json
from pathlib import Path
from datetime import datetime

HISTORY_FILE = Path("history.json")


def load_history():

    if not HISTORY_FILE.exists():
        return []

    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except json.JSONDecodeError:
        return []


def save_history(history):

    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(
            history,
            file,
            ensure_ascii=False,
            indent=4
        )


def add_record(record_type, expression, result):

    history = load_history()

    history.append({
        "date": datetime.now().strftime("%d.%m.%Y"),
        "time": datetime.now().strftime("%H:%M:%S"),
        "type": record_type,
        "expression": expression,
        "result": result
    })

    save_history(history)


def show_history():

    history = load_history()

    if not history:

        print("\nHistory is empty.")
        return

    print("\n========== History ==========\n")

    for record in history:

        print(f"[{record['date']} {record['time']}]")
        print(f"Type: {record['type']}")
        print(f"Expression: {record['expression']}")
        print(f"Result: {record['result']}")
        print("-" * 50)


def clear_history():

    save_history([])

    print("\nHistory cleared successfully.")