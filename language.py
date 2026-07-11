import json
from pathlib import Path

from settings import get_language

BASE_DIR = Path(__file__).resolve().parent
LOCALES = BASE_DIR / "locales"

_language = {}


def load_language():

    global _language

    language = get_language()

    file = LOCALES / f"{language}.json"

    if not file.exists():
        file = LOCALES / "en.json"

    with open(file, encoding="utf-8") as f:
        _language = json.load(f)


def t(key: str) -> str:

    return _language.get(key, f"[{key}]")