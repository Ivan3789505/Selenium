from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# Открыть страницу https://SunInJuly.github.io/execute_script.html
link = "https://SunInJuly.github.io/execute_script.html" 

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
    # Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
    # Считать значение для переменной x
    x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = x_element.text
    y = calc(x)


# Проскроллить страницу вниз.

    inp = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", inp)
    inp.send_keys(y)


# Выбрать checkbox "I'm the robot".
    option1 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    option1.click()

# Переключить radiobutton "Robots rule!".
    option2 = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    option2.click()

# Нажать на кнопку "Submit".
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(10)

finally:
    time.sleep(3)
    browser.quit()


