import os
import random

# Draw grid

# Pick random location for player

# Pick random location for exit door

# Pick random location for the monster

# Draw player in the grid

# Take input for movement

# Move play, unless invalid move (past edges of grid)

# Check for win/loss

# Clear screen and redraw gird

CELLS = [
    (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
    (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
    (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
    (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
    (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
]


def clear_screen():
    # run "cls" if on windows or "clear" if on mac or linux
    os.system("cls" if os.name == "nt" else "clear")


def get_locations():
    return random.sample(CELLS, 3)


def move_player(player, move):
    x, y = player
    if move == "LEFT":
        x -= 1
    if move == "RIGHT":
        x += 1
    if move == "UP":
        y -= 1
    if move == "DOWN":
        y += 1
    return x, y


def get_moves(player):
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]
    x, y = player
    if x == 0:
        moves.remove("LEFT")
    if x == 4:
        moves.remove("RIGHT")
    if y == 0:
        moves.remove("UP")
    if y == 4:
        moves.remove("DOWN")
    return moves


def draw_map(player, door):
    print(" _" * 5)
    tile = "|{}"

    for cell in CELLS:
        x, y = cell
        if x < 4:
            line_end = ""
            if cell == player:
                output = tile.format("X")
            elif cell == door:
                output = tile.format("D")
            else:
                output = tile.format("_")
        else:
            line_end = "\n"
            if cell == player:
                output = tile.format("X|")
            elif cell == door:
                output = tile.format("D|")
            else:
                output = tile.format("_|")
        print(output, end=line_end)


def game_loop():
    monster, door, player = get_locations()
    playing = True

    while playing:
        clear_screen()
        draw_map(player, door)
        valid_moves = get_moves(player)
        print("You're currently in room {}".format(player))
        print("Monster in room {}".format(monster))
        print("You can move {}".format(", ".join(valid_moves)))
        print("Enter QUIT to quit")

        move = input("> ").upper()

        if move == "QUIT":
            print("See you next time")
            break
        if move in valid_moves:
            player = move_player(player, move)
            if player == door:
                print("Congratulations, You've escaped!")
                playing = False
            elif player == monster:
                print("Ooops, you ran into the monster, game over!")
                playing = False
        else:
            input("** You ran into a wall!, press ENTER to continue **")
    else:
        if input("Play again? [Y/N]").lower() != "n":
            game_loop()


clear_screen()
print("Welcome to the dungeon!")
input("Press ENTER to start!")
clear_screen()
game_loop()

