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
    basket = special_items(skus=skus)
    value = basket['value']
    breakpoint()
    skus = dict(basket['simplified_basket'])

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
    value = 0

    sku_list = skus.split(",")
    sku_list = [item.strip() for item in sku_list]
    counted_sku_dict = Counter(sku_list)

    for sku in counted_sku_dict:
        product = PRODUCTS.get(sku)

        if product['special'] != None and (counted_sku_dict[sku] >= product['special'][0]):
            value += product['special'][1] * int(counted_sku_dict[sku] / product['special'][0])
            counted_sku_dict[sku] = (counted_sku_dict[sku] % product['special'][0])

    return {
        "simplified_basket": counted_sku_dict,
        "value": value
    }


print(checkout(skus='A, A, A, A, A, A, B, C, D, D, D'))




