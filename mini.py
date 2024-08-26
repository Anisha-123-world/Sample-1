import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


def capture_ss(profile_url , screenshot_path ):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu") 

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service = service , options= chrome_options)
        
        try:
            driver.get(profile_url)
            time.sleep(3)
            driver.save_screenshot(screenshot_path)
            print(f"the screenshot is saved at {screenshot_path}")
        
        finally:
            driver.quit()

name = input("enter the id name: ")
profile_url = f"https://www.instagram.com/{name}" 
screenshot_path = f"{name}_screenshot.png"

capture_ss(profile_url , screenshot_path)





        
