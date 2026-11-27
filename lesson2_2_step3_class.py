from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


# Открыть страницу https://suninjuly.github.io/selects1.html
link = "https://suninjuly.github.io/selects2.html" 

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Посчитать сумму заданных чисел
    x_element = browser.find_element(By.CSS_SELECTOR, "[id='num1']")
    y_element = browser.find_element(By.CSS_SELECTOR, "[id='num2']")
    sum = int(x_element.text) + int(y_element.text)
    
    print(sum)

    # Выбрать в выпадающем списке значение равное расчитанной сумме
    browser.find_element(By.CSS_SELECTOR, "[id='dropdown']").click()
    browser.find_element(By.CSS_SELECTOR,  f"[value='{sum}']").click()

        # Нажать на кнопку Submit.
    button_element = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button_element.click()

    time.sleep(10)

finally:
    time.sleep(3)
    browser.quit()