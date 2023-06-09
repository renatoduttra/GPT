from senhagoogle import API_KEY
import requests
import json
import time

# Chave de API do Google Places
api_key = API_KEY  # Substitua pela sua chave de API do Google Places

# Palavra-chave que você deseja pesquisar
keyword = 'advocacia'  # Substitua pela palavra-chave desejada

# Localização que você deseja pesquisar (no exemplo, Brasília, DF)
location = '-15.644213346051028, -47.829548118720055'  # Substitua pela localização desejada


# URL da API do Google Places para pesquisa de empresas
url = f'https://maps.googleapis.com/maps/api/place/textsearch/json?query={keyword}&location={location}&radius=5000&key={api_key}'

# Faz uma requisição GET para a URL e armazena a resposta
response = requests.get(url)

# Verifica se a requisição foi bem sucedida
if response.status_code == 200:

    # Analisa o JSON retornado usando a biblioteca json
    data = response.json()

    # Imprime o nome das empresas encontradas
    for result in data['results']:
        print(result['name'])

    # Verifica se há mais páginas de resultados
    while 'next_page_token' in data:
        # Aguarda 2 segundos antes de fazer uma nova solicitação para a próxima página de resultados
        time.sleep(2)
        # Faz uma nova solicitação GET para a próxima página de resultados
        next_page_url = f'https://maps.googleapis.com/maps/api/place/textsearch/json?pagetoken={data["next_page_token"]}&key={api_key}'
        next_page_response = requests.get(next_page_url)
        next_page_data = next_page_response.json()
        # Imprime o nome das empresas encontradas na próxima página
        for result in next_page_data['results']:
            print(result['name'])
        # Atualiza o valor de data para o objeto JSON da próxima página de resultados
        data = next_page_data

else:
    # Imprime uma mensagem de erro caso a requisição não tenha sido bem sucedida
    print('Erro ao acessar a API do Google Places: ', response.status_code)