shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    for order in orders:
        if order in menus:
            continue
        else:
            return "unavailable"
    return "available"


result = is_available_to_order(shop_menus, shop_orders)
print(result)