# Ex 1 Player ##################################################################

import random

player = {
    'gold': 21,
    'inventory': {
        'sword': 1,
        'apple': 3
    }
}

def print_player(player):
    print('* Player')
    inventory_entries = []
    for item_name, item_qty in player['inventory'].items():
        inventory_entries.append(f"{item_name} x{item_qty}")

    print('  Gold: ' + str(player['gold']) + '$')
    print('  Inventory:', inventory_entries)


# Ex 2 Shop ####################################################################

shop = {
    'stock': {
        'shield': 3,
        'special sword': 2,
        'apple': 10,
        'wood log': 99,
    },
    'prices': {
        'shield': 100,
        'special sword': 500,
        'apple': 2,
        'wood log': 1,
    }
}

# Ex 3 Menu ####################################################################

def menu(options, title):
    print(title)
    print('*' * len(title))

    i = 0
    for o in options:
        print(f' > {i}. {o}')
        i += 1

    selection = -1
    while selection < 0 or selection >= len(options):
        selection = input("Introduce an option: ")
        selection = int(selection)
    return selection


def buy_menu(player, shop):
    while True:
        shop_items = []
        for item_name in shop['stock']:
            price = shop['prices'][item_name]
            qty = shop['stock'][item_name]
            shop_items.append(f'{item_name} - {price}$ - x{qty}')

        sel = menu(shop_items + ['Back'], "Buying")
        if sel == len(shop_items):
            break

        item = list(shop['stock'])[sel]
        if not buy(player, shop, item):
            print("You cannot buy " + item)
        else:
            print_player(player)


def sell_menu(player, shop):
    while True:
        inventory_items = list(player['inventory'])

        menu_entries = []
        for item in inventory_items:
            qty = player['inventory'][item]
            menu_entries.append(f'{item.capitalize()} x{qty}')

        sel = menu(menu_entries + ['Back'], title='What do you want to sell?')
        if sel == len(inventory_items):
            break # back
        else:
            if not sell(player, shop, inventory_items[sel]):
                print("* You cannot sell a " + inventory_items[sel])

            print_player(player)


# Ex4 Buy Logic ################################################################

def buy(player, shop, item_name):
    if player['gold'] < shop['prices'][item_name]:
        return False
    elif shop['stock'][item_name] <= 0:
        return False
    else:
        player['gold'] -= shop['prices'][item_name]

        if item_name in player['inventory']:
            player['inventory'][item_name] += 1
        else:
            player['inventory'][item_name] = 1

        shop['stock'][item_name] -= 1

        return True


# Ex5 Sell Logic ###############################################################

def sell(player, shop, item_name):
    if player['inventory'][item_name] <= 0 or item_name not in shop['prices']:
        return False
    else:
        player['gold'] += shop['prices'][item_name] // 2
        player['inventory'][item_name] -= 1
        shop['stock'][item_name] += 1
        if player['inventory'][item_name] == 0:
            del player['inventory'][item_name]

        return True


def main():
    print_player(player)

    while True:
        sel = menu(['Buy', 'Sell', 'Exit'], title='Shop Welcome')
        if sel == 0:
            buy_menu(player, shop)
        elif sel == 1:
            sell_menu(player, shop)
        else:
            print('Goodbye!!')
            break


if __name__ == "__main__":
    main()