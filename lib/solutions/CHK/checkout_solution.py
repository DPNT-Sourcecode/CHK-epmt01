

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
    },
}

def checkout(skus):
    raise NotImplementedError()

