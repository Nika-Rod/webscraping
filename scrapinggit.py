from itertools import product
from re import search
import time
from xml.dom.minidom import Element
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import ActionChains

def scroll() : 
 driver.execute_script('window.scroll(0, 0,)')  
 driver.execute_script('window.scroll(0, 500,)')
 driver.execute_script('window.scroll(0, 1000,)')
 time.sleep(1)
 driver.execute_script('window.scroll(0, 1500,)')
 driver.execute_script('window.scroll(0, 2000,)')
 driver.execute_script('window.scroll(0, 2500,)')
 time.sleep(1)
 driver.execute_script('window.scroll(0, 3000,)')
 driver.execute_script('window.scroll(0, 3500,)')
 driver.execute_script('window.scroll(0, 4000,)')
 time.sleep(1)
 driver.execute_script('window.scroll(0, 4500,)')
 driver.execute_script('window.scroll(0, 5000,)')
 driver.execute_script('window.scroll(0, 5500,)')
 time.sleep(1)
 driver.execute_script('window.scroll(0, 6000,)')
 driver.execute_script('window.scroll(0, 6500,)')
 driver.execute_script('window.scroll(0, 7000,)')
 time.sleep(1)
 driver.execute_script('window.scroll(0, 7500,)')
 driver.execute_script('window.scroll(0, 8000,)')
 driver.execute_script('window.scroll(0, 8500,)')
 time.sleep(1) 



url="https://www.mercadolivre.com.br/"

driver = webdriver.Firefox()
driver.get(url)
driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]/button[1]").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/header/div/div[2]/ul/li[3]/a").click()
scroll()



conteudo = driver.page_source
soup=BeautifulSoup(conteudo,"html.parser")


produtos= soup.findAll("div", class_="promotion-item__description")


lista_produtos=[]



for produto in produtos:
    preco = produto.find("span", class_="promotion-item__price")
    nome = produto.find("p", class_="promotion-item__title")

    lista_produtos.append([nome, preco])


produtos_dt = pd.DataFrame(lista_produtos, columns=["Nome", "Preço"])
produtos_dt.to_csv("arquivo.csv", index=False)

print(produtos_dt)


#parte2

url_celulares = "https://www.mercadolivre.com.br/ofertas#nav-header"

driver.get(url_celulares)
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/main/div/section[1]/div/section/div/section/div[2]/button[2]").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/main/div/section[1]/div/section/div/section/div[2]/div/div/div[9]/div").click()
time.sleep(2)
scroll()

conteudo = driver.page_source
soup=BeautifulSoup(conteudo,"html.parser")

celulares= soup.findAll("div", class_="promotion-item__description")

lista_celulares=[]

for celular in celulares:
    preco = celular.find("span", class_="promotion-item__price")
    nome = celular.find("p", class_="promotion-item__title")

    lista_celulares.append([nome, preco])


    celulares_dt = pd.DataFrame(lista_celulares, columns=["Nome", "Preço"])
    celulares_dt.to_csv("celulares.csv", index=False)

    print(celulares_dt)

    #parte3

url_notebooks = "https://www.mercadolivre.com.br/ofertas?domain_id=MLB-CELLPHONES&container_id=MLB779535-1#origin=scut&filter_applied=domain_id&filter_position=9&is_recommended_domain=false"
driver.get(url_notebooks)
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/main/div/section[1]/div/section/div/section/div[2]/div/div/div[10]/div").click()
time.sleep(2)
scroll()

conteudo = driver.page_source
soup=BeautifulSoup(conteudo,"html.parser")

notebooks= soup.findAll("div", class_="promotion-item__description")

lista_notebooks=[]

for notebook in notebooks:
    preco = notebook.find("span", class_="promotion-item__price")
    nome = notebook.find("p", class_="promotion-item__title")

    lista_notebooks.append([nome, preco])

    
    notebooks_dt = pd.DataFrame(lista_notebooks, columns=["Nome", "Preço"])
    notebooks_dt.to_csv("notebooks.csv", index=False)

    print(notebooks_dt)

driver.quit()