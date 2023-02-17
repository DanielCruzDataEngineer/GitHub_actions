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

def func():

    url_base = f'https://coinranking.com/'

    

    response = requests.get(url_base)

    site = BeautifulSoup(response.text, 'html.parser')

    produtos = site.findAll('tr', attrs={'class': 'table__row table__row--click table__row--full-width'})
    titulo_df = []
    real_df = []
    link_df  = []
    local_df = []
    percent_df = []
    hour_df = []
    day_df = []
    month_df = []
    if (produtos):
        for produto in produtos:
            
            titulo = produto.find('a', attrs={'class': 'profile__link'}).text
            titulo = re.sub(re.compile("[\n^\s+]"),"",titulo)
            link = produto.find('a', attrs={'class': 'profile__link'})
            real = produto.find('div', attrs={'class': 'valuta valuta--light'}).text
            real = re.sub(re.compile("[\s+\$]"),"",real)
            now = datetime.datetime.now()

            day = str(now.day) + '-'+ str(now.month) + '-' + str(now.year) 
            hour = str(now.hour)
            
            percent = produto.find('div', attrs={'class': re.compile('change change--light\s*\w*\-*\-*\w*')}).get_text()
            percent = re.sub(re.compile("[\s+\n]"),"",percent)
            print(percent)
            percent_df.append(percent)
            hour_df.append(hour)
            day_df.append(day)
            titulo_df.append( titulo)
            link_df.append("https://coinranking.com"+ link['href'])
            real_df.append(real) 

            print('Título da Crypto:', titulo)
            print('Link da crypto:', "https://coinranking.com"+link['href'])
            print("Preço da Crypto :",real)


            df_produtos = pd.DataFrame(list(zip( titulo_df,link_df, real_df,percent_df, day_df,hour_df)), columns=[

                                        'Coin','Link', 'Price', 'Volume(1h)','Data','Hora'])

            print('\n\n')
            # print(df_produtos)
    # df_produtos.to_excel("cryptos.xlsx")
    # # MONGODB_CONNECTION_STRING = os.environ['MONGODB_CONNECTION_STRING']
    # client = MongoClient("mongodb+srv://rodridc:220412@cluster0.klgekbo.mongodb.net/?retryWrites=true&w=majority")
    # client.server_info()['ok']

    # symbol_dict = df_produtos.to_dict('records')
    # db = client.cryptos_exchanges
    # db.cryptos_exchanges.insert_many(symbol_dict)




if __name__ == '__main__':
   
    func()



