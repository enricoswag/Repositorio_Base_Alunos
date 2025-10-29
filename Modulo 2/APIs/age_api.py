# importamos de bibliotecas
import requests

#definir o nome para consulta
nome = input('Digite o nome dessa pessoa: ').strip()

#url da api
url = f'https://api.agify.io?name={nome}'

# fazer a requisição
response = requests.get(url)
#processar a resposta
if response.status_code == 200:
    dados = response.json()
    print(f"Nome{dados['name']}")
    print(f"Idade estimada:{dados['age']} anos")
    print(f'Numero de registros analisando: {dados['count']}')
else:
    print(f"Erro ao acessar a API:{response.status_code}") 