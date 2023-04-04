from senhagoogle import API_KEY
import requests
import json
import time

# Chave de API do Google Places
api_key = API_KEY  # Substitua pela sua chave de API do Google Places

# Palavra-chave que você deseja pesquisar
keyword = 'imobiliaria'  # Substitua pela palavra-chave desejada

# Localização que você deseja pesquisar (no exemplo, Brasília, DF)
location = '-15.644213346051028, -47.829548118720055'  # Substitua pela localização desejada


# URL da API do Google Places para pesquisa de empresas
url = f'https://maps.googleapis.com/maps/api/place/textsearch/json?query={keyword}&location={location}&radius=5000&key={api_key}'

# Lista para armazenar todas as empresas encontradas
results = []

# Faz uma requisição GET para a URL e armazena a resposta
response = requests.get(url)

# Verifica se a requisição foi bem sucedida
if response.status_code == 200:

    # Analisa o JSON retornado usando a biblioteca json
    data = response.json()

    # Adiciona os resultados encontrados na lista
    results.extend(data['results'])

    # Enquanto houverem mais páginas a serem consultadas, faz uma nova requisição
    while 'next_page_token' in data:

        # Espera um tempo para evitar atingir a taxa limite da API
        time.sleep(2)

        # Consulta a próxima página passando o token retornado no campo 'next_page_token'
        next_page_token = data['next_page_token']
        next_url = f'https://maps.googleapis.com/maps/api/place/textsearch/json?query={keyword}&location={location}&radius=5000&key={api_key}&pagetoken={next_page_token}'
        next_response = requests.get(next_url)

        # Adiciona os resultados encontrados na lista
        next_data = next_response.json()
        results.extend(next_data['results'])

        # Atualiza a variável 'data' com a nova resposta
        data = next_data

    # Imprime o nome e as informações de contato (se disponíveis) de todas as empresas encontradas
    for i, result in enumerate(results):
        name = result['name']
        address = result.get('formatted_address', 'N/A')
        phone_number = result.get('formatted_phone_number', 'N/A')
        website = result.get('website', 'N/A')

        print(f'{i+1}. Nome: {name}')
        print(f'   Endereço: {address}')

        if phone_number != 'N/A':
            print(f'   Telefone: {phone_number}')
        if website != 'N/A':
            print(f'   Website: {website}')

        print()

else:
    # Imprime uma mensagem de erro caso a requisição não tenha sido bem sucedida
    print('Erro ao acessar a API do Google Places: ', response.status_code)