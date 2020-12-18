shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    menus.sort()
    orders.sort()
    order_index = 0
    while order_index <= len(orders)-1:
        if orders[order_index] == menus[0]:
            menus = menus[1:]
            order_index += 1
            continue
        else:
            menus = menus[1:]
            if len(menus) != 0:
                continue
            return "not_available"

    return "available"


result = is_available_to_order(shop_menus, shop_orders)
print(result)