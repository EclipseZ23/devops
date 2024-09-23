from tests.web.pages.page_base import PageBase
from tests.web.helpers.element import Element
from munch import munchify



class CalculationsPage(PageBase):
    def __init__(self, driver):
        PageBase.__init__(self, driver = driver)
        self.page_elements = {
            'key1': Element('//button[@id="key-1"]', self),
            'key2': Element('//button[@id="key-2"]', self),
            'key3': Element('//button[@id="key-3"]', self),
            'key4': Element('//button[@id="key-4"]', self),
            'key5': Element('//button[@id="key-5"]', self),
            'key6': Element('//button[@id="key-6"]', self),
            'key7': Element('//button[@id="key-7"]', self),
            'key8': Element('//button[@id="key-8"]', self),
            'key9': Element('//button[@id="key-9"]', self),
            'key0': Element('//button[@id="key-0"]', self),
            'decimal': Element('//button[@id="key-decimal"]', self),
            'add': Element('//button[@id="key-add"]', self),
            'subtract': Element('//button[@id="key-subtract"]', self),
            'multiply': Element('//button[@id="key-multiply"]', self),
            'divide': Element('//button[@id="key-divide"]', self),
            'equals': Element('//button[@id="key-equals"]', self),
            'clear': Element('//button[@id="key-clear"]', self),
            'screen': Element('//input[@id="calculator-screen"]', self),
            'history': Element('//button[@id="toggle-button"]', self),
            'historyarea': Element('//textarea[@id="history"]', self),
        }

        self.elements = munchify(self.page_elements)