from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    # link = "http://suninjuly.github.io/registration1.html"
    link = "http://suninjuly.github.io/registration2.html"  
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    # input1_first_element = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
    input1_first_element = browser.find_element(By.CSS_SELECTOR, ".first[required]")
    input1_first_element.send_keys("Иван")
    # input2_second_element = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
    input2_second_element = browser.find_element(By.CSS_SELECTOR, '.second[required]')
    input2_second_element.send_keys("Петров")
    # input3_third_element = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
    input3_third_element = browser.find_element(By.CSS_SELECTOR, '.third[required]')
    input3_third_element.send_keys("petrov@mail.ru")
   
    # Отправляем заполненную форму
    button_element = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button_element.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    