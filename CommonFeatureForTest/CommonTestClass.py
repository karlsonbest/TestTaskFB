from Resources import config
from selenium import webdriver
from time import sleep as sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.support.ui as ui
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

browser = None
DEFAULT_WAITING_FOR_ELEMENT = config.DEFAULT_WAITING_FOR_ELEMENT


def get_browser( browser_name="chrome"):
    print ("   START [CommonTestClass.get_browser] param value is: [" + browser_name + "]" )

    if (browser_name=="chrome"):
        options = webdriver.ChromeOptions()
        # options.add_argument("--lang=en_US.UTF-8")
        options.add_argument('--allow-silent-push')
        options.add_argument('--disable-notifications')

        browser = webdriver.Chrome(executable_path = config.DRIVER_PATH.get( browser_name ), chrome_options=options)

    elif (browser_name=='ie'):
        browser = webdriver.Ie(config.DRIVER_PATH.get( browser_name ))

    elif (browser_name=='firefox'):
        binary = FirefoxBinary(config.DRIVER_PATH.get( browser_name ))
        fp = webdriver.FirefoxProfile()
        browser = webdriver.Firefox(firefox_binary=binary, firefox_profile=fp)
    else:
        browser = webdriver.Chrome(config.DRIVER_PATH.get( browser_name ))

    print ("   FINISH [CommonTestClass.get_browser] param value is: " + browser_name + "]" )
    return browser


def close_browser(browser):
    print ("   START [CommonTestClass.close_browser]" )
    sleep(5)
    browser.close()
    print ("   FINISH [CommonTestClass.close_browser]" )


def double_click_on_body (browser):
    body = browser.find_element_by_tag_name('body')
    actionChains = ActionChains(browser)
    double_click_on_body = actionChains.double_click(body)
    double_click_on_body.perform()

def open_page(browser, url="http://google.com.ua"):
    print ("   START [CommonTestClass.open_page] param value is: [" + url + "]" )
    browser.get(url)
    sleep(2)
    print ("   FINISH [CommonTestClass.open_page] param value is: [" + url + "]" )


def login_to_fb (browser):
    print ("   START [CommonTestClass.login_to_fb] " )
    open_page(browser,config.FB_LOCATORS.get('fb_for_url'))
    wait_title_condition(browser, "Facebook", DEFAULT_WAITING_FOR_ELEMENT)

    emailElem = wait_element_by_id(browser, config.FB_LOCATORS.get('user_id'), DEFAULT_WAITING_FOR_ELEMENT)
    emailElem.send_keys(config.FB_CREDENTIALS.get('user'))

    passlElem = wait_element_by_id(browser, config.FB_LOCATORS.get('pass_id'), DEFAULT_WAITING_FOR_ELEMENT)
    passlElem.send_keys( config.FB_CREDENTIALS.get('password'))

    buttonElem = wait_element_by_xpath (browser,config.FB_LOCATORS.get('login_button_xpath'))
    buttonElem.click()

    sleep(2)
    double_click_on_body (browser)
    wait_element_by_xpath (browser, config.FB_LOCATORS.get('logout_xpath1'),DEFAULT_WAITING_FOR_ELEMENT )
    print ("   FINISH [CommonTestClass.login_to_fb] " )


def logout_from_fb (browser):
    print ("   START [CommonTestClass.logout_from_fb] " )
    sleep(5)
    logoutElem = wait_element_by_xpath (browser, config.FB_LOCATORS.get('logout_xpath1'),DEFAULT_WAITING_FOR_ELEMENT )
    logoutElem.click()
    logoutElem = wait_element_by_xpath (browser, config.FB_LOCATORS.get('logout_xpath2'),DEFAULT_WAITING_FOR_ELEMENT )
    logoutElem.click()

    print ("   FINISH [CommonTestClass.logout_from_fb] " )


def wait_title_condition (browser, text, wait_in_sec = DEFAULT_WAITING_FOR_ELEMENT):
    print ("   START [CommonTestClass.wait_title_condition] ")
    try:
        element = WebDriverWait(browser, wait_in_sec).until(
            EC.title_contains (text))
    except NoSuchElementException:
        print ("     [NoSuchElementException] Nothing was found in the title for [" + text + "] during(sec) " + str(wait_in_sec) )
        assert False, 'Title is not: ' + 'text'
    except TimeoutException:
        print ("     [TimeoutException] Element is not appear ")
        assert False, "Page is not opened during(sec)" + str(wait_in_sec)
    print ("   FINISH [CommonTestClass.wait_title_condition] " )


