from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def enel(codigo_cliente, cpf_cliente):
    firefox = webdriver.Firefox()
    firefox.get('https://www.eneldistribuicao.com.br/rj/LoginAcessoRapidoSegundaVia.aspx')

    path_codigo_cliente = "ctl00$CONTENT$NumeroCliente"
    path_cpf_cliente = "ctl00$CONTENT$Documento"
    path_ok = "ctl00$CONTENT$Ok"

    firefox.find_element_by_name(path_codigo_cliente).send_keys(codigo_cliente)
    firefox.find_element_by_name(path_cpf_cliente).send_keys(cpf_cliente)
    firefox.find_element_by_name(path_ok).click()

    time.sleep(3)

    status_ultima_fatura = '/html/body/form/div[4]/div/div/div[2]/div[2]/div[6]/div/div/table/tbody/tr[2]/td[8]'
    status = firefox.find_element_by_xpath(status_ultima_fatura).text
    if status == "EM ABERTO":
        checkbox_ultima_fatura = 'ctl00$CONTENT$segviarapida$GridViewSegVia$ctl02$CheckFatura'
        firefox.find_element_by_name(checkbox_ultima_fatura).click()

        time.sleep(3)

        salvar_em_pdf = 'ctl00$CONTENT$segviarapida$btnSalvarPDF'
        firefox.find_element_by_name(salvar_em_pdf).click()
    else:
        return "Nada a pagar."
