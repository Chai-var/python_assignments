import self as self
from selenium import webdriver


class Autolog:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get("http://www.practiceselenium.com/welcome.html")
        welcome = self.driver.find_element_by_xpath('//*[@id="wsb-nav-00000000-0000-0000-0000-000450914915"]/ul/li[1]/a')
        welcome.click()
        our_passion = self.driver.find_element_by_xpath('//*[@id="wsb-nav-00000000-0000-0000-0000-000450914915"]/ul/li[2]/a')
        our_passion.click()
        menu = self.driver.find_element_by_xpath('//*[@id="wsb-nav-00000000-0000-0000-0000-000450914915"]/ul/li[3]/a')
        menu.click()
        lets_talk_tea = self.driver.find_element_by_xpath('//*[@id="wsb-nav-00000000-0000-0000-0000-000450914915"]/ul/li[4]/a')
        lets_talk_tea.click()
        check_out = self.driver.find_element_by_xpath('//*[@id="wsb-nav-00000000-0000-0000-0000-000450914915"]/ul/li[5]/a')
        check_out.click()


bot = Autolog()
bot.login()
