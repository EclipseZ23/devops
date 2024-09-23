from tests.web.pages.page_base import PageBase
from tests.web.helpers.element import Element
from munch import munchify


class LogoutPage(PageBase):
    def __init__(self, driver):
        PageBase.__init__(self, driver = driver)

        self.elements = {
            'logout': Element('//button[@id="logout-button"]', self),
        }