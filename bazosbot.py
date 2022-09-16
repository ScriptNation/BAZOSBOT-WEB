#!/bin/python

from flask import Flask, render_template
import requests
from bs4 importBeautifulSoup


app = Flask(__name__)

component = 'graficka'
#cena_od = input('CENA OD: ')
#cena_do = input('CENA DO: ')
cena_od = 80
cena_do = 300
baseurl = f"https://pc.bazos.sk/{component}/?hledat=&rubriky=pc&hlokalita=&humkreis=25&cenaod={cena_od}&cenado={cena_do}&Submit=H%C4%BEada%C5%A5&kitx=ano"

baseurl_test = f"https://pc.bazos.sk/{component}/?hledat=&rubriky=pc&hlokalita=&humkreis=25&cenaod={cena_od}&cenado={cena_do}&Submit=H%C4%BEada%C5%A5&kitx=ano"

#HEADERS
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

GPU_list = []
print('')
r = requests.get(baseurl)
soup = BeautifulSoup(r.content, 'lxml')

product_list = soup.find_all('div', class_='inzeraty inzeratyflex')

for item in product_list:
    name = item.find('h2', class_='nadpis').text.strip()
    price = item.find('div', class_='inzeratycena').text.strip()
    date = item.find('span', class_='velikost10').text.strip()
    link_s = item.find('a',href=True)['href']
    link = f'https://pc.bazos.sk{link_s}'

    GPU = {
        'COMPONENT': name,
        'date': date,
        'CENA': price+'\n',
        'link':link,
    }
    GPU_list.append(GPU)
    
#GPU infos
item1 = GPU_list[0]['COMPONENT'] + " :    " + GPU_list[0]['CENA']
item2 = GPU_list[1]['COMPONENT'] + " :    " + GPU_list[1]['CENA']
item3 = GPU_list[2]['COMPONENT'] + " :    " + GPU_list[2]['CENA']
item4 = GPU_list[3]['COMPONENT'] + " :    " + GPU_list[3]['CENA']
item5 = GPU_list[4]['COMPONENT'] + " :    " + GPU_list[4]['CENA']
item6 = GPU_list[5]['COMPONENT'] + " :    " + GPU_list[5]['CENA']
item7 = GPU_list[6]['COMPONENT'] + " :    " + GPU_list[6]['CENA']
item8 = GPU_list[7]['COMPONENT'] + " :    " + GPU_list[7]['CENA']
item9 = GPU_list[8]['COMPONENT'] + " :    " + GPU_list[8]['CENA']
item10 = GPU_list[9]['COMPONENT'] + " :    " + GPU_list[9]['CENA']
#Links for GPU
link1 = GPU_list[0]['link']
link2 = GPU_list[1]['link']
link3 = GPU_list[2]['link']
link4 = GPU_list[3]['link']
link5 = GPU_list[4]['link']
link6 = GPU_list[5]['link']
link7 = GPU_list[6]['link']
link8 = GPU_list[7]['link']
link9 = GPU_list[8]['link']
link10 = GPU_list[9]['link']

@app.route("/")
def index():
    return render_template("bazosbotweb.html", i1=item1,i2=item2,i3=item3,i4=item4,i5=item5,i6=item6,i7=item7,i8=item8,i9=item9,i10=item10)


app.run(host="0.0.0.0",port=80)
