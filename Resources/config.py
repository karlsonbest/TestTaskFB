import sys


# path for drivers
# C:\Program Files (x86)\Python36-32\selenium\webdriver\chrome
DRIVER_PATH = {
    # 'chrome'  : sys.path[5]+r'''\selenium\webdriver\chrome\chromedriver''',
    # ie' : sys.path[5]+r'''\selenium\webdriver\ie\IEDriverServer.exe'''
    'chrome': sys.path[0]+r'''\Resources\chromedriver''',
    'ie' : sys.path[0]+r'''\Resources\IEDriverServer.exe''',
    'firefox' : ''
}

# configuration for FB page login and pass
FB_CREDENTIALS = {
    'user': 'user@gmail.com',
    'password': 'pass',
    'url_for_friends': 'https://www.facebook.com/122210365949665/friends'
}

#Locators for FB element: login and logout
FB_LOCATORS = {
    'fb_for_url': "https://www.facebook.com",
    'user_id': 'email',
    'pass_id': 'pass',
    'login_button_xpath': '''//*[@id="loginbutton"]/input''',
    'logout_xpath1': '''//*[@id="logoutMenu"]''',
    'logout_xpath2': '''//li//div[.='Выйти' or .='Log Out']''',
    'friend_link_id': 'medley_header_movies',
    'friends_xpath': '''//*[@id="pagelet_timeline_medley_friends"]//ul[contains(@data-pnref, 'friends')]//li//div[contains(@data-testid, 'friend_list_item')]//div[contains(@class,'fsl fwb fcb')]//a''',
    'fb_friend_count_path': '''//*[@id="pagelet_timeline_medley_friends"]//a[contains(@name, 'Все друзья')]/span[2]'''
}

URL_FOR_FRIENDS = 'https://www.facebook.com/100010365949665/friends'
DEFAULT_WAITING_FOR_ELEMENT = 2
