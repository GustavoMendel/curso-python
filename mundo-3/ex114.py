import requests

def verificaPudim():
    try:
        response = requests.get('http://pudim.com.br')
        print('Site Pudim acessado com sucesso!')
    except Exception:
        print('Site Pudim não conseguiu ser acessado!')

verificaPudim()
