from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def aguas_de_niteroi(codigo_cliente, cpf_cliente):
    firefox = webdriver.Firefox()
    firefox.get('https://www.grupoaguasdobrasil.com.br/aguas-niteroi/')

    path_codigo_cliente = "matricula"
    path_cpf_cliente = "documento"
    path_ok = "/html/body/div/div/main/article/div[1]/div/div/form/button"

    firefox.find_element_by_name(path_codigo_cliente).send_keys(codigo_cliente)
    firefox.find_element_by_name(path_cpf_cliente).send_keys(cpf_cliente)
    firefox.find_element_by_xpath(path_ok).click()

    time.sleep(5)

    status_ultima_fatura = '/html/body/div/div/main/div[2]/div/label[1]/div[2]/div[1]/div/div[3]/span[2]/span[2]'
    status = firefox.find_element_by_xpath(status_ultima_fatura).text

    if status != "PAGO":
        checkbox_ultima_fatura = "/html/body/div/div/main/div[2]/div/label[1]/div[1]/div"
        firefox.find_element_by_xpath(checkbox_ultima_fatura).click()
        time.sleep(1)

        salvar_em_pdf = "/html/body/div/div/main/div[3]/div[2]/div/div[1]/button[2]"
        firefox.find_element_by_xpath(salvar_em_pdf).click()
    else:
        return "Nada a pagar."
