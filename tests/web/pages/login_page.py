from tests.web.pages.page_base import PageBase
from tests.web.helpers.element import Element
from munch import munchify


class LoginPage(PageBase):
    def __init__(self, driver):
        PageBase.__init__(self, driver = driver)

        self.page_elements = {
            'username': Element('//input[@id="username"]', self),
            'password': Element('//input[@id="password"]', self),
            'login': Element('//button[@id="login"]', self),
            'username_logged_in': Element('//label[@id="user-name"]', self),
        }

        self.elements = munchify(self.page_elements)

    
class RegisterPage(PageBase):

    def __init__(self, driver):
        PageBase.__init__(self, driver = driver)

        self.page_elements = {
            'username': Element('//input[@id="username"]', self),
            'password1': Element('//input[@id="password1"]', self),
            'password2': Element('//input[@id="password2"]', self),
            'register': Element('//button[@id="register"]', self),
            'username_logged_in': Element('//label[@id="user-name"]', self),
            'username_registered': Element('//div[@id="errormsg"]', self),
        }
        
        
        self.elements = munchify(self.page_elements)
