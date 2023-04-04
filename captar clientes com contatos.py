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

    # Percorre os resultados e obtém os detalhes de cada lugar
    for result in data['results']:
        place_id = result['place_id']
        details_url = f'https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=name,formatted_address,website,international_phone_number&key={api_key}'
        details_response = requests.get(details_url)
        details_data = details_response.json()

        # Extrai as informações de contato e as imprime
        print(result['name'])
        details = details_data['result']
        if 'formatted_address' in details:
            print(f"Endereço: {details['formatted_address']}")
        if 'website' in details:
            print(f"Website: {details['website']}")
        if 'international_phone_number' in details:
            print(f"Telefone: {details['international_phone_number']}")

else:
    # Imprime uma mensagem de erro caso a requisição não tenha sido bem sucedida
    print('Erro ao acessar a API do Google Places: ', response.status_code)
