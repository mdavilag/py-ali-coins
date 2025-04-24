from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time
from notifications import notify
from log import logging

options = webdriver.ChromeOptions()
options.add_experimental_option("mobileEmulation", {
    "deviceName": "iPhone X"
})
options.add_argument(r"user-data-dir=C:\\ChromeDriver\\Profiles\\profile")
options.add_argument("--headless")

service = Service(r"C:\\ChromeDriver\chromedriver.exe")


driver = webdriver.Chrome(service=service, options=options)

driver.get("http://aliexpress.com")
print("-- Entrando na pagina aliexpress")
wait = WebDriverWait(driver, 10)
print("-- Procurando ícone da conta")
login_box = wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, 'comet-icon-myaccount'))
)
#driver.find_element(By.XPATH,value='//*[@id="_full_container_header_23_"]/div[2]/div/div[2]/div[3]/div/b/span[1]')
time.sleep(2)
login_box.click()
print("-- Ícone da conta clicado")
time.sleep(1)
print("-- Procurando ícone de moedas")
coinMenu_btn = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, "comet-icon-coins"))
)
coinMenu_btn.click()
print("-- Ícone de moedas clicado - redirecionando para página de moedas")

print("-- Procurando botão para resgatar moedas")
try:
    getCoins_btn = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class^="aecoin-unchecked"]'))
    )
    getCoins_btn.click()
    notify("Moedas recolhidas!!","Moedas recolhidas com sucesso!")
    print("-- Moedas recolhidas com sucesso")
    logging.info("Moedas recolhiedas com sucesso - Notificacao enviada")
    
except:
    if(EC.presence_of_element_located((By.CSS_SELECTOR,'div[class^="aecoin-checked"]'))):
        print("-- Moedas já recolhidas hoje")
        logging.info("Moedas já recolhidas hoje")
    else:
        print("-- Erro ao recolher moedas")
        notify("Error..","Erro ao tentar recolher moedas")
        logging.error("Erro ao recolher moedas")
    time.sleep(2)
    print("-- Encerrando script")
time.sleep(5)
driver.quit()



