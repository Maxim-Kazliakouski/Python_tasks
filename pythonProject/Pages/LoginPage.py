from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class LoginPage(BasePage):

    username_field = (By.NAME, 'login_email')
    password_field = (By.NAME, 'login_password')
    sign_in_button = (By.XPATH, "//body/div[@id='outer-frame']/div[@id='page-content']/div[@id='login-or-register-page-content']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[2]/button[1]")
    account_menu = (By.XPATH)

    def login(self, username, password):
        self.send_keys(self.username_field, username)
        self.send_keys(self.password_field, password)
        self.click(self.sign_in_button)

        self.is_visible(self.account_menu)
