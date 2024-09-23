import pytest
import random
import string
from tests.web.test_base import WebBase
from tests.web.pages.login_page import LoginPage
from tests.web.pages.login_page import RegisterPage
from tests.web.pages.Calculations_page import CalculationsPage
from assertpy import assert_that
from time import sleep

class TestWeb(WebBase):

    def test_login(self):
        LoginPage(self.driver).elements.username.set('admin')
        LoginPage(self.driver).elements.password.set('test1234')
        LoginPage(self.driver).elements.login.click()
        sleep(3)
        assert_that(LoginPage(self.driver).elements.username_logged_in.text).is_equal_to('admin')


class TestRegister(WebBase):
    
    def test_Register(self):
        
        random_name = ''.join(random.choices(string.ascii_letters,k=5))

        RegisterPage(self.driver).elements.register.click()
        RegisterPage(self.driver).elements.username.set(random_name)
        RegisterPage(self.driver).elements.password1.set('password')
        RegisterPage(self.driver).elements.password2.set('password')
        RegisterPage(self.driver).elements.register.click()
        
        sleep(3)
        
        assert_that(RegisterPage(self.driver).elements.username_logged_in.text).is_equal_to(random_name)

class TestCalculations(WebBase):
    def login(self):
        LoginPage(self.driver).elements.username.set('admin')
        LoginPage(self.driver).elements.password.set('test1234')
        LoginPage(self.driver).elements.login.click()

    def test_add(self):
        self.login()
        CalculationsPage(self.driver).elements.key5.click()
        CalculationsPage(self.driver).elements.add.click()
        CalculationsPage(self.driver).elements.key2.click()
        CalculationsPage(self.driver).elements.equals.click()
        assert_that(CalculationsPage(self.driver).elements.screen.value).is_equal_to('7')

    def test_subtract(self):
        self.login()
        CalculationsPage(self.driver).elements.key8.click()
        CalculationsPage(self.driver).elements.subtract.click()
        CalculationsPage(self.driver).elements.key6.click()
        CalculationsPage(self.driver).elements.equals.click()
        assert_that(CalculationsPage(self.driver).elements.screen.value).is_equal_to('2')

    def test_multiply(self):
        self.login()
        CalculationsPage(self.driver).elements.key5.click()
        CalculationsPage(self.driver).elements.multiply.click()
        CalculationsPage(self.driver).elements.key8.click()
        CalculationsPage(self.driver).elements.equals.click()
        assert_that(CalculationsPage(self.driver).elements.screen.value).is_equal_to('40')

    def test_divide(self):
        self.login()
        CalculationsPage(self.driver).elements.key8.click()
        CalculationsPage(self.driver).elements.divide.click()
        CalculationsPage(self.driver).elements.key2.click()
        CalculationsPage(self.driver).elements.equals.click()
        assert_that(CalculationsPage(self.driver).elements.screen.value).is_equal_to('4')

    def test_history(self):
        self.test_multiply()
        CalculationsPage(self.driver).elements.history.click()
        assert_that(CalculationsPage(self.driver).elements.historyarea.value).is_equal_to('5*8=40\n')

