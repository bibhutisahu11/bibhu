from selenium import webdriver
import time
from downloadfile import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver =webdriver.Chrome("C:\\Users\\sahubi2\\PycharmProjects\\TabTest\\driver\\chromedriver.exe")

driver.get("https://tableau.mars")
driver.maximize_window()
driver.find_element_by_name("loginfmt").send_keys("mansi.tanwani@effem.com")
driver.find_element_by_id("idSIButton9").click()
time.sleep(5)

driver.find_element_by_id("passwordInput").send_keys("craftsyFingers@4")
driver.find_element_by_class_name("submit").click()
driver.find_element_by_xpath("//input[@type='submit' and @value='Yes']").click()
time.sleep(5)
driver.find_element_by_xpath("//a[@href='/#/projects/84']").click()
time.sleep(5)
driver.find_element_by_xpath("//a[@href='/#/workbooks/576']").click()
time.sleep(5)
driver.find_element_by_xpath("//a[@href='/#/views/PromotionReporting/WebEditView']").click()
driver.switch_to.frame(0)
#driver.find_element_by_xpath("//span[@class='tabToolbarButtonImg tab-icon-download']").click()
#link = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "(//span[contains(text(),'Download')])[1]")))
#driver.find_element_by_xpath("//div[@class='tabToolbarButton tab-widget download tab-showFocusIndicator']").click()
find_and_click("download")
find_and_click("crosstab")
find_and_click("download_crosstab")


