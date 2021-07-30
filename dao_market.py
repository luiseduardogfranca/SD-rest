class Market():

    def __init__(self):
        self.products = [
            {"code": "123", "name": "Margarina 200g", "price": 6.2, "quantity": 10},
            {"code": "122", "name": "Margarina 500g", "price": 12.2, "quantity": 30},
            {"code": "127", "name": "Cerveja 500ml", "price": 4, "quantity": 20},
            {"code": "124", "name": "Cerveja 1L", "price": 8, "quantity": 50},
            {"code": "121", "name": "Marcarrão", "price": 2.40, "quantity": 23},
            {"code": "126", "name": "Feijão carioquinha", "price": 6.89, "quantity": 40}]
    
    def get_product_by_code(self, code):
        return list(filter(lambda product: product["code"] == code, self.products))

    def get_amount_products_by_code(self, code):
        list_product = self.get_product_by_code(code)
        list_quantity = list(map(lambda product: product["quantity"], list_product))

        return sum(list_quantity)

    def add_product(self, product): 
        if ("code" in product and "name" in product and "price" in product and "quantity" in product):
            self.products.append(product)
            print(self.products)
            return True

        return False

    def update_product(self, newProduct):
        if ("code" in newProduct and "name" in newProduct and "price" in newProduct and "quantity" in newProduct):
            new_array = list(map(lambda product: newProduct if newProduct["code"] == product["code"] else product, self.products))
            self.products = new_array
            return True

        return False

    def remove_product(self, code): 
        new_product_arr = list(filter(lambda product: product["code"] != code, self.products))
        is_removed = True if len(new_product_arr) < len(self.products) else False
        self.products = new_product_arr

        return is_removed

    def get_all(self):
        return self.products