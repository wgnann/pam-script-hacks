# pam-script-hacks
Alguns hacks para usar mecanismos distintos, por ora somente de login, no PAM.

## Dependências
  * libpam-script
  * pamtester
  * eapoltest (RADIUS)
  * curl (OAUTH1 sem python)
  * libxml2-utils (OAUTH1 sem python)
  * python3-bs4 (OAUTH1)
  * python3-requests (OAUTH1)

## Como instalar?
Para instalar os hacks, é preciso ter suporte ao módulo de scripts do PAM. Feito isso, é preciso colocar o script, executável, com o nome: `pam_script_auth` no diretório via parâmetro `dir=/seu/path` ou no padrão do debian, `/usr/share/libpam-script`. Ou seja:
  * instalar as dependências;
  * configurar o PAM: pode usar `pam-auth-update` ou editar o arquivo correspondente em `/etc/pam.d`;
  * copiar o conteúdo do módulo específico para o diretório configurado;
  * editar o script para usar o diretório (está como padrão do debian).

No escopo desse executável, existirão diversas variáveis de ambiente. Há uma documentação melhor no exemplo `logscript` que vem com o `libpam-script`.

## Como testar?
Rodar o pamtester. Exemplo: `pamtester auth NUSP authenticate`.

## Referências
O modelo do RADIUS veio daqui: `http://deployingradius.com/scripts/eapol_test/peap-mschapv2.conf`.
