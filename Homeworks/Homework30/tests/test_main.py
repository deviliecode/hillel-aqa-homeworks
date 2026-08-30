import allure
from playwright.sync_api import Page, expect
import os
import dotenv

dotenv.load_dotenv()

@allure.feature("Авторизація користувача")
def test_login(page: Page):
    with allure.step("Ввести валідні дані"):
        page.goto(os.getenv("URL_30"))
        page.get_by_role(role="button", name="Sign In").click()
        page.get_by_role(role="textbox", name="Email").fill(os.getenv("LOGIN_30"))
        page.get_by_role(role="textbox", name="Password").fill(os.getenv("PASSWORD_30"))
        page.get_by_role(role="button", name="Login").click()
    with allure.step("Перевірити успішний логін"):
        expect(page.locator("p", has_text="You have been successfully logged in")).to_be_visible()