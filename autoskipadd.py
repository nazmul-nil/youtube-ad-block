# from selenium import webdriver
# import selenium.webdriver.support.ui as ui
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.support import expected_conditions as EC

# path = r'driver/chromedriver'
# url = "https://www.youtube.com/"
   

# options = webdriver.ChromeOptions()
# options.add_argument("user-data-dir=C:/Users/Nazm/AppData/Local/Google/Chrome/User Data/")

# driver = webdriver.Chrome(executable_path="lib/chromedriver",options=options)
# driver.maximize_window()
# driver.get(url)

# wait = ui.WebDriverWait(driver,300)
# while True:
#     try:
#         if EC.presence_of_element_located((By.XPATH,".//div/div/div/div/div/span/button/div[contains(text(),'Skip Ad')]")):
#             button=driver.find_element_by_xpath(".//div/div/div/div/div/span/button/div[contains(text(),'Skip Ad')]")
#             driver.execute_script("arguments[0].click();",button)
#             print("Skipped")
#             sleep(2)
#         else:
#              continue
#     except NoSuchElementException:
#         print("skip button not found")
#         sleep(2)


from selenium import webdriver
import selenium.webdriver.support.ui as ui
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

# Path to the chromedriver executable
path = r'C:/Users/Nazm/Documents/Python Scripts/youtube-ad-bot/lib/chromedriver.exe'

# URL to open
url = "https://www.youtube.com/"

# Setup Chrome options
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:/Users/Nazm/AppData/Local/Google/Chrome/User Data/")

# Create a Service object
service = Service(path)

# Initialize the Chrome driver with the Service object and options
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
driver.get(url)

# Setup wait object
wait = ui.WebDriverWait(driver, 300)

while True:
    try:
        # Wait for the "Skip Ad" button to appear
        skip_button_locator = (By.XPATH, ".//div/div/div/div/div/span/button/div[contains(text(),'Skip')]")
        wait.until(EC.presence_of_element_located(skip_button_locator))

        # Find the "Skip Ad" button and click it
        button = driver.find_element(By.XPATH, ".//div/div/div/div/div/span/button/div[contains(text(),'Skip')]")
        driver.execute_script("arguments[0].click();", button)
        print("Skipped")
        sleep(2)
    except NoSuchElementException:
        print("Skip button not found")
        sleep(2)
    except Exception as e:
        print(f"An error occurred: {e}")
        sleep(2)
