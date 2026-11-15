from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



# Открыть страницу http://suninjuly.github.io/alert_accept.html
link = "http://suninjuly.github.io/alert_accept.html" 

try:
    browser = webdriver.Chrome()
    browser.get(link)

# Нажать на кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
   
# Принять confirm   
    confirm = browser.switch_to.alert
    confirm.accept()

# На новой странице решить капчу для роботов, чтобы получить число с ответом
    x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = x_element.text
    y = calc(x)


    # Ввести ответ в текстовое поле.
    inp = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    inp.send_keys(y)


    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

finally:
    time.sleep(3)
    browser.quit()
