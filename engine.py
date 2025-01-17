import ObjectGenerator
import util
import time
import ui

CURRENT_ENEMY = {}


def create_board(width, height, hause=False):
    board = []
    for i in range(width):
        board.append([])
        for j in range(height):
            board[i].append(ObjectGenerator.spawn_floor())
    for i in range(1,29):
        board[0][i] = ObjectGenerator.spawn_wall_horizontal()
        board[19][i] = ObjectGenerator.spawn_wall_horizontal()
    for i in range(1,19):
         board[i][0] = ObjectGenerator.spawn_wall_upright()
         board[i][29] = ObjectGenerator.spawn_wall_upright()
    corners = ObjectGenerator.spawn_corners()
    board[0][0] = corners[0]
    board[0][29] = corners[1]
    board[19][0] = corners[2]
    board[19][29] = corners[3]
    if hause:
        board = create_house(board,18)
    return board

def create_house(board,place):
    house = ObjectGenerator.spawn_house()
    floor = False
    for i in range(8):
        if floor == False:
            board[place][place+i] = house[7]
            floor = True
        else:
            board[place][place+i] = house[8]
            floor = False
    board[place-1][19] = house[5]
    board[place-1][20] = house[6]
    board[place-1][21] = house[6]
    board[place-1][22] = house[4]
    board[place-1][23] = house[6]
    board[place-1][24] = house[5]
    board[place-2][20] = house[1]
    board[place-2][21] = house[2]
    board[place-2][22] = house[3]
    board[place-2][23] = house[2]
    board[place-3][21] = house[5]
    board[place-3][22] = house[5]
    return board




def put_player_on_board(board, player):
    '''
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''
    board[player["Ypoz"]][player["Xpoz"]] = player

def create_player():
    type = 0
    while True:
        print('\nAnd this is a beginning of your adventure!')
        print(""" \nCHOOSE YOUR CHARACTER: \n""")
        if type == 0:
            character_type = ObjectGenerator.labrador_character()
        elif type == 1:
            character_type = ObjectGenerator.shiba_character()
        elif type == 2:
            character_type = ObjectGenerator.doberman_character()
        elif type == 3:
            character_type = ObjectGenerator.mops_character()
        print(create_character_class_as_table(character_type))
        print("""
Press [e] choose this character
Press [d] next character
Press [a] previous character\n""")
        user_input = util.key_pressed().lower()
        if user_input == 'e':
            player_input = input("Put name of your character: ")
            character_type["Name"] = player_input
            util.clear_screen()
            return character_type
        elif user_input == 'd':
            type += 1
            if type < 4:
                util.clear_screen()
                continue
            else:
                type = 0
                util.clear_screen()
                continue
        elif user_input == "a":
            type -= 1
            if type >= 0:
                util.clear_screen()
                continue
            else:
                type = 3
                util.clear_screen()
                continue
        else:
            util.clear_screen()
            # print("Invalid type\n")
            # time.sleep(1)
            # util.clear_screen()
            continue

def create_character_class_as_table(character_type):
    statistics = dict()
    table = ""
    for element in character_type:
        if len(statistics) > 5:
            break
        if element != "Name":
            statistics[element] = character_type[element]
    table += f"{character_type['Name'].upper()}\n"
    outside_edges1 = 14*"═"
    outside_edges2 = 8*"═"
    table += f"╔{outside_edges1}╦{outside_edges2}╗"
    for i in statistics.items():
        space_before_values = 8 - len(str(i[1]))
        space_after_key = 14 - len(i[0])
        table += f"\n║{i[0]}{' '*space_after_key}║{' '*space_before_values}{str(i[1])}║"
    table += f"\n╚{outside_edges1}╩{outside_edges2}╝"
    return table


def display_statistics(player):
    HEADERS = f"""
╔══════════╦══════════╦══════════╦══════════╗
║Name      ║HP        ║Level     ║Experience║
╠══════════╬══════════╬══════════╬══════════╣ \n"""
    table = ""
    table += HEADERS
    for element in player:
        if element == "Name":
            spaces = 10 - len(player[element])
            table += f"║{player[element]}{' '*spaces}║"
        elif element == "HP":
            spaces = 10 - len(str(player[element]))
            table += f"{player[element]}{' '*spaces}"
        elif element == "Level":
            spaces = 10 - len(str(player[element]))
            table += f"║{player[element]}{' '*spaces}"
        elif element == "Experience":
            spaces = 10 - len(str(player[element]))
            table += f"║{player[element]}{' '*spaces}║"
    table += f"\n╚{10*'═'}╩{10*'═'}╩{10*'═'}╩{10*'═'}╝"
    return table

def display_current_enemy():
    if CURRENT_ENEMY == {}:
        table = "\n\n\n\n\n"
    else:
        HEADERS = f"""
╔══════════╦══════════╦══════════╦══════════╗
║Name      ║HP        ║Level     ║XP Reward ║
╠══════════╬══════════╬══════════╬══════════╣ \n"""
        table = ""
        table += HEADERS
        for element in CURRENT_ENEMY:
            if element == "Name":
                spaces = 10 - len(CURRENT_ENEMY[element])
                table += f"║{CURRENT_ENEMY[element]}{' '*spaces}║"
            elif element == "HP":
                spaces = 10 - len(str(CURRENT_ENEMY[element]))
                table += f"{CURRENT_ENEMY[element]}{' '*spaces}"
            elif element == "Level":
                spaces = 10 - len(str(CURRENT_ENEMY[element]))
                table += f"║{CURRENT_ENEMY[element]}{' '*spaces}"
            elif element == "XpReward":
                spaces = 10 - len(str(CURRENT_ENEMY[element]))
                table += f"║{CURRENT_ENEMY[element]}{' '*spaces}║"
        table += f"\n╚{10*'═'}╩{10*'═'}╩{10*'═'}╩{10*'═'}╝"
    return table
    

def display_end_screen(player, win=False):
    counters = [util.Kill_count,util.Steps_count,util.Critical_hits]
    table = ""
    if not win:
        table += "YOU LOST THE GAME\nSTATISTICS\n"
    else:
        table += "YOU WON THE GAME\nSTATISTICS\n"
    table += "╔══════════╦══════════╗\n"
    for element in player:
        if element == "Name":
            spaces = 10 - len(str(player[element]))
            table += f"║Name{6*' '}║{player[element]}{' '*spaces}║\n"
            table += f"╠{10*'═'}╬{10*'═'}╣\n"
        elif element == "Level":
            spaces = 10 - len(str(player[element]))
            table += f"║Level{5*' '}║{player[element]}{' '*spaces}║\n"
            table += f"╠{10*'═'}╬{10*'═'}╣\n"
        elif element == "Experience":
            spaces = 10 - len(str(player[element]))
            table += f"║Experience║{player[element]}{' '*spaces}║\n"
            table += f"╠{10*'═'}╬{10*'═'}╣\n"
    for info in range(len(counters)):
        if info == 0:
            spaces = 10 - len(str(util.Kill_count))
            table += f"║Kills{5*' '}║{util.Kill_count}{' '*spaces}║\n"
            table += f"╠{10*'═'}╬{10*'═'}╣\n"
        elif info == 1:
            spaces = 10 - len(str(util.Steps_count))
            table += f"║Steps{5*' '}║{util.Steps_count}{' '*spaces}║\n"
            table += f"╠{10*'═'}╬{10*'═'}╣\n"
        else:
            spaces = 10 - len(str(util.Critical_hits))
            table += f"║Criticals{1*' '}║{util.Critical_hits}{' '*spaces}║\n"
    table += "╚══════════╩══════════╝"
    return table




