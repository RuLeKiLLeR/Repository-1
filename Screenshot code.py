from selenium import webdriver

driver = webdriver.Chrome(executable_path='/Users/X/Documents/chromedriver')

driver.get(input('Target_Url'))

driver.get_screenshot_as_file('Test.png')
driver.close()
