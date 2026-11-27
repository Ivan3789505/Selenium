from selenium import webdriver
from selenium.webdriver.common.by import By
# Импортируем инструменты для явных ожиданий — это надёжнее, чем time.sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestInp(unittest.TestCase):
    # setUpClass выполняется один раз перед всеми тестами в классе.
    # Здесь мы инициализируем браузер и объект ожидания, чтобы не создавать их заново для каждого теста.
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome()
        # Создаём объект WebDriverWait с таймаутом 10 секунд — он будет ждать появления элементов до этого времени
        cls.wait = WebDriverWait(cls.browser, 10)

    # tearDownClass выполняется один раз после всех тестов в классе.
    # Гарантированно закрывает браузер, даже если какой-то тест упал с ошибкой.
    @classmethod
    def tearDownClass(cls):
        if cls.browser:
            cls.browser.quit()

    # Вспомогательный метод для заполнения формы.
    # Вынесен отдельно, чтобы избежать дублирования кода в разных тестах.
    def fill_form(self, first_name, last_name, email):
        # Находим поле «Имя» по CSS-селектору: элемент с классом first, у которого есть атрибут required
        input1 = self.browser.find_element(By.CSS_SELECTOR, ".first[required]")
        input1.send_keys(first_name)

        # Находим поле «Фамилия» аналогично — класс second и атрибут required
        input2 = self.browser.find_element(By.CSS_SELECTOR, ".second[required]")
        input2.send_keys(last_name)

        # Находим поле «Email» — класс third и атрибут required
        input3 = self.browser.find_element(By.CSS_SELECTOR, ".third[required]")
        input3.send_keys(email)

        # Находим кнопку отправки формы по классу btn
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

    # Вспомогательный метод для проверки сообщения об успехе.
    # Использует явное ожидание вместо жёсткой паузы time.sleep.
    def check_success_message(self):
        # Ждём до 10 секунд, пока на странице появится элемент <h1>.
        # Если элемент не появится за это время, тест упадёт с понятным сообщением об ошибке.
        welcome_text_elt = self.wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )
        welcome_text = welcome_text_elt.text
        expected_text = "Congratulations! You have successfully registered!"
        # Сравниваем фактический текст на странице с ожидаемым.
        self.assertEqual(expected_text, welcome_text, "Сообщение об успешной регистрации не совпадает")

    # Тест для первой страницы регистрации (упрощённая версия формы)
    def test_inp1(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.browser.get(link)
        # Заполняем форму тестовыми данными
        self.fill_form("Иван", "Петров", "petrov@mail.ru")
        # Проверяем, что появилось сообщение об успешной регистрации
        self.check_success_message()

    # Тест для второй страницы регистрации (форма с дополнительными полями)
    def test_inp2(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.browser.get(link)
        # Заполняем ту же самую форму теми же данными — логика проверки идентична
        self.fill_form("Иван", "Петров", "petrov@mail.ru")
        self.check_success_message()

if __name__ == "__main__":
    # Запускает все тесты из этого файла через стандартный механизм unittest
    unittest.main()