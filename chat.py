from senha import API_KEY
import requests
import json

headers = {"Authorization": f"Bearer {API_KEY}", "content-type": "application/json"}
#link = "https://api.openai.com/v1/models"
link = "https://api.openai.com/v1/chat/completions"
id_modelo = "gpt-3.5-turbo"

body = {
  "model": "gpt-3.5-turbo",
  "messages": [{"role": "user", "content": "me diga somente o comando em shell que desliga o sistema operacional win 10, sem explicar nada"}]
}
body = json.dumps(body)

requi = requests.post(link, headers = headers, data=body)
#print(requi)
resposta = requi.json()

mensagem = resposta["choices"][0]["message"]["content"]
print(mensagem)