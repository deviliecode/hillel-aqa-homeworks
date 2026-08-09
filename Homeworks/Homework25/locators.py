#25 XPath
XPath_loc_1 = """//button[@class="btn btn-outline-white header_signin"]""" # За точним атрибутом
XPath_loc_2 = """//button[text()='Sign In']""" # За текстом
XPath_loc_3 = """//button[contains(text(), 'Sign I')]""" # За частковим текстом
XPath_loc_4 = """//button[contains(@class, 'header_signin')]""" # За частковим Атрибутом
XPath_loc_5 = """//button[starts-with(@class, 'btn btn-outline-')]""" # За початковим значенням атрибуту
XPath_loc_6 = """//a[@class='header_logo']""" # За точним класом (логотип)
XPath_loc_7 = """//a[contains(@class, 'header-link') and contains(@class, '-active')]""" # Декілька умов через AND
XPath_loc_8 = """//button[text()='Sign up']""" # За точним текстом (кнопка Sign up)
XPath_loc_9 = """//h2[contains(text(), 'Contact')]""" # За частковим текстом заголовка
XPath_loc_10 = """//button[@appscrollto='contactsSection']""" # За кастомним атрибутом appscrollto
XPath_loc_11 = """//div[@class='contacts_socials socials']/a[1]""" # Прямий (перший) дочірній елемент
XPath_loc_12 = """//div[@id='contactsSection']//a""" # Будь-який елемент-нащадок (усі посилання всередині блока)
XPath_loc_13 = """//h2[text()='Contacts']/following-sibling::div[1]""" # Наступний сусід (перший)
XPath_loc_14 = """//h1/following-sibling::p""" # Усі наступні сусіди по тегу p
XPath_loc_15 = """//img[contains(@src, 'info_1')]""" # Частковий атрибут src
XPath_loc_16 = """//a[starts-with(@href, 'https://www.linkedin')]""" # Початок значення атрибуту href
XPath_loc_17 = """(//p[@class='about-block_descr lead'])[1]""" # Перший елемент за позицією [1]
XPath_loc_18 = """(//a[@class='socials_link'])[last()]""" # Останній елемент за позицією last()
XPath_loc_19 = """(//footer//p)[2]""" # Другий елемент серед нащадків footer
XPath_loc_20 = """//span[contains(@class, 'icon-youtube')]/ancestor::a""" # Вісь ancestor (пошук "вгору" до предка)
XPath_loc_21 = """//span[@class='socials_icon icon icon-instagram']/parent::a""" # Вісь parent (безпосередній батько)
XPath_loc_22 = """//p[@class='about-block_descr lead'][1]/preceding-sibling::p""" # Вісь preceding-sibling (попередні сусіди)
XPath_loc_23 = """//button[@class='btn header-link' and @appscrollto='aboutSection']""" # Декілька атрибутів одночасно (AND)
XPath_loc_24 = """//a[@class='socials_link' and not(contains(@href, 'facebook'))][1]""" # Функція not() — виключення варіанту
XPath_loc_25 = """//a[normalize-space(text())='ithillel.ua']""" # За нормалізованим текстом (normalize-space)

#25 CSS
CSS_loc_1 = """.btn-outline-white""" # За класом
CSS_loc_2 = """.btn.btn-outline-white.header_signin""" # За декількома класами
CSS_loc_3 = """h1.hero-descriptor_title""" # Тег + клас
CSS_loc_4 = """#aboutSection""" # За ID
CSS_loc_5 = """#aboutSection img""" # ID + будь-який нащадок
CSS_loc_6 = """.about-block > .about-block_picture""" # Прямий дочірній елемент (>)
CSS_loc_7 = """.hero-descriptor_title + p""" # Наступний сусід (+)
CSS_loc_8 = """.hero-descriptor_title ~ .hero-descriptor_btn""" # Усі наступні сусіди (~)
CSS_loc_9 = """a[href$="ithillel.ua/"]""" # Атрибут закінчується на ($=)
CSS_loc_10 = """a[href^="mailto:"]""" # Атрибут починається з (^=)
CSS_loc_11 = """a[href*="linkedin"]""" # Атрибут містить (*=)
CSS_loc_12 = """a[class="contacts_link display-4"]""" # Точне значення атрибуту class
CSS_loc_13 = """.contacts_socials a:first-child""" # Псевдоклас :first-child
CSS_loc_14 = """.contacts_socials a:last-child""" # Псевдоклас :last-child
CSS_loc_15 = """.contacts_socials a:nth-child(3)""" # Псевдоклас :nth-child(n)
CSS_loc_16 = """.contacts_socials a:nth-of-type(2)""" # Псевдоклас :nth-of-type(n)
CSS_loc_17 = """footer p:first-of-type""" # Псевдоклас :first-of-type
CSS_loc_18 = """.about-block_descr:not(:first-of-type)""" # Псевдоклас :not()
CSS_loc_19 = """img[alt="Instructions"]""" # Точне значення атрибуту
CSS_loc_20 = """[appscrollto]""" # Наявність атрибуту (без значення)
CSS_loc_21 = """[appscrollto="aboutSection"]""" # Кастомний атрибут з точним значенням
CSS_loc_22 = """.header_right button.header-link.-guest""" # Нащадок + декілька класів
CSS_loc_23 = """.footer_item.-right a""" # Комбінація класів + нащадок
CSS_loc_24 = """h2, .about-block_title""" # Груповий селектор (,)
CSS_loc_25 = """.socials_link:nth-last-child(1)""" # Псевдоклас :nth-last-child(n)