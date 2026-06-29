import logging
import xml.etree.ElementTree as ET

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def find_incoming_by_group_number(file_path, group_number):
    tree = ET.parse(file_path)
    root = tree.getroot()

    for group in root.findall("group"):
        number = group.find("number").text

        if number == str(group_number):
            timing = group.find("timingExbytes")

            if timing is None:
                logging.info(f"Група {group_number} не має блоку timingExbytes")
                return

            incoming = timing.find("incoming")

            if incoming is None:
                logging.info(f"Група {group_number} не має поля incoming")
                return

            logging.info(f"Група {group_number} — incoming: {incoming.text}")
            return

    logging.info(f"Групу з номером {group_number} не знайдено")


find_incoming_by_group_number("groups.xml", 0)
find_incoming_by_group_number("groups.xml", 2)
find_incoming_by_group_number("groups.xml", 4)
find_incoming_by_group_number("groups.xml", 1)
find_incoming_by_group_number("groups.xml", 99)