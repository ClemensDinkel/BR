def random_id():
    import random
    cr_id = random.randint(0, 9)
    if cr_id >= 7:
        identity = "Replikant"
    else:
        identity = "Mensch"
    return identity


def add_player(name):
    from listen import locations
    import random

    random_number = random.randint(1, 5)
    player_loc = locations[random_number]
    identity = random_id()
    print(f"{name} ist ein {identity} und wohnt in {player_loc}")


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


def random_pc_livingloc_even(iterations):
    import random
    from listen import locations

    loc_list = list(locations)
    del loc_list[0]
    del loc_list[5:]
    tuple(loc_list)
    loc_list_editable = list(loc_list)
    random_pc_livingloc_return_list = []

    while iterations > 0:
        if len(loc_list_editable) != 0:
            available_locs = len(loc_list_editable)
            random_number = random.randint(0, available_locs - 1)
            pc_loc = loc_list_editable[random_number]
            random_pc_livingloc_return_list.append(pc_loc)
            loc_list_editable.pop(random_number)
            iterations -= 1
        else:
            loc_list_editable = list(loc_list)
    return random_pc_livingloc_return_list


def npc_disappears():
    import random
    from listen import locations
    npc_loc = locations[random.randint(0, 5)]
    return npc_loc
