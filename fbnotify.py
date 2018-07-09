# This script brings your recent facebook notifications in one place thus saving your time from getting indulged in your feed.

# Steps to run the script:
    # Run python fbnotify.py
    # The script will prompt you to enter email and password. Don't worry its totally safe.
    # Voila, all your new notifications will be listed. 

from selenium import webdriver
import time, getpass
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display

display = Display(visible=0, size=(800, 600))
display.start()

option = webdriver.ChromeOptions()
option.add_argument("--disable-notifications")

capa = DesiredCapabilities.CHROME.copy()
capa["pageLoadStrategy"] = "none"
browser = webdriver.Chrome(desired_capabilities = capa, chrome_options = option)
wait = WebDriverWait(browser,240)

try:
    browser.get('https://www.facebook.com/')
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#u_0_2')))

    email = raw_input('Enter your email: ')
    emailElem = browser.find_element_by_css_selector('#email')
    emailElem.send_keys(email)


    p = getpass.getpass()
    passElem = browser.find_element_by_css_selector('#pass')
    passElem.send_keys(p)

    logElem = browser.find_element_by_css_selector('#u_0_2')
    logElem.click()

    wait.until(EC.presence_of_element_located((By.NAME, 'notifications')))
    notifButton = browser.find_element_by_name('notifications')
    notifButton.click()
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, '_fyy')))
    notif = browser.find_elements_by_css_selector('._4l_v')
    numNotif = min(15,len(notif))
    for i in range(numNotif):
        print('Notif ' + str(i+1) +': '+  notif[i].text.strip() + '\n')
    browser.quit()
    display.stop()

    
except:
    print('There was an error executing the task. Maybe the page failed to load. Check your connection and run the script again')
    



