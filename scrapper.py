import time
import smtplib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
while True:
	driver = webdriver.Safari()
	driver.get("https://www.walgreens.com/findcare/vaccination/covid-19")
	continue_link = driver.find_element_by_link_text('Schedule new appointment')
	continue_link.click()
	time.sleep(7)
	driver.find_element_by_xpath('//*[@id="wag-body-main-container"]/section/section/section/section/section[2]/div/span/button').click()
	time.sleep(2)
	if driver.find_element_by_xpath('//*[@id="wag-body-main-container"]/section/section/section/section/div/a/span[2]/p').text == 'Appointments Available!':
		print('Yay!')
		body = 'Vaccine Available'
		try:
		    smtpObj = smtplib.SMTP('smtp.outlook.com', 587)
		except Exception as e:
		    print(e)
		    smtpObj = smtplib.SMTP_SSL('smtp-mail.outlook.com', 465)
		#type(smtpObj) 
		smtpObj.ehlo()
		smtpObj.starttls()
		smtpObj.login('jwfunkbot@outlook.com', "goddEr-fikbic-percu4") 
		smtpObj.sendmail('jwfunkbot@outlook.com', 'jwfunk@outlook.com', body) # Or recipient@outlook

		smtpObj.quit()
	driver.quit()
	time.sleep(60)
