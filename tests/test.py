from time import sleep
from pages.sbis_n_tensor_pages import MainTensorPage


def test_first_script(web_driver, logger):
    page = MainTensorPage(web_driver)

    page.contacts_btn.click()
    page.tensor_bar.wait_to_be_clickable()
    page.tensor_bar.click()
    page.switch_to_next_tab()
    page.sila_v_ludyax.scroll_to_element()
    page.about_in_sila.scroll_to_element()

    if 'Сила в людях' in page.sila_v_ludyax.get_text():

        page.about_in_sila.scroll_to_element()
        page.about_in_sila.click()
        assert page.get_current_url() == 'https://tensor.ru/about'
    else:
        logger.warning("Текст в блоке Сила в людях требует внимания")
        raise AssertionError

    page.rabotaem_block.scroll_to_element()

    try:
        assert page.rabotaem_block.get_text() == 'Работаем'
    except AssertionError as error:
        logger.error('Ошибка в тексте блока Работаем или проблема с блоком', exc_info=True)

    w = list(map(int, page.all_pictures.get_attribute('width')))
    h = list(map(int, page.all_pictures.get_attribute('height')))

    try:
        assert len(set(w)) == 1 and len(set(h)) == 1
    except AssertionError as error:
        logger.error('длина множества с длинами и ширинами картинок больше одного - что-то с размерами', exc_info=True)


def test_second_script(web_driver, logger):
    page = MainTensorPage(web_driver)

    page.contacts_btn.click()

    try:
        assert page.location_city.get_text() == 'г. Санкт-Петербург'
    except AssertionError as error:
        logger.error('Локация определена некорректно. См. скриншот.', exc_info=True)
        page.screenshot('location_error.png')

    local_partners_list = page.partners_list.get_text()

    try:
        assert len(local_partners_list) > 0
    except AssertionError as error:
        logger.error('Список партнёров пуст', exc_info=True)
        page.screenshot('artners_list.png')

    page.location_city.click()
    page.kamchatka.wait_to_be_clickable()
    page.kamchatka.click()
    page.wait_page_loaded()

    try:
        assert page.location_city.get_text() == 'Камчатский край' and \
               page.partners_list.get_text() != local_partners_list
    except AssertionError as error:
        logger.error('Локация и список партнёров не прошли проверку', exc_info=True)
        page.screenshot('location_n_partners.png')

    try:
        assert ('41-kamchatskij-kraj' in page.get_current_url()) and \
               ('Камчатский край' in page.get_page_source().title())
    except AssertionError as error:
        logger.error('URL & title nave not passed', exc_info=True)
        page.screenshot('url_n_title.png')


def test_third_script(web_driver):
    page = MainTensorPage(web_driver)

    pass
