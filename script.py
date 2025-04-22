from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("mobileEmulation", {
    "deviceName": "iPhone X"
})
options.add_argument(r"user-data-dir=C:\\ChromeDriver\\Profiles\\profile")

service = Service(r"C:\\ChromeDriver\chromedriver.exe")


driver = webdriver.Chrome(service=service, options=options)

driver.get("http://aliexpress.com")
print("Aguardando")
#input()
wait = WebDriverWait(driver, 10)
#input("Esperando..")
login_box = wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, 'comet-icon-myaccount'))
)
#driver.find_element(By.XPATH,value='//*[@id="_full_container_header_23_"]/div[2]/div/div[2]/div[3]/div/b/span[1]')
time.sleep(2)
login_box.click()
print("Clicado no ícone")
time.sleep(1)
print("Procurando botão de moedas")
coinMenu_btn = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, "comet-icon-coins"))
)
print("Achou botão")
#driver.find_element(By.CLASS_NAME, value="my-account--signin--RiPQVPB")
coinMenu_btn.click()
input()



input()
driver.quit()



