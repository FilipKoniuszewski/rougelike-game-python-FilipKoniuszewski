import util
import engine
import ui
import ObjectGenerator
import random
import time


PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20


def main():
    # player = create_player()
    # board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)

    # util.clear_screen()
    # is_running = True
    # while is_running:
    #     engine.put_player_on_board(board, player)
    #     ui.display_board(board)

    #     key = util.key_pressed()
    #     if key == 'q':
    #         is_running = False
    #     else:
    #         pass
    #     util.clear_screen()

    board = engine.create_board(20,30)
    player = engine.create_player()
    engine.put_player_on_board(board, player)
    # engine.put_player_on_board(board, ObjectGenerator.spawn_dogge(5,3))
    list_of_enemies = []
    add_enemies(board, 3, list_of_enemies)
    while True:
        util.clear_screen()
        print(engine.display_statistics(player))
        ui.display_board(board)
        success = False
        while not success:
            success = move_player(board, player)
        enemy_activity(board, list_of_enemies)
        


def add_enemies(board, amount, list_of_enemies):
    for i in range(amount):
        temp = ObjectGenerator.spawn_dogge(random.randint(3,15),random.randint(3,15))
        engine.put_player_on_board(board, temp)
        list_of_enemies.append(temp)


def enemy_activity(board, list_of_enemies):
    for enemy in list_of_enemies:
        success = False
        while not success:
            x = random.randint(0, 4)
            if x == 0:
                if enemy["Ypoz"] - 1 >= 0 and board[enemy["Ypoz"] - 1][enemy["Xpoz"]]["Walkable"]:
                    board[enemy["Ypoz"] - 1][enemy["Xpoz"]] = enemy
                    board[enemy["Ypoz"]][enemy["Xpoz"]] = ObjectGenerator.spawn_floor()
                    enemy["Ypoz"] -= 1
                    success = True
            elif x == 1:
                if enemy["Ypoz"] < len(board) - 1 and board[enemy["Ypoz"] + 1][enemy["Xpoz"]]["Walkable"]:
                    board[enemy["Ypoz"] + 1][enemy["Xpoz"]] = enemy
                    board[enemy["Ypoz"]][enemy["Xpoz"]] = ObjectGenerator.spawn_floor()
                    enemy["Ypoz"] += 1
                    success = True
            elif x == 2:
                if enemy["Xpoz"] < len(board[0]) - 1 and board[enemy["Ypoz"]][enemy["Xpoz"] + 1]["Walkable"]:
                    board[enemy["Ypoz"]][enemy["Xpoz"] + 1] = enemy
                    board[enemy["Ypoz"]][enemy["Xpoz"]] = ObjectGenerator.spawn_floor()
                    enemy["Xpoz"] += 1
                    success = True
            elif x == 3:
                if enemy["Xpoz"] - 1 >= 0 and board[enemy["Ypoz"]][enemy["Xpoz"] - 1]["Walkable"]:
                    board[enemy["Ypoz"]][enemy["Xpoz"] - 1] = enemy
                    board[enemy["Ypoz"]][enemy["Xpoz"]] = ObjectGenerator.spawn_floor()
                    enemy["Xpoz"] -= 1
                    success = True


def move_player(board, player):
    pressed_key = util.key_pressed()
    if pressed_key == "w":
        if player["Ypoz"] - 1 >= 0:
            if board[player["Ypoz"] - 1][player["Xpoz"]]["Walkable"]:
                board[player["Ypoz"] - 1][player["Xpoz"]] = player
                board[player["Ypoz"]][player["Xpoz"]] = ObjectGenerator.spawn_floor()
                player["Ypoz"] -= 1
            elif board[player["Ypoz"] - 1][player["Xpoz"]]["Type"] == "Enemy":
                input("attack")
            else:
                return False
        else:
            return False
    elif pressed_key == "s":
        if player["Ypoz"] < len(board) - 1:
            if board[player["Ypoz"] + 1][player["Xpoz"]]["Walkable"]:
                board[player["Ypoz"] + 1][player["Xpoz"]] = player
                board[player["Ypoz"]][player["Xpoz"]] = ObjectGenerator.spawn_floor()
                player["Ypoz"] += 1
            elif board[player["Ypoz"] + 1][player["Xpoz"]]["Type"] == "Enemy":
                input("attack")
            else:
                return False
        else:
            return False
    elif pressed_key == "d":
        if player["Xpoz"] < len(board[0]) - 1:
            if board[player["Ypoz"]][player["Xpoz"] + 1]["Walkable"]:
                board[player["Ypoz"]][player["Xpoz"] + 1] = player
                board[player["Ypoz"]][player["Xpoz"]] = ObjectGenerator.spawn_floor()
                player["Xpoz"] += 1
            elif board[player["Ypoz"]][player["Xpoz"] + 1]["Type"] == "Enemy":
                input("attack")
            else:
                return False
        else:
            return False
    elif pressed_key == "a":
        if player["Xpoz"] - 1 >= 0:
            if board[player["Ypoz"]][player["Xpoz"] - 1]["Walkable"]:
                board[player["Ypoz"]][player["Xpoz"] - 1] = player
                board[player["Ypoz"]][player["Xpoz"]] = ObjectGenerator.spawn_floor()
                player["Xpoz"] -= 1
            elif board[player["Ypoz"]][player["Xpoz"] - 1]["Type"] == "Enemy":
                input("attack")
            else:
                return False
        else:
            return False
    else:
        return False
    return True




if __name__ == '__main__':
    main()