def wait_element_by_id (browser, id, wait_in_sec = DEFAULT_WAITING_FOR_ELEMENT):
    print ("   START [CommonTestClass.wait_element_by_id] id: [" + id +"] wait_in_sec: [" + str(wait_in_sec) +"]")
    element = None
    try:
        element = ui.WebDriverWait(browser, wait_in_sec).until(EC.visibility_of_element_located((By.ID, id)))
    except NoSuchElementException:
        print ("     [NoSuchElementException] Element is not present after (sec) " + str (wait_in_sec))
        assert False, 'No such element: ' + id
    except TimeoutException:
        if id == 'medley_header_movies':
            None
        else:
            print ("     [TimeoutException] Element is not appear ")
            assert False,'element is not appeared during(sec) ' + str (wait_in_sec)
    print ("   FINISH [CommonTestClass.wait_element_by_id] " )
    return element


def wait_element_by_xpath(browser, xpath, wait_in_sec = DEFAULT_WAITING_FOR_ELEMENT):
    print ("   START [CommonTestClass.wait_element_by_xpath] xpath: [" + xpath +"] wait_in_sec: [" + str(wait_in_sec) +"]")
    element = None
    try:
        element = ui.WebDriverWait(browser, wait_in_sec).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    except NoSuchElementException:
        print ("     [NoSuchElementException] Element is not present after (sec) " + str (wait_in_sec))
        assert False,  'No such element: ' + xpath
    except TimeoutException:
        print ("     [TimeoutException]")
        assert False,  'element is not appeared during(sec) ' + str (wait_in_sec)
    print ("   FINISH [CommonTestClass.wait_element_by_xpath] " )
    return element


def scroll (browser):
    SCROLL_PAUSE_TIME = 0.5
    print ("   START [CommonTestClass.scroll] SCROLL_PAUSE_TIME: " + str (SCROLL_PAUSE_TIME) )

    while True:
        print ("    scroll value: " + str (browser.execute_script("return document.body.scrollHeight")))
        passlElem = wait_element_by_id(browser, config.FB_LOCATORS.get('friend_link_id'), DEFAULT_WAITING_FOR_ELEMENT)
        if (passlElem == None):
            # Scroll down to bottom
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Wait to load page
            sleep(SCROLL_PAUSE_TIME)
        else:
            break
    print ("   FINISH [CommonTestClass.scroll]" )


def get_amount_of_friends (browser):
    print ("   START [CommonTestClass.get_amount_of_friends]" )
    elems = browser.find_elements_by_xpath(config.FB_LOCATORS.get('friends_xpath'))
    count = len(elems)
    print (" !!!!!!!!!!!!!!!!!!!! --->>>>>>>>>" + str(count))
    print ("   FINISH [CommonTestClass.get_amount_of_friends] count of friend is " + str(count))
    return count


def get_list_of_friends (browser):
    print ("   START [CommonTestClass.get_list_of_friends]")
    A = []
    elems = browser.find_elements_by_xpath(config.FB_LOCATORS.get('friends_xpath'))
    for elem in elems:
        A.append([elem.get_attribute('text'), elem.get_attribute('href')])

    print ("   FINISH [CommonTestClass.get_list_of_friends]")
    return A


def get_count_of_friend_using_fb_for_link (browser, url_for):
    print ("   START [CommonTestClass.get_count_of_friend_using_fb_for_link] url is " + url_for)
    login_to_fb (browser)
    open_page(browser, url_for)
    cnt_using_fb = wait_element_by_xpath (browser, config.FB_LOCATORS.get('fb_friend_count_path'),DEFAULT_WAITING_FOR_ELEMENT )
    cnt_using_fb = cnt_using_fb.text
    print (" !!!!!!!!!!!!!! --->>>>>>>>> FB COUNT IS " + str(cnt_using_fb))
    print ("   FINISH [CommonTestClass.get_count_of_friend_using_fb_for_link]")

    return cnt_using_fb


def get_count_of_friend_for_link (browser, url_for):
    print ("   START [CommonTestClass.get_count_of_friend_for_link] url is " + url_for)
    login_to_fb (browser)
    open_page(browser, url_for)
    double_click_on_body (browser)
    scroll(browser)
    cnt = get_amount_of_friends (browser)
    logout_from_fb (browser)
    print ("   FINISH [CommonTestClass.get_count_of_friend_for_link]")

    return cnt


if __name__ == "__main__":
    print (" Common Test Class ")