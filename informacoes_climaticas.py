import urllib.request
from urllib.parse import urlencode

def obter_informacoes_climaticas(cidade, chave_api):
    parametros = {'q': cidade, 'appid': chave_api, 'units': 'metric'}
    url = f"http://api.openweathermap.org/data/2.5/weather?{urlencode(parametros)}"

    try:
        with urllib.request.urlopen(url) as resposta:
            dados_climaticos = resposta.read().decode('utf-8')
            return dados_climaticos
    except urllib.error.URLError as e:
        print(f"Erro ao fazer a requisição: {e}")
        return None

cidade_desejada = "Viamão"
chave_api = "f544a43e75b1e764194088c036b5429d"

dados_climaticos = obter_informacoes_climaticas(cidade_desejada, chave_api)

if dados_climaticos is not None:
    print(dados_climaticos)
else:
    print("Não foi possível obter informações climáticas.")


