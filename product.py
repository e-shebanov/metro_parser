class Product:
    def __init__(self, product_id, name, url, regular_price, promo_price, brand):
        self.product_id = product_id
        self.name = name
        self.url = url
        self.regular_price = regular_price
        self.promo_price = promo_price
        self.brand = brand

    def __str__(self):
        return f"Product ID: {self.product_id}\n" \
               f"Name: {self.name}\n" \
               f"URL: {self.url}\n" \
               f"Regular Price: {self.regular_price}\n" \
               f"Promo Price: {self.promo_price}\n" \
               f"Brand: {self.brand}"