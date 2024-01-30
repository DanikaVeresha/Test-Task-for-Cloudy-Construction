from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from configfile import username, user_password

#if:
# DataConfig:
# username = 'deshdesh288'
# user_password = 'desh288diesh'


def send_proton_email(email_to, email_subject):
    service = Service(exsecutive_path='/usr/local/bin/chromedriver')
    driver = webdriver.Chrome(service=service)
    try:
        driver.get('https://mail.protonmail.com/login')
        time.sleep(5)
        driver.find_element(by=By.ID, value='username').send_keys(username)
        time.sleep(5)
        driver.find_element(by=By.ID, value='password').send_keys(user_password)
        time.sleep(3)
        driver.find_element(by=By.XPATH,
                            value='/html/body/div[1]/div[4]/div[1]/main/div[1]/div[2]/'
                                  'form/button').send_keys(Keys.ENTER)
        time.sleep(30)
        print('You are logged in')
        driver.find_element(by=By.XPATH,
                            value='/html/body/div[1]/div[3]/div/div[2]/div/div[1]/div[2]/button').click()
        time.sleep(8)
        print('Send SMS')
        driver.find_element(by=By.XPATH,
                            value='/html/body/div[1]/div[4]/div/div/div/div/div/div[2]/div/div/div/div/'
                                  'div/div/input').send_keys(email_to)
        time.sleep(8)
        print('You are enter email')
        driver.find_element(by=By.XPATH,
                            value='/html/body/div[1]/div[4]/div/div/div/div/div/div[3]/div/div/'
                                  'input').send_keys(email_subject)
        time.sleep(10)
        print('You are enter subject')
        driver.find_element(by=By.XPATH,
                            value='html/body/div[1]/div[4]/div/div/div/div/section/div/div[1]/div[1]/div').click()
        time.sleep(8)
        print('You are enter text for next recipient')
        driver.find_element(by=By.XPATH,
                            value='/html/body/div[1]/div[4]/div/div/div/footer/div/div[1]/button[1]').click()
        time.sleep(25)
        print('Send SMS - Done')

        driver.find_element(by=By.XPATH,
                            value='/html/body/div[1]/div[3]/div/div/div/div[1]/div[4]/nav/div/ul/div[3]/li/a').click()
        time.sleep(25)
        print('Its all.Thank you so match!')

    except Exception as error:
        driver.quit()
        print('You must enter correct information!!!')
        status = (str(error), 'Error Origin: Proton Mail Script')
        print(status)


send_proton_email('deshdesh288@proton.me',
                  'Hello! Its me. Candidate for a vacancy! '
                  'I am so glad that you have an opening for this position.')

