import requests

API_KEY = 'f544a43e75b1e764194088c036b5429d' 
cidade = 'Viamão'

link =  f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}'

requisicao = requests.get(link)
requisicao.dic = (requisicao.json())  
descricao = requisicao.dic['weather'][0]['description']
temperatura_kelvin = requisicao.dic['main']['temp']

temperatura = temperatura_kelvin - 273.15
print(requisicao.dic)
print('-')
print(cidade +',', descricao +',', temperatura)


