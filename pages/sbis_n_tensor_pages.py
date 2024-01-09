from settings_n_data import sbis_URL

from pages.base import WebPage
from pages.elements import WebElement, ManyWebElements


class MainSbisPage(WebPage):
    '''Описание элементов на странице СБИС'''
    def __init__(self, webdriver, url=''):
        
        if not url:
            url = sbis_URL or 'https://sbis.ru/'
            
        super().__init__(webdriver, url)

    contacts_btn = WebElement(xpath='//*[@id="wasaby-content"]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[2]/a[1]')
    # для поиска кнопки "Контакты"
    tensor_bar = WebElement(xpath='//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a')
    # для поиска баннера "Тензор"
    location_city = WebElement(xpath='//*[@id="container"]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/span[1]/span[1]')
    # для поиска элемента с определением локации на странице
    partners_list = WebElement(xpath='//*[@id="contacts_list"]/div[1]/div[2]')
    # для получения списка партнёров с сайта
    kamchatka = WebElement(xpath='//*[@id="popup"]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[43]/span[1]')
    # для выбора Камчатки в поп-ап окне
    download_sbis = WebElement(link_text='Скачать СБИС')
    #
    plugin_sbis = WebElement(id='ws-jm379jpy481704827453351')

    #
    downl_link = WebElement(xpath='//*[@id="ws-xkfk13wxqwc1704645855413"]/div[1]/div[2]/div[2]/div[1]/a[1]')
    title = WebElement(tag_name='title')
    tarifi = WebElement(link_text='Тарифы')


class MainTensorPage(MainSbisPage):
    '''Описание элементов на странице Тензор.'''

    sila_v_ludyax = WebElement(xpath='//*[@id="container"]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/p[1]')
    # для поиска блока "Сила в людях"
    about_in_sila = WebElement(xpath='//*[@id="container"]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/p[4]/a[1]')
    # кнопка "Подробнее" в блоке "Сила в людях"
    rabotaem_block_to_find = WebElement(link_text='Присоединяйтесь к нашей команде!')
    # для поиска блока по фразе, уникально на странице
    rabotaem_block = WebElement(xpath='//*[@id="container"]/div[1]/div[1]/div[4]/div[1]/h2[1]')
    # для поиска блока "Работаем"
    all_pictures = ManyWebElements(class_name='tensor_ru-About__block3-image.new_lazy.loaded')
    # данные с картинками
