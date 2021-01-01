"""
Name: WLAN Rate changer
Note: Works only on Router Model: Huawei - HG630 V2
Author: kfrawee
"""

from os import system
from sys import exit
from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import Fore, init

from login import user, password
from welcome import welcome

# Chromedriver path
driver = webdriver.Chrome(ChromeDriverManager().install())

init(autoreset=True)
system('cls')

print(f"{Fore.CYAN}{welcome}")
sleep(3)
system('cls')


# Default Gateway url
default_gateway = r'https://192.168.1.1/'
driver.get(default_gateway)


def notSecure():
    """ For passing "Your connection is not private" """
    driver.find_element_by_id("details-button").click()
    driver.find_element_by_id("proceed-link").click()
    system('cls')


def login(user, password):
    """ Login function, requires user and password """
    driver.find_element_by_id("index_username").send_keys(user)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("loginbtn").click()
    system('cls')


def navigate():
    """ Navigate to get WLAN page """
    driver.find_element_by_id("homenetwork_settings_menu").click()
    sleep(2)

    driver.find_element_by_id("wlan_menuId").click()
    sleep(2)

    driver.find_element_by_id("wlan_ss_view_head_id").click()

    # Scroll Down & Right, You may change to your screen resolution
    driver.execute_script("window.scrollTo(1366,768)")
    system('cls')


def changeRate():
    """ Change Rate form dropdown menu """
    Rates = driver.find_element_by_id("wlan_ss_rate_ctrl")

    print(Fore.CYAN +
          f"\nYour current rate: {Select(Rates).first_selected_option.text}")

    print(Fore.YELLOW + f"\nAvailable Rates:")
    ratesList = []

    for rate in Select(Rates).options:
        print(Fore.YELLOW + f"- {rate.text}")
        ratesList.append(rate.text)

    rateDic = {'auto': 'auto',
               '1': '1 mbps',
               '2': '2 mbps',
               '5.5': '5.5 mbps',
               '6': '6 mbps',
               '9': '9 mbps',
               '11': '11 mbps',
               '12': '12 mbps',
               '18': '18 mbps',
               '24': '24 mbps',
               '36': '36 mbps',
               '48': '48 mbps',
               '54': '54 mbps',
               }

    while True:
        newRateIn = input("\nSelect new rate: ")
        if newRateIn in rateDic.keys():
            newRateOut = rateDic.get(newRateIn).title()
            if newRateOut == Select(Rates).first_selected_option.text:
                print(
                    Fore.CYAN + f"\nYour current rate is already {Select(Rates).first_selected_option.text}.\nTry another rate.")
            else:
                rateSelect = Select(Rates).select_by_visible_text(newRateOut)
                print(Fore.GREEN +
                      f"\nNew Rate applied successfully. ({newRateOut})")
                sleep(2)
                # Saving
                driver.find_element_by_id(
                    "SendSettings_submitbutton").click()
                sleep(2)
                system('cls')
                driver.quit()
                exit(1)

        else:
            print(Fore.RED + "\nRate is not availabe.")


def main():
    try:
        # Connection not Secure
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "details-button")))
        notSecure()
        # Login
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "index_username")))
        login(user, password)
        sleep(3)
        # Navigate
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "homenetwork_settings_menu")))
        navigate()
        # Change Rate
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "wlan_ss_rate_ctrl")))
        changeRate()

    except Exception as e:
        print(Fore.RED + f"{e}")
        sleep(3)

    finally:
        system('cls')
        driver.quit()
        exit(1)


if __name__ == "__main__":
    main()
