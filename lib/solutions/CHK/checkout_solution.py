from collections import Counter

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

    skus, value = special_items(skus=skus)

    
    for sku in skus:
        if product := PRODUCTS.get(sku):
            value = value + product['price']
    return value

def special_items(skus: str) -> dict[str: int]:
    """Deals with the special items in a basket.
    
    Args:
        skus: string of skus in basket.
    Returns:
        A dict containing a simplified basket with all special items 
        accounted for and a value of the special items.
    
    """

    # sku_list = skus.split(",")
    # sku_list = [item.strip() for item in sku_list]

    thing = Counter(skus)

    breakpoint()

checkout(skus='A, B, C, D, D, D')




