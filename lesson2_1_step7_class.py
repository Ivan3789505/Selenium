from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# Открыть страницу http://suninjuly.github.io/get_attribute.html
link = "http://suninjuly.github.io/get_attribute.html" 

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
    # Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
    # Считать значение для переменной x
    x_element = browser.find_element(By.CSS_SELECTOR, "[id='treasure']")
    x = x_element.get_attribute("valuex")
    y = calc(x)


    # Ввести ответ в текстовое поле.
    input_element = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    input_element.send_keys(y)

    # Отметить checkbox "I'm the robot".
    option1_element = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    option1_element.click()

    # Выбрать radiobutton "Robots rule!".
    option2_element = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    option2_element.click()

    # Нажать на кнопку Submit.
    button_element = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button_element.click()

    time.sleep(10)

finally:
    time.sleep(3)
    browser.quit()