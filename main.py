from seleniumwire import webdriver
import unittest
from interaction import Interaction


class TestRony(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path='./driver/chromedriver')
        self.browser.get("https://dhaka.mrbjarke.com/")
        self.interaction = Interaction(self.browser)

        self.interaction.insert_email("ehasanul.haque@wunderman.com")
        self.interaction.click_email_next_button()
        self.interaction.insert_password("P@ssw0rd1")
        self.interaction.click_login()
        self.interaction.expand_setting_dropdown()
        self.interaction.select_tanant_setting()
        self.interaction.click_config_user_button()
        self.interaction.wait_for_user_table_page()
        

    def test_search_rony(self):
        del self.browser.requests
        self.interaction.serach_user("rony")
        self.interaction.busy_wait_for_table_update()
        table_row = self.interaction.get_user_table_row()
        assert len(table_row) == 2

    def test_search_email(self):
        table_row = self.interaction.get_user_table_row()
        email_found = False
        for element in table_row:
            if(element.find_elements_by_tag_name("td")[1].text=="ehasanul.haque@adpeople.com"):
                email_found = True
        assert email_found

    def tearDown(self):
        self.browser.close()

if __name__ == '__main__':
    unittest.main()

