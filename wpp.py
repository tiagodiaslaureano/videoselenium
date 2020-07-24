from selenium import webdriver
from pessoas import lista_de_pessoas
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('https://web.whatsapp.com')

input('Digite ENTER quando executar o QR code!')

sleep(2)

msg = 'Temos uma promoção incrivel para você! Acesse: www.sitemuitobom.com.br'

for i in range(3):
	for contato in lista_de_pessoas:
		nome_contato = driver.find_element_by_xpath(f'//span[@title = "{contato}" ]')
		nome_contato.click()
		caixa_msg = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
		caixa_msg.click()
		caixa_msg.send_keys(msg)
		button_click = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
		button_click.click()
		sleep(1)