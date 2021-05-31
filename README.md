# Trabalho SD - API Rest

### Descrição

##### Uma empresa fornece uma API para gerênciamento e listagem de produtos

A API consiste em uma interface de comunicação utilizado os métodos HTTP, que são:

- GET -> Para ler um ou mais itens
- POST -> Para adicionar um item
- DELETE -> Para remover o item

### Pré-requisitos

- Python3
- Flask

### Como executar?

O projeto está dividido em dois arquivos, que são: _market_controller.py_ e _dao_market.py_.

- market_controller.py: contém a implementação para a leitura das requests vindo do client e o processamento dos dados com a classe de acesso a dados contida no arquivo dao_market.py através dos métodos HTTP citados acima. Esse arquivo vai ser o intermédio entre o cliente e a classe responsável pela manipulação dos dados

- dao_market.py: contém a gerência dos dados bem como a inicialização do array de dados simulando uma lista de produtos fazendo a gerêcia dos mesmmos.

Dado a explicação acima de cada arquivo, podemos passar para o passo a passo de execução do projeto.

#### Passos

Considerando que você já esteja dentro do folder do projeto e que as depedências já tenham sido instaladas no seu computador.

1. Abra o terminal e execute o seguinte comando:

```bash
python3 market_controller.py

```

Caso ainda não tenha instalado o Flask, basta executar o seguinte comando:

```bash
pip3 install flask
```

### Rotas

Com o projeto em execução, para acessar a API basta executar os seguintes comandos com os devidos parâmetros no terminal:

- Para ler os produtos:

  curl -i http://localhost:5000/produtos

### Equipe:

- Luís Eduardo Gomes França
