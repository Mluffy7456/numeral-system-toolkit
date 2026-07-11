import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SETTINGS = BASE_DIR / "settings.json"

DEFAULT = {
    "language": "en"
}


def load_settings():

    if not SETTINGS.exists():
        save_settings(DEFAULT)

    with open(
        SETTINGS,
        encoding="utf-8"
    ) as f:

        return json.load(f)


def save_settings(settings):

    with open(
        SETTINGS,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            settings,
            f,
            indent=4,
            ensure_ascii=False
        )


def get_language():

    return load_settings().get(
        "language",
        "en"
    )


def set_language(language):

    if language not in ("en", "ru"):
        language = "en"

    settings = load_settings()

    settings["language"] = language

    save_settings(settings)