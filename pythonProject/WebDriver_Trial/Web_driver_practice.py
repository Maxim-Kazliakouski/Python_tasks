import time
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# установка Driver Manager для Chrome
browser = 'chrome'
driver = None
if browser == 'chrome':
    options = webdriver.ChromeOptions()
    # при помощи метода headless, браузер запускается в фоновом режиме
    options.headless = True
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
elif browser == 'firefox':
    options = webdriver.FirefoxOptions()
    options.headless = True
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
else:
    print('please provide a valid driver'.format(browser))

# после выполнения какого-либо действия драйвер ждёт 5 секунд появления интересующего нас элемента
driver.implicitly_wait(3)
# наш искомый URL, который будет отображаться при открытии браузера
driver.get('http://www.google.com')
# выводим tittle нашего искомого сайта
print(driver.title)
# находим эелемент по его имени. В нашем случае мы находим поле поиска Google, который имеет name = 'q'
search_field = driver.find_element(By.NAME, 'q')
# передаём в поле поиска 'selenium'
search_field.send_keys('selenium')

option_list = driver.find_elements(By.CSS_SELECTOR, 'ul.erkvQe li span')
print(len(option_list))
# отображается 20, потому что между строк есть пробелы, которые вопринимаются как эелементы
for element in option_list:
    print(element.text)

    if element.text == 'selenium hotel':
        element.click()
        break


time.sleep(3)
# выход из браузера
driver.quit()
