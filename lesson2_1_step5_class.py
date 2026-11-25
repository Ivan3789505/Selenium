from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html" 

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Считать значение для переменной x
    x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = x_element.text
    
    # Посчитать математическую функцию от x.
    y = calc(x)

    # Ввести ответ в текстовое поле.
    inp_element = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    inp_element.send_keys(y)

    # Отметить checkbox "I'm the robot".
    option1_element = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    option1_element.click()

    # Выбрать radiobutton "Robots rule!".
    option2_element = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    option2_element.click()




    # Нажать на кнопку Submit.
  
    button_element = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button_element.click()

    time.sleep(5)

finally:
    time.sleep(3)
    browser.quit()