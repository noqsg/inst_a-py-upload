# Forgot original author, sad
# Source Selenium: https://medium.com/@ivantay2003/selenium-cheat-sheet-in-python-87221ee06c83
# Project: Instagram Posting Bot Selenium
import os, sys, click, autoit
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

@click.command()
@click.option(
    '--username',
    '-u',
    prompt='Username: ',
    help='The username to your Instagram account.',
    required=True,
)
@click.option(
    '--password',
    '-p',
    prompt='Password: ',
    help='The password to your Instagram account.',
    required=True,
)
@click.option(
    '--image-path',
    '-i',
    prompt='The Path to the Image: ',
    help="The path to the image you want to upload. Until now unly work if its going from the path you run the script from",
    required=True,
)
@click.option(
    '--caption',
    '-c',
    prompt='Caption: ',
    help='The caption for underneath your image.',
)

def caesar(username, password, image_path, caption):
    # Variables
    #image_path = r"%s" % imagepath #1. path should not start with a back slash  
    firstrun = os.path.isdir('selenium')

    # Configuration Chrome
    mobile_emulation = { "deviceName": "Pixel 2" }
    opts = webdriver.ChromeOptions()
    opts.add_argument("user-data-dir=selenium") # Source: https://stackoverflow.com/questions/15058462/how-to-save-and-load-cookies-using-python-selenium-webdriver
    opts.add_experimental_option("mobileEmulation", mobile_emulation)

    # Loads ChromeWebdriver
    driver = webdriver.Chrome(executable_path=r"chromedriver.exe",options=opts) # you must enter the path to your driver

    # Opens Instagram.com
    main_url = "https://www.instagram.com"
    driver.get(main_url)

    sleep(4)

    def login():
        login_button = driver.find_element_by_xpath("//button[contains(text(),'Log In')]")
        login_button.click()
        sleep(3)
        username_input = driver.find_element_by_xpath("//input[@name='username']")
        username_input.send_keys(username)
        password_input = driver.find_element_by_xpath("//input[@name='password']")
        password_input.send_keys(password)
        password_input.submit()

    # Closing reactivated Popup
    def close_reactivated():
        try:
            sleep(2)
            not_now_btn = driver.find_element_by_xpath("//a[contains(text(),'Not Now')]")
            not_now_btn.click()
        except:
            pass


    # Closing notification Popup
    def close_notification():
        try: 
            sleep(2)
            close_noti_btn = driver.find_element_by_xpath("//button[contains(text(),'Not Now')]")
            close_noti_btn.click()
            sleep(2)
        except:
            pass


    # Closing add to Home Popup
    def close_add_to_home():
        sleep(3) 
        close_addHome_btn = driver.find_element_by_xpath("//button[contains(text(),'Cancel')]")
        close_addHome_btn.click()
        sleep(1)

    # Checks if Script run before
    if firstrun:
        print("used the cookies")
        sleep(2)
        close_notification()
        sleep(2)
    else:
        login()
        print("Fresh Login, takes longer")
        close_notification()
        close_reactivated()
        sleep(4)
        close_add_to_home()
        sleep(3)
        close_notification()

    

    # Posting Picture
    new_post_btn = driver.find_element_by_xpath("//div[@role='menuitem']")
    new_post_btn.click()
    sleep(1.5)
    autoit.win_active("Open") 
    sleep(2)
    autoit.control_send("Open","Edit1",image_path) 
    sleep(1.5)
    autoit.control_send("Open","Edit1","{ENTER}")

    sleep(2)

    next_btn = driver.find_element_by_xpath("//button[contains(text(),'Next')]")
    next_btn.click()

    sleep(1.5)

    caption_field = driver.find_element_by_xpath("//textarea[@aria-label='Write a caption…']")
    caption_field.send_keys(caption)

    share_btn = driver.find_element_by_xpath("//button[contains(text(),'Share')]")
    share_btn.click()
    # -- 

    sleep(25)
    driver.close()

if __name__ == '__main__':
    caesar()