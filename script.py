from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("mobileEmulation", {
    "deviceName": "iPhone X"
})

driver = webdriver.Chrome(options)

driver.get("http://aliexpress.com")

wait = WebDriverWait(driver, 10)
#input("Esperando..")
login_box = wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, 'comet-icon-account'))
)
#driver.find_element(By.XPATH,value='//*[@id="_full_container_header_23_"]/div[2]/div/div[2]/div[3]/div/b/span[1]')
login_box.click()
print("Clicado no ícone")
print("Procurando botão de outros")
login_btn = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, "scene-login-icon-more"))
)
print("Achou botão")
#driver.find_element(By.CLASS_NAME, value="my-account--signin--RiPQVPB")
login_btn.click()

login_input=wait.until(
    EC.presence_of_element_located((By.CLASS_NAME,'cosmos-input'))
)
#driver.find_element(By.CLASS_NAME, '._1unVQ')
login_input.click()
login_input.send_keys("matdavila.97@gmail.com")

login_input.send_keys(Keys.RETURN)
login_pwd = wait.until(
    EC.presence_of_element_located((By.ID, 'fm-login-password'))
)
login_pwd.click()
login_pwd.send_keys("teste123")
login_pwd.send_keys(Keys.RETURN)
input()


input()
driver.quit()



