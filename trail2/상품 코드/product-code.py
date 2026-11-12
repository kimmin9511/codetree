product_name, product_code = input().split()
product_code = int(product_code)


class store :
    def __init__(self, a = 'codetree', b = 50) :
        self.name = a
        self.code = b


product1 = store()
product2 = store(product_name, product_code)

print(f"product {product1.code} is {product1.name}")
print(f"product {product2.code} is {product2.name}")
