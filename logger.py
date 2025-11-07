# python
# logger.py
import json
from datetime import datetime

LOG_PATH = "game_events.jsonl"

def log_event(event_type, data=None):
    event = {
        "type": event_type,
        "ts": datetime.utcnow().isoformat() + "Z",
    }
    if data is not None:
        event["data"] = data
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(event) + "\n")