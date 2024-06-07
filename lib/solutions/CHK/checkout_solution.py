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
    try:
        if valid(skus):
            basket = special_items(skus=skus)
            value = basket['value']
            skus = dict(basket['simplified_basket'])

            for sku in skus:
                if product := PRODUCTS.get(sku):
                    value += product['price'] * skus[sku]
        else:
            value = -1
        return value

    except Exception:
       raise NotImplementedError()


def special_items(skus: str) -> dict[str: int]:
    """Deals with the special items in a basket.

    This removes all special items from the dictionary and exchanges 
    them for a basket value.
    
    Args:
        skus: string of skus in basket.

    Returns:
        A dict containing a simplified basket with all special items 
        accounted for and a value of the special items.
    """
    value = 0

    sku_list = skus.split(",")
    sku_list = [item.strip().upper() for item in sku_list]
    counted_sku_dict = Counter(sku_list)

    if sku_list[0] != '':
        for sku in counted_sku_dict:
            product = PRODUCTS.get(sku)

            if product['special'] != None and (counted_sku_dict[sku] >= product['special'][0]):
                value += product['special'][1] * int(counted_sku_dict[sku] / product['special'][0])
                counted_sku_dict[sku] = (counted_sku_dict[sku] % product['special'][0])

    return {
        "simplified_basket": counted_sku_dict,
        "value": value
    }

def valid(input):
    """Checks for valid inputs."""
    valid = False
    valid_charactars = set('abcdefghijklmnopqrstuvwxyz,ABCDEFGHIJKLMNOPQRSTUVWXYZ ')

    if isinstance(input, str):
        for char in input:
            if char in valid_charactars:
                valid = True
            else:
                valid = False
                break

    return valid






