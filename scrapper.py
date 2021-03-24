import time
import datetime
import smtplib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
while True:
	driver = webdriver.Safari()
	driver.get("https://www.walgreens.com/findcare/vaccination/covid-19")
	continue_link = driver.find_element_by_link_text('Schedule new appointment')
	continue_link.click()
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="wag-body-main-container"]/section/section/section/section/section[2]/div/span/button').click()
	time.sleep(3)
	try:
		if driver.find_element_by_xpath('//*[@id="wag-body-main-container"]/section/section/section/section/section[1]/section/div/a/span[2]/p').text == 'Appointments Available!':
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
			smtpObj.login('sender@outlook.com', "password") 
			smtpObj.sendmail('sender@outlook.com', 'reciever@outlook.com', body) # Or recipient@outlook

			smtpObj.quit()
	except Exception as e:
		print(str(datetime.datetime.now()))
	driver.quit()
	time.sleep(300)
