from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver=webdriver.Chrome(options)
driver.get("http://aliexpress.com")

wait = WebDriverWait(driver, 10)

login_box = driver.find_element(By.XPATH,value='//*[@id="_full_container_header_23_"]/div[2]/div/div[2]/div[3]/div/b/span[1]')
login_box.click()

login_btn = wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "my-account--signin--RiPQVPB"))
)
#driver.find_element(By.CLASS_NAME, value="my-account--signin--RiPQVPB")
login_btn.click()

google_btn=driver.find_element(By.CLASS_NAME, '._1unVQ')
google_btn.click()


input()

driver.quit()
