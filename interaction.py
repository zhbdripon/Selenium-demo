from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Interaction():

    def __init__(self,browser):
        self.browser = browser

    def insert_email(self,email):
        email_text_box = self.browser.find_element_by_tag_name("input")
        email_text_box.send_keys(email)

    def click_email_next_button(self):
        next_button = self.browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[3]/div/div[2]/div/button")
        next_button.click()

    def insert_password(self,password):
        password_text_box = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div[2]/form/div/div/div[1]/div/input")))
        password_text_box.send_keys(password)

    def click_login(self):
        login_button = self.browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/form/div/div/div[2]/div/button")
        login_button.click()

    def expand_setting_dropdown(self):
        setting_dropdown = WebDriverWait(self.browser,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/nav/div/div[2]/ul/li[1]")))
        setting_dropdown.click()

    def select_tanant_setting(self):
        tanant_settings_button = WebDriverWait(self.browser,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/nav/div/div[2]/ul/li[1]/ul/li")))
        tanant_settings_button.click()

    def click_config_user_button(self):
        manage_user_config_button = WebDriverWait(self.browser,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div[10]/div/div[3]")))
        manage_user_config_button.click()

    def wait_for_user_table_page(self):
        WebDriverWait(self.browser,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[4]/div/div[2]/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div[2]/span")))

    def serach_user(self,text):
        search_bar_toggle = WebDriverWait(self.browser,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[4]/div/div[2]/div/div/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div/span[2]/div")))
        search_bar_toggle.click()
        search_bar = WebDriverWait(self.browser,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[4]/div/div[2]/div/div/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div/span[1]/input")))
        search_bar.send_keys(text+Keys.ENTER)

    def busy_wait_for_table_update(self):
        time.sleep(2)
        while(self.browser.last_request.response is None):
            continue

    def get_user_table_row(self):
        return self.browser.find_elements_by_xpath("/html/body/div[4]/div/div[2]/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/table/tbody/tr")