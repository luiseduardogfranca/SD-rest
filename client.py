import requests
from time import sleep 

class Client():
    def __init__(self):
        self.HOST="127.0.0.1"
        self.PORT=5000
    
    def print_product(self, product):
        if ('code' in product and 'name' in product and 'price' in product and 'quantity' in product):
            print(f"Cód.: {product['code']} \tNome: {product['name']} \tPreço: {product['price']} \tQuantitdade: {product['quantity']}")

    def get_products(self):
        res = requests.get(f"http://{self.HOST}:{self.PORT}/produtos")
        list(map(lambda product: self.print_product(product), res.json()))

    def create_product(self, code, name, price, quantity):
        product = {
            "code": code,
            "name": name,
            "price": price,
            "quantity": quantity
        }
        
        res = requests.post(f"http://{self.HOST}:{self.PORT}/produtos", json=product)
        
        if (res.status_code == 400 or res.status_code == 500):
            print("\n>>> Erro ao cadastrar")
        
        elif (res.status_code == 201 and res.json()):
            print("\n>>> Produto criado!\n")
            self.print_product(res.json())
            print("\n>>> ===============")

    def remove_product(self, code):
        res = requests.delete(f"http://{self.HOST}:{self.PORT}/produtos/{code}")

        if (res.status_code == 404 or res.status_code == 500):
            print("\n>>> Erro ao remover ou produto não encontrado")
        
        elif (res.status_code == 200):
            print("\n>>> Produto removido!\n")
            print("Lista de produtos atualizada\n")
            self.get_products()
            print("\n>>> ===============")


client = Client()

print("<<<   Iniciando conexão com a central de produtos  >>>")
print("Conectando a central da empresa. Para sair digite 0.\n")

msg_code = input("Funções disponíveis: \n\n\t1 - Listar todos os produtos \n\t2 - Cadastrar produto \n\t3 - Remover produto \n\t0 - Encerrar programa \n>>> ")

while msg_code != "0":
    if msg_code == "1":
        print(">>> \nListando produtos...\n")
        client.get_products()
    
    elif msg_code == "2":
        print(">>> \nForneça os dados do produto\n")
        
        code = input("Código: ")
        name = input("Nome: ")
        price = input("Preço: ")
        quantity = input("Quantidade: ")

        client.create_product(code, name, price, quantity)

    elif msg_code == "3":
        print(">>> \nForneça o código do produto a ser removido")
        code = input("Código: ")

        client.remove_product(code)
    
    msg_code = input("\n\nFunções disponíveis: \n\n\t1 - Listar todos os produtos \n\t2 - Cadastrar produto \n\t3 - Remover produto \n\t0 - Encerrar programa \n>>> ")

