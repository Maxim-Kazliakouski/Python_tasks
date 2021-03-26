# импорт библиотек и параметров
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    # метод для поиска элемента на странице а затем кликает на него
    def click(self, by_locator):
        # поиск элемента для события, т.е. для ожидания в нашем случае 10 сек
        condition = EC.visibility_of_element_located(by_locator)
        # мы ожижаем Webdrier'ом в течение 10 сек появление нашего element
        element = WebDriverWait(self.driver, self.timeout).until(condition)
        element.click()

    # добавлеие значений на страницу
    def send_keys(self, by_locator, value):
        condition = EC.visibility_of_element_located(by_locator)
        # мы ожижаем Webdrier'ом в течение 10 сек появление нашего element
        element = WebDriverWait(self.driver, self.timeout).until(condition)
        element.send_keys(value)

    # поиск текста на странице у определенного элемента
    def get_element_text(self, by_locator, ):
        # посик элемента
        condition = EC.visibility_of_element_located(by_locator)
        element = WebDriverWait(self.driver, self.timeout).until(condition)

        return element.text

    # проверка эелемента на отображаемость
    def is_visible(self, by_locator):
        # посик элемента
        condition = EC.visibility_of_element_located(by_locator)
        element = WebDriverWait(self.driver, self.timeout).until(condition)
        return bool(element)


