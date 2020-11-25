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


player = {
    'gold': 21,
    'inventory': {
        'sword': 1,
        'apple': 3
    }
}


def save_player(player):
    player_save = "player\n"
    player_save += "gold," + str(player['gold']) + '\n'
    
    player_save += "\nplayer.inventory\n"
    for item, qty in player['inventory'].items():
        player_save += item + "," + str(qty) + "\n"

    return player_save


def save_shop(shop):
    shop_save = "shop.stock\n"
    for item, qty in shop['stock'].items():
        shop_save += item + "," + str(qty) + "\n"

    shop_save += "\nshop.prices\n"
    for item, qty in shop['prices'].items():
        shop_save += item + "," + str(qty) + "\n"

    return shop_save


def save_state(player, shop, fname):
    shop_str = save_shop(shop)
    player_str = save_player(player)
    with open(fname, 'w') as f:
        f.write(player_str)
        f.write("\n")
        f.write(shop_str)


def load_single_dict(f):
    line = f.readline().strip()
    new_dict = {}
    while line != "":
        key, value = line.split(',')
        new_dict[key] = int(value)
        line = f.readline().strip()

    return new_dict


def load_game_state(fname):
    player = {}
    shop = {}

    with open(fname) as f:
        line = f.readline().strip()

        while line != "":
            if line == 'player':
                player = load_single_dict(f)
            elif line == 'player.inventory':
                player['inventory'] = load_single_dict(f)
            elif line == 'shop.prices':
                shop['prices'] = load_single_dict(f)
            elif line == 'shop.stock':
                shop['stock'] = load_single_dict(f)

            line = f.readline().strip()

    return player, shop

save_state(player, shop, 'game.txt')
p, s = load_game_state('game.txt')
print(p)
print(s)