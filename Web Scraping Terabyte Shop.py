from bs4 import BeautifulSoup as soup
import requests

span = '</span>'
# Pagina guadada na variavel, a url pode ser modificada para qualquer departamento.
url = requests.get("https://www.terabyteshop.com.br/hardware/placas-de-video")

# Ver se a página foi baixada com sucesso(200 = baixada com sucesso)
# Se Começar com 4 ou 5 = erro ao baixar.
# print(url.status_code)

soup = soup(url.content, 'html.parser')

arquivo = "ProdutosFinal.csv"
f = open(arquivo, "w")
# Cria as legendas das colunas.
linhas = "Descrição; Preço\n"

f.write(linhas)


# Pega todos os produtos.
produtos = soup.find_all("div", {"class": "commerce_columns_item_caption"})

# Pega todos os preços.
precos = soup.find_all("div", {"class": "prod-new-price"})

# Passa por todos os produtos e preços e os escreve no arquivo .csv.
for produto, preco in zip(produtos, precos):
    descricao = produto.a["title"]
    vista = str(preco.span).strip(span)
    f.write(descricao + ';' + vista + "\n")

f.close()
