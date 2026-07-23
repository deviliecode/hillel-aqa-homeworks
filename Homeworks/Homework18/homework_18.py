from pathlib import Path
from datetime import datetime
import logging

file_path = Path("Homeworks/Homework18/hblog.txt")
log_path = Path("Homeworks/Homework18/hb_test.log")

logging.basicConfig(
    filename=log_path,
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

def get_needed_times():
    """Строки лише з вказаним ключем TSTFEED0300|7E3E|0400"""
    list_of_rows = []

    with file_path.open("r", encoding="utf-8") as f:
        for line in f:
            split_row = line.split()
            if "TSTFEED0300|7E3E|0400" in split_row:
                first = split_row.index("Timestamp")
                row = f"{split_row[first + 1]}"
                list_of_rows.append(row)

    return list_of_rows


def create_heartbeat_log():
    """Додає логи"""
    times = get_needed_times()

    timestamps = []

    for i in times:
        parsed_time_to_datatime = datetime.strptime(i, "%H:%M:%S")
        timestamps.append(parsed_time_to_datatime)

    timestamps.sort()

    for i in range(1, len(timestamps)):
        prev_time = timestamps[i - 1]
        curr_time = timestamps[i]
        heartbeat = (curr_time - prev_time).total_seconds()

        curr_time_str = curr_time.strftime("%H:%M:%S")

        if 31 < heartbeat < 33:
            logger.warning(f"Heartbeat {heartbeat} sec at {curr_time_str}")
        elif heartbeat >= 33:
            logger.error(f"Heartbeat {heartbeat} sec at {curr_time_str}")

create_heartbeat_log()