import os
from selenium import webdriver
from selenium.webdriver.common.by import By
#time.sleep(60)
from webdriver_manager.chrome import ChromeDriverManager

from env import *
from datetime import datetime, time
from time import sleep

os.environ['PATH'] += r"C:\Users\renda\OneDrive\Documents\CsEandeavours\SeleniumDrivers"
# driver = webdriver.Chrome()


def wait_start2(runTime):
    startTime = time(*(map(int, runTime.split(':'))))
    while startTime > datetime.today().time(): # you can add here any additional variable to break loop if necessary
        sleep(1)# you can change 1 sec interval to any other


wait_start2('08:00')

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://vula.uct.ac.za/portal")

#login
UCTLogin = driver.find_element_by_id('loginLink1')
UCTLogin.click()
Username = driver.find_element_by_id('userNameInput')
Username.send_keys(email)
Password = driver.find_element_by_id('passwordInput')
Password.send_keys(password)
Submit = driver.find_element_by_id('submitButton')
Submit.click()

#navigate and book
site = driver.find_element_by_xpath("//a[@title='Woolsack Laundry Bookings']")
site.click()
book = driver.find_element_by_xpath("//a[@title='Laundry Sign-up - For enabling online registration for meetings and other events']")
book.click()
expand = driver.find_element_by_id('items:showallrecurmeeting')
expand.click()


# time slots counted from 0
def book(slot):
    court = driver.find_element_by_id('items:meetinglist:10:cmdlink90')
    court.click()
    bookIt = driver.find_element_by_id('meeting:timeslots:'+str(slot)+':addMe')
    bookIt.click()
    finish = driver.find_element_by_id('meeting:save')
    finish.click()

def cancel(slot):
    cancelIt = driver.find_element_by_id('meeting:timeslots:'+str(slot)+':Cancel')
    cancelIt.click()
    #Not sure about this part
    finish = driver.find_element_by_id('meeting:save')
    finish.click()

def wait(slot):
    waitForIt = driver.find_element_by_id('meeting:timeslots:'+str(slot)+':addMeOnWaitingList')
    waitForIt.click()
    #Not sure about this part
    finish = driver.find_element_by_id('meeting:save')
    finish.click()

#wait here till 8am
def wait_start(runTime, action):
    startTime = time(*(map(int, runTime.split(':'))))
    while startTime > datetime.today().time(): # you can add here any additional variable to break loop if necessary
        sleep(1)# you can change 1 sec interval to any other
    return action


# wait_start2('08:00')

court = driver.find_element_by_id('items:meetinglist:10:cmdlink90')
court.click()
bookIt = driver.find_element_by_id('meeting:timeslots:'+str(2)+':addMe')
bookIt.click()
finish = driver.find_element_by_id('meeting:save')
finish.click()

# book(2)
# wait_start('13:20', lambda: book(3))
# """
# todo: Check cancel and wait finishes
#       Add user interface
# """