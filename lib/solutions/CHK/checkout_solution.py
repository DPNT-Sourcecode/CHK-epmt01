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
    
    sku_list = clean(skus=skus)

    if len(sku_list) != 0:
        basket = special_items(sku_list=sku_list)
        value = basket['value']
        sku_dict = dict(basket['simplified_basket'])

        for sku in sku_dict:
            if product := PRODUCTS.get(sku):
                value += product['price'] * sku_dict[sku]
    elif skus == "":
        value = 0
    else:
        value = -1
    return value

def special_items(sku_list: list) -> dict[str: int]:
    """Deals with the special items in a basket.

    This removes all special items from the dictionary and exchanges 
    them for a basket value.
    
    Args:
        skus: list of skus in basket.

    Returns:
        A dict containing a simplified basket with all special items 
        accounted for and a value of the special items.
    """
    value = 0
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

def clean(skus: str) -> list:
    """Cleans the sku input string in the following ways.
    
        1. Checks the input is of string format.
        2. Returns an empty list if invalid charactars detected.
        3. Places sku string into a list and removes blank spaces and comma sperators.
        4. Removes all skus in the dictionary that do not appear in the product 
        table.

    Returns:
        A list of string items in the basket.
    """
    valid_charactars = set(',ABCDEFGHIJKLMNOPQRSTUVWXYZ ')
    
    if isinstance(skus, str):
        for char in skus:
            if char not in valid_charactars:
                cleaned_sku_list = []
                return cleaned_sku_list

        sku_string = skus.replace(",", "").replace(" ", "")
        sku_list = [item.strip() for item in sku_string]

        product_key_list = list(PRODUCTS.keys())
        cleaned_sku_list = []

        for sku in sku_list:
            if sku in product_key_list:
                cleaned_sku_list.append(sku)

    else:
        cleaned_sku_list = []

    return (cleaned_sku_list)