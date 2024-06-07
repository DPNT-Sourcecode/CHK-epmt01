

# noinspection PyUnusedLocal
# skus = unicode string

PRODUCTS = {
    "A": {
        'price': 50,
        'special': [3, 130]
    },
    "B": {
        'price': 30,
        'special': [2, 45]
    },
    "C": {
        'price': 20,
        'special': None
    },
    "D": {
        'price': 15,
        'special': None
    }
}

def checkout(skus: str) -> int:
    """Returns an integer sum of the skus in the basket."""
    value = 0

    for sku in skus:
        product = PRODUCTS.get(sku)
        breakpoint()

        


    return value

checkout(skus='A, B, C')


