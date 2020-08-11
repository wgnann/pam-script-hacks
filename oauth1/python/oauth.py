import os
import requests
from bs4 import BeautifulSoup

user = os.environ['PAM_USER']
password = os.environ['PAM_AUTHTOK']

session = requests.Session()

# estamos usando o COPACO como meio de login
page = session.get("https://copaco.ime.usp.br/login")
parser = BeautifulSoup(page.content, 'html.parser')

form = parser.find('form', id='formLogin')
oauth_token = form.find('input', id='oauth_token').get('value')
callback_id = form.find('input', id='callback_id').get('value')

payload = {
    'loginUsuario': user,
    'senhaUsuario': password,
    'oauth_token': oauth_token,
    'callback_id': callback_id
}

page = session.post("https://uspdigital.usp.br/wsusuario/oauth/authorize?oauth_token="+oauth_token+"&callback_id="+callback_id, data=payload)
parser = BeautifulSoup(page.content, 'html.parser')

# definindo o status de login
# a partir do que o COPACO devolve
# queremos ver o usuário na página e o cookie de login
if user in parser.get_text():
    if 'copaco_ime_usp_session' in [c.name for c in session.cookies]:
        exit(0)
exit(1)
