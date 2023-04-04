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
        name = result['name']
        place_id = result['place_id']
        address = result.get('formatted_address', '')
        
        # Faz uma nova requisição para obter mais detalhes do lugar
        details_url = f'https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=name,formatted_address,formatted_phone_number,website&key={api_key}'
        details_response = requests.get(details_url)
        
        if details_response.status_code == 200:
            # Analisa o JSON retornado pela requisição de detalhes
            details_data = details_response.json()
            
            # Obtém as informações de contato, se disponíveis
            phone_number = details_data.get('result', {}).get('formatted_phone_number', '')
            website = details_data.get('result', {}).get('website', '')
            
            # Exibe o nome, endereço e informações de contato do lugar
            print(f'Nome: {name}')
            print(f'Endereço: {address}')
            if phone_number:
                print(f'Telefone: {phone_number}')
            if website:
                print(f'Site: {website}')
            print('-' * 50)
        else:
            # Imprime uma mensagem de erro caso a requisição de detalhes não tenha sido bem sucedida
            print(f'Erro ao acessar a API do Google Places Details para o lugar {name}: {details_response.status_code}')
else:
    # Imprime uma mensagem de erro caso a requisição não tenha sido bem sucedida
    print('Erro ao acessar a API do Google Places: ', response.status_code)