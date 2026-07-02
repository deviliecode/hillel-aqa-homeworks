"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import logging

def log_event(username: str, status: str):
    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.

    status: Статус події входу:

    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити, логується на рівні warning
    * failed  - пароль невірний, логується на рівні error
    """
    log_message = f"Login event - Username: {username}, Status: [{status}]"

    # Створення та налаштування логера
    logging.basicConfig(
        filename='system.log',
        level=logging.INFO,
        format='%(asctime)s - %(message)s'
        )
    logger = logging.getLogger("log_event")

    # Логування події
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)



# ВИРІШЕННЯ
import unittest

def get_last_log_line():
    """Для отримання останнього рядка з логів"""
    with open('system.log', 'r') as f:
        lines = f.readlines()
        if lines:
            return lines[-1]
        else:
            raise ValueError("Log file is empty")

class TestLogEvent(unittest.TestCase):

    def test_success(self):
        log_event("Yaroslav", "success")
        last_line = get_last_log_line()
        self.assertIn("[success]", last_line)

    def test_expired(self):
        log_event("Yaroslav", "expired")
        last_line = get_last_log_line()
        self.assertIn("[expired]", last_line)

    def test_failed(self):
        log_event("Yaroslav", "failed")
        last_line = get_last_log_line()
        self.assertIn("[failed]", last_line)

if __name__ == "__main__":
    unittest.main()