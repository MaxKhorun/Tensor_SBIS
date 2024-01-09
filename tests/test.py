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

        page.rabotaem_block.scroll_to_element()

        try:
            assert page.rabotaem_block.get_text() == 'Работаем'
        except AssertionError as error:
            logger.error('AssertionError', exc_info=True)

        w = list(map(int, page.all_pictures.get_attribute('width')))
        h = list(map(int, page.all_pictures.get_attribute('height')))

        try:
            assert len(set(w)) == 1 and len(set(h)) == 1
        except AssertionError as error:
            logger.error('AssertionError', exc_info=True)


def test_second_script(web_driver, logger):
    page = MainTensorPage(web_driver)

    page.contacts_btn.click()

    try:
        assert page.location_city.get_text() == 'г. Санкт-Петербург'
    except AssertionError as error:
        logger.error('AssertionError', exc_info=True)

    local_partners_list = page.partners_list.get_text()

    assert len(local_partners_list) > 0

    page.location_city.click()
    page.kamchatka.wait_to_be_clickable()
    page.kamchatka.click()
    page.wait_page_loaded()

    assert page.location_city.get_text() == 'Камчатский край' and \
        page.partners_list.get_text() != local_partners_list
    assert '41-kamchatskij-kraj' in page.get_current_url()
    # assert 'Камчатский край' in page.get_page_source().find('title')


def test_third_script(web_driver):
    page = MainTensorPage(web_driver)

    page.download_sbis.scroll_to_element()
    page.download_sbis.click()
    page.wait_page_loaded()
    page.plugin_sbis.click()
    # page.plugin_sbis.click()
    # page.downl_link.click()
    # sleep(2)
    # page.screenshot('plugin.png')
    sleep(2)
