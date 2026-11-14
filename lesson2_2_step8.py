from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 


# Открыть страницу http://suninjuly.github.io/file_input.html
link = "http://suninjuly.github.io/file_input.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)


# Заполнить текстовые поля: имя, фамилия, email
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("petrov@mail.ru")
       
# Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    element = browser.find_element(By.CSS_SELECTOR, "input[type='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))                   # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, "file.txt")                          # добавляем к этому пути имя файла 
    element.send_keys(file_path)

# Нажать кнопку "Submit"
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()


