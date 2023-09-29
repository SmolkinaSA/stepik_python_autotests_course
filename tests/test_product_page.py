import pytest
import time
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage

#Примет с параметризацией
#@pytest.mark.parametrize('promo_offer', ["0","1", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
#def test_guest_can_add_product_to_basket(browser, promo_offer):
#    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
#    page = ProductPage(browser, link)
#    page.open()
#    product_page = ProductPage(browser, browser.current_url)
#    product_page.add_item_to_bascket()
#    product_page.solve_quiz_and_get_code()
#    product_page.check_add_item_to_basket()
@pytest.mark.xfail(reason="fixing this bug right now")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        product_page = ProductPage(browser, browser.current_url)
        product_page.add_item_to_bascket()
        product_page.should_not_be_success_message()
        
@pytest.mark.xfail(reason="fixing this bug right now")
def test_message_disappeared_after_adding_product_to_basket(browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        product_page = ProductPage(browser, browser.current_url)
        product_page.add_item_to_bascket()
        product_page.should_is_disappeared_message()

def test_guest_should_see_login_link_on_product_page(browser):
    #Тест: гость видит ссылку login_link на странице продукта
        link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    """Тест: гость может перейти на страницу логина со страницы продукта"""
    link = 'http://selenium1py.pythonanywhere.com/catalogue/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """Тест: при переходе со страницы продукта корзина пуста и есть сообщение об этом"""
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/reversing_202/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()

@pytest.mark.autorizated_user
class TestUserAddToBasketFromProductPage(object):
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        """
        setup-функция, подготавливает данные и выполняется перед запуском каждого теста из класса
        Открывает форму регистрации, регистрирует нового пользователя
        Проверяет, что пользователь залогинен
        """
        link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + '@fakemail.org'
        password = str(time.time())
        page.register_new_user(email=email, password=password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        """Тест нет success_message"""
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        product_page = ProductPage(browser, browser.current_url)
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        # link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
        page = ProductPage(browser, link)
        page.open()
        product_page = ProductPage(browser, browser.current_url)
        product_page.add_item_to_bascket()
        product_page.solve_quiz_and_get_code()
        product_page.check_add_item_to_basket()
