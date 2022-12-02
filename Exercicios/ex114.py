# Crie um código em Python que teste se o site Pudim está acessivel pelo computador usado.
import requests

url = 'http://pudim.com.br/'

try:
    if requests.get(url).status_code == 200:
        print('O site \"Pudim\" está disponivel.')
    else:
        print('O site \"Pudim\" não está disponivel no momento.')
except:
    print('O site \"Pudim\" não está disponivel no momento.')
