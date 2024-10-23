from selenium.webdriver.common.by import By
import time
import pytest

link = ' http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


class TestProductPage:
    
    def test_button_add_to_basket_is_visible(self, browser):
        # Открываем страницу товара
        browser.get(link)
        
        # Установлено время принудительной задержки браузера
        # после открытия страницы, для визуальной проверки языка открытой страницы
        time.sleep(10)
        
        # Проверяем наличие кнопки добавления товара в корзину
        assert browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")