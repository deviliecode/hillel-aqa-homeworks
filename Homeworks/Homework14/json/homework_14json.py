import json
import logging
from pathlib import Path

log_file = Path(__file__).parent.parent.parent.parent / "system.log"

logging.basicConfig(
    filename=log_file,
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

folder = Path(".")

for i in folder.glob("*.json"):

    content = i.read_text(encoding="utf-8")

    try:
        json.loads(content)

    except json.JSONDecodeError as e:
        logging.error(f"Файл '{i.name}' не є валідним JSON. Причина: {e}")
