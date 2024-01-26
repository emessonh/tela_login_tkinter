from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

PROXY = f'http://{os.getenv('usuario')}:{os.getenv('senha')}@{os.getenv('firewall')}'
webdriver.DesiredCapabilities.CHROME['proxy'] = {
"httpProxy": PROXY,
"ftpProxy": PROXY,
"sslProxy": PROXY,
"proxyType": "manual",

}

# /html/body/div[1]/div/a[4]
opcoes = webdriver.ChromeOptions()
# opcoes.add_argument('--headless=new')

with webdriver.Chrome(options=opcoes) as driver:
    # driver.get("https://www.selenium.dev/pt-br/")
    # //*[@id="main_navbar"]/ul/li[7]/div/a
    driver.get("https://hml.sei.seplag.al.gov.br/sip/login.php?sigla_orgao_sistema=AL&sigla_sistema=SEI")

    # Login
    driver.find_element(By.XPATH, '//*[@id="txtUsuario"]').send_keys('11136701427')
    driver.find_element(By.XPATH, '//*[@id="pwdSenha"]').send_keys('Asp@0715')
    driver.find_element(By.XPATH, '//*[@id="selOrgao"]').send_keys('SEPLAG')
    driver.find_element(By.XPATH, '//*[@id="sbmLogin"]').click()

    # processo
    driver.find_element(By.XPATH, '//*[@id="txtPesquisaRapida"]').send_keys('E:01700.0000000002/2022')
    driver.find_element(By.XPATH, '//*[@id="txtPesquisaRapida"]').send_keys(Keys.ENTER)
    try:
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//html/body/div[1]/div/a[4]'))
        )
        # src="/infra_css/imagens/mais.gif"
        # Once the element is found, you can perform actions on it
        element.click()
        print('clicou no elemento')

    except Exception:
        print("Timed out waiting for the element to be present")
    
    # Close the browser window
    driver.quit()
