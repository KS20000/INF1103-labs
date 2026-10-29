class Product:
    """Represents one product in the inventory."""

    def __init__(self, product_id, name, price, stock):
        product_id = str(product_id).strip().upper()
        name = str(name).strip()

        if not product_id:
            raise ValueError("Product ID cannot be empty.")
        if not name:
            raise ValueError("Product name cannot be empty.")

        price = float(price)
        stock = int(stock)
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if stock < 0:
            raise ValueError("Stock cannot be negative.")

        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    @property
    def product_id(self):
        return self.__product_id

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def stock(self):
        return self.__stock

    def update_stock(self, quantity):
        """Set the stock to a non-negative whole number."""
        quantity = int(quantity)
        if quantity < 0:
            raise ValueError("Stock cannot be negative.")
        self.__stock = quantity

    def display_information(self):
        print(f"ID: {self.__product_id}")
        print(f"Name: {self.__name}")
        print(f"Price: ${self.__price:.2f}")
        print(f"Stock: {self.__stock}")

    def to_dict(self):
        """Convert to a JSON-friendly record for file storage."""
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Product from a saved JSON record."""
        return cls(data["id"], data["name"], data["price"], data["stock"])
