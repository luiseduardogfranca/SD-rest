# Trabalho SD - API Rest

### Descrição

##### Uma empresa fornece uma API para gerênciamento e listagem de produtos

A API consiste em uma interface de comunicação utilizado os métodos HTTP, que são:

- GET -> Para ler um ou mais itens
- POST -> Para adicionar um item
- DELETE -> Para remover o item

Enquanto o lado cliente utiliza a biblioteca requests para executar as requisições de acordo com os métodos expostos na API (GET, POST e DELETE).

### Pré-requisitos

- python3
- flask (API)
- requests (client)

### Como executar?

O projeto está dividido em dois arquivos, que são: _market_controller.py_ e _dao_market.py_.

- market_controller.py: contém a implementação para a leitura das requests vindo do client e o processamento dos dados com a classe de acesso a dados contida no arquivo dao_market.py através dos métodos HTTP citados acima. Esse arquivo vai ser o intermédio entre o cliente e a classe responsável pela manipulação dos dados

- dao_market.py: contém a gerência dos dados bem como a inicialização do array de dados simulando uma lista de produtos fazendo a gerêcia dos mesmmos.

- client.py: contém toda a interface de comunicação com a API de gerênciamento de produtos através de requests HTTP. Neste arquivo possui um menu com as funções de leitura, cadastro e remoção.

Dado a explicação acima de cada arquivo, podemos passar para o passo a passo de execução do projeto.

#### Passos

Considerando que você já esteja dentro do folder do projeto e que as depedências já tenham sido instaladas no seu computador.

1. Abra um terminal à parte e execute o seguinte comando para deixar a API em execução:

```bash
python3 market_controller.py

```

Caso ainda não tenha instalado o **Flask**, basta executar o seguinte comando:

```bash
pip3 install flask
```

2. Abra um outro terminal para executar o lado cliente e assim simular todas as funcionalidades através das requests. Execute o seguinte comando:

```bash
python3 client.py

```
Caso ainda não tenha instalado a lib **requests**, basta executar o seguinte comando:

```bash
pip3 install requests
```

### Rotas

Com o projeto em execução, caso não queira executar o cliente, você pode acessar a API com o software Curl, que simula as requisições HTTP, basta executar os seguintes comandos com os devidos parâmetros no terminal de acordo com cada rota:

- Para ler os produtos:

  curl -i http://localhost:5000/produtos

- Para adicionar algum produto

  curl -i -X POST http://localhost:5000/produtos/[strinng:codeProduto]

- Para adicionar produto
  curl -i -H "Content-Type: application/json" -X POST -d '{"code":"223","name": "Sushi", "price": 2.40, "quantity":1}' http://localhost:5000/produtos

- Para remover algum produto pelo código

  curl -i -X DELETE http://localhost:5000/produtos/[strinng:codeProduto]

### Equipe:

- Luís Eduardo Gomes França
