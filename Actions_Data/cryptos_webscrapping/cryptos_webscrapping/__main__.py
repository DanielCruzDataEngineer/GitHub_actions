from json import encoder
from os import readlink
import pandas as pd
import requests
from bs4 import BeautifulSoup
import regex as re
import datetime
import time
from pymongo import MongoClient
import asyncio
import os
from lxml import etree
def func():

    url_base = f'https://coinranking.com/'

    

    response = requests.get(url_base)

    site = BeautifulSoup(response.text, 'html.parser')
    dom = etree.HTML(str(site))
    titulo_df = []
    price_df = []
    link_df  = []
    percent_df = []
    for i in dom.xpath("//tr[@class=\"table__row table__row--click table__row--full-width\"]"):
        titulo = i.xpath(
            './/a[@class="profile__link"]/text()'
        )[0]

        titulo = str(titulo).replace('\n','')
        price = i.xpath(
            './/div[@class="valuta valuta--light"]/text()'
        )[0]

        price = str(price).replace(',','.')

        volume = i.xpath(
            'td[4]//div/text()'
        )[0]
        volume = str(volume).replace('\n','')
        link = i.xpath(
            './/a[@class="profile__link"]/@href'
        )[0]
        link = 'https://coinranking.com' + str(link).replace('\n','')


        #Etapa de tratamento de dados em massa
        titulo = re.sub(re.compile("[\s*]"),"",titulo)
        price = re.sub(re.compile("[\s*\$]"),"",price)

        percent_df.append(volume)
        titulo_df.append( titulo)
        link_df.append(link)
        price_df.append(price)

    df_cryptos = pd.DataFrame(list(zip( titulo_df,link_df, price_df,percent_df, )), columns=[

                                        'Coin','Link', 'Price', 'Volume(1h)'])
    print(df_cryptos)


    # print('\n\n')
            # print(df_produtos)
    df_cryptos.to_excel("cryptos.xlsx")
    # # MONGODB_CONNECTION_STRING = os.environ['MONGODB_CONNECTION_STRING']
    # client = MongoClient("mongodb+srv://rodridc:220412@cluster0.klgekbo.mongodb.net/?retryWrites=true&w=majority")
    # client.server_info()['ok']

    # symbol_dict = df_produtos.to_dict('records')
    # db = client.cryptos_exchanges
    # db.cryptos_exchanges.insert_many(symbol_dict)




if __name__ == '__main__':
   
    func()



