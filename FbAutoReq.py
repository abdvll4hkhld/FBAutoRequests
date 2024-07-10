from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



usr = input("Enter your username:" )
pas = input("Enter your password:" )
search = input("What do you want to search:" )

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome()
print("Chrome opened")
driver.get('https://www.facebook.com/')
print("Facebook opened")
sleep(3)

usrname_box = driver.find_element(By.ID, 'email')
usrname_box.send_keys(usr)
usrname_box.click()
sleep(1)

password_box = driver.find_element(By.ID, 'pass')
password_box.send_keys(pas)
password_box.click()
sleep(1)

login_button = driver.find_element(By.XPATH, "//button[@name='login']")
login_button.click()
sleep(5)
print("Done")

# friends_icon = driver.find_element(By.XPATH, "//a[@aria-label='Friends']")
# print("reached here")

# sleep(15)
# friends_icon.click()
# print("Opened friends tab")
# print('')

search_box = driver.find_element(By.XPATH, "//input[@aria-label='Search Facebook']")
print("Search found")
print("Search clicked")
search_box.send_keys(search, Keys.ENTER)

print("Search value sent")
sleep(5)
print("Search complete")


def get_profile_links():
    return driver.find_elements(By.XPATH, '//a[contains(@href, "/profile.php?id=")]')


profile_links = get_profile_links()
lenn = (f"Found {len(profile_links)} profile links")
print(lenn, 'length')

original_window = driver.current_window_handle  

index = 1  

while index < len(profile_links):
    link = profile_links[index]
    try:
        profile_url = link.get_attribute('href')
        if profile_url:
            driver.execute_script("window.open(arguments[0]);", profile_url)  
            sleep(2)
            driver.switch_to.window(driver.window_handles[-1])  
            print(f"Visited profile: {profile_url}")
            try:
                add_friend_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Add friend']"))
                )
                if add_friend_button:
                    add_friend_button.click()
                    print("Clicked 'Add Friend' button")
                    sleep(2)
            except Exception as e:
                print(f"Error finding 'Add Friend' button: {e}")
            finally:
                driver.close()  
                driver.switch_to.window(original_window)  
        else:
            print("No href attribute found for this link.")
    except Exception as e:
        print(f"Error visiting profile: {e}")
        driver.switch_to.window(original_window)  
    
    index += 1 
