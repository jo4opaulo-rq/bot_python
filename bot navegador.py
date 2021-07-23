from selenium import webdriver
import selenium
import time

navegador = webdriver.Chrome()
navegador.get('https:login.live.com')

navegador.find_element_by_xpath('//*[@id="i0116"]').send_keys(#Seu e-mail)
navegador.find_element_by_xpath('//*[@id="idSIButton9"]').click()
navegador.find_element_by_xpath('//*[@id="i0118"]').send_keys(#sua senha)
time.sleep(2)
navegador.find_element_by_xpath('//*[@id="idSIButton9"]').click()

navegador.get("https://outlook.live.com/mail/0/inbox")