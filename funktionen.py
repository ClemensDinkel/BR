def random_race():
    import random
    cr_race = random.randint(0, 9)
    if cr_race >= 7:
        rasse = "Replikant"
    else:
        rasse = "Mensch"
    return rasse


def add_player(name):
    from listen import locations
    import random

    random_number = random.randint(1, 5)
    player_loc = locations[random_number]
    race = random_race()
    print(f"{name} ist ein {race} und wohnt in {player_loc}")


def create_players(player_count):
    import random
    from listen import locations

    player_loc_list = list(locations)
    del player_loc_list[0]
    del player_loc_list[5:]
    tuple(player_loc_list)
    player_loc_list_editable = list(player_loc_list)
    player_loc_return_list = []
    player_name_return_list = []
    spielernummer = 1

    while player_count > 0:
        if len(player_loc_list) != 0:
            player_name = input(f"Spieler {spielernummer}: ")
            player_name_return_list.append(player_name)
            available_locs = len(player_loc_list_editable)
            random_number = random.randint(0, available_locs - 1)
            pc_loc = player_loc_list_editable[random_number]
            player_loc_return_list.append(pc_loc)
            player_loc_list_editable.pop(random_number)
            player_count -= 1
            spielernummer += 1
        else:
            player_loc_list_editable = list(player_loc_list)

    return (player_name_return_list, player_loc_return_list)


def random_npc_loc(first_loc, last_loc):
    import random
    from listen import locations
    npc_loc = locations[random.randint(first_loc, last_loc)]
    return npc_loc


def random_npc_cityloc_even(iterations):
    import random
    from listen import locations

    loc_list = list(locations)
    del loc_list[0:6]
    del loc_list[5:]
    tuple(loc_list)
    loc_list_editable = list(loc_list)
    random_npc_cityloc_return_list = []

    while iterations > 0:
        if len(loc_list_editable) != 0:
            available_locs = len(loc_list_editable)
            random_number = random.randint(0, available_locs - 1)
            npc_loc = loc_list_editable[random_number]
            random_npc_cityloc_return_list.append(npc_loc)
            loc_list_editable.pop(random_number)
            iterations -= 1
        else:
            loc_list_editable = list(loc_list)
    return random_npc_cityloc_return_list


def npc_disappears():
    import random
    from listen import locations
    npc_loc = locations[random.randint(0, 5)]
    return npc_loc
