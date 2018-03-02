import unittest
from Resources import config
from CommonFeatureForTest import CommonTestClass as CommonTestClass


class Test(unittest.TestCase):

    DEFAULT_BROWSER = 'chrome'

    def setUp(self, browser_name = DEFAULT_BROWSER):
        print (" START [testFBFriens.setUp] ")
        self.browser = CommonTestClass.get_browser(browser_name)

    def tearDown(self):
        print (" START [testFBFriens.tearDown] ")
        CommonTestClass.close_browser(self.browser)

    def testCheckAmountOfFriends(self):
        print (" Test testCheckAmountOfFriends ")

        assert (CommonTestClass.get_count_of_friend_for_link(self.browser, config.URL_FOR_FRIENDS)
                == int(CommonTestClass.get_count_of_friend_using_fb_for_link (self.browser, config.URL_FOR_FRIENDS)))

    # def test_second (self):
    #     print (" Test testsecond ")