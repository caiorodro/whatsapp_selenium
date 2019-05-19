from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import json
import time
import datetime
import platform
import random
import os

class whatsApp:

    def __init__(self):
        self.customers = []

    def stringToJson(self, results):

        bracket = results.find("]")
        strEnd = ']' if bracket > -1 else '}'

        idx = results.index(strEnd) + 1
        strJson = results[0 : idx]

        singleQuot = strJson.find("'")

        if singleQuot > -1:
            return  json.loads(strJson.replace("'", '"'))

        elif singleQuot == -1:
            return json.loads(strJson)

    def findCustomers(self):
        # you'll must specify on NICKNAME field the same name of your whatsapp contacts in your cellphone

        strCustomers = ''.join(('[{"NICKNAME": "CAIO 1", "CONTATO": "CAIO RODRIGUES", "PROMOCAO": "|| ||https://linkdepromocao.com.br/" },', 
            '{"NICKNAME": "CAIO 2", "CONTATO": "CAIO RODRIGUES", "PROMOCAO": "|| ||https://linkdepromocao.com.br/" }]'))

        self.customers = self.stringToJson(strCustomers)


    def sendMessages(self, driver):
        userToFind = driver.find_element_by_class_name('copyable-text')
        lErrors = []

        for i, contato in enumerate(self.customers, start=1):

            try:
                nick = contato['NICKNAME']
                nomeContato = contato['CONTATO']
                promocao = contato['PROMOCAO']

                userToFind.clear()
                userToFind.send_keys(nick)

                time.sleep(5)

                user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(nick))
                user.click()

                textBox = driver.find_element_by_class_name('_2S1VP')

                now = datetime.datetime.now()

                regards = 'Bom dia {}, '

                if now.hour > 11 and now.hour < 19:
                    regards = 'Boa tarde {}, '
                elif now.hour > 18:
                    regards = 'Boa noite {}, '

                texto = 'Olá {}, ' if i % 2 == 0 else regards
                texto = texto.format(nomeContato)

                textBox.clear()
                textBox.send_keys(texto)
                textBox.send_keys(Keys.SHIFT + Keys.RETURN)

                campaign = promocao.split("||")

                for linha in campaign:
                    textBox.send_keys(linha)
                    textBox.send_keys(Keys.SHIFT + Keys.RETURN)

                secs = random.randint(4, 8)

                time.sleep(secs)

                textBox.send_keys(Keys.RETURN)

                userToFind.clear()
            except: 
                lErrors.append(contato['NICKNAME'])

    def prepareAndSendMessages(self):

        self.findCustomers()

        try:
            cwd = os.getcwd()

            # you'll must check the specific version of your google chrome installed and download the correct version of chromedriver
            
            driver_executable = 'chromedriver' if platform.system() == 'Darwin' else 'chromedriver.exe'

            pathChromeDriver = os.path.join(cwd, driver_executable)

            driver = webdriver.Chrome(pathChromeDriver)
            driver.get('https://web.whatsapp.com/')

            time.sleep(20)

            self.sendMessages(driver)
        except Exception as err:
            print(err)

    def __del__(self):
        pass