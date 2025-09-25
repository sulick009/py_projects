from solver import do_moves
from cube_model import Cube_model


edges = {
    "wo" : 1,
    "wg" : 2,
    "wr" : 3,
    "wb" : 4,
    "gw" : 5,
    "go" : 6,
    "gr" : 7,
    "gy" : 8,
    "rw" : 9,
    "rg" : 10,
    "rb" : 11,
    "ry" : 12,
    "bw" : 13,
    "br" : 14,
    "bo" : 15,
    "by" : 16,
    "yr" : 17,
    "yg" : 18,
    "yb" : 19,
    "yo" : 20,
    "ow" : 21,
    "ob" : 22,
    "og" : 23,
    "oy" : 24,
    }

cube = Cube_model()

def find_white_edge(cube):
        for i in range(1, 5):
            if(cube.sides["w"][i * 2 - 1] == "w" and not is_edge_correct(cube, i)):
                return i
        for i in range(1, 5):
            if(cube.sides["g"][i * 2 - 1] == "w"):
                return i + 4
        for i in range(1, 5):
            if(cube.sides["r"][i * 2 - 1] == "w"):
                return i + 8
        for i in range(1, 5):
            if(cube.sides["b"][i * 2 - 1] == "w"):
                return i + 12
        for i in range(1, 5):
            if(cube.sides["y"][i * 2 - 1] == "w"):
                return i + 16
        for i in range(1, 5):
            if(cube.sides["o"][i * 2 - 1] == "w"):
                return i + 20
                
    

    

def is_edge_correct(cube, num_white_edge):
    next_edge_color = find_next_color_of_edge(cube, num_white_edge)
    if(next_edge_color == "o" and num_white_edge == 1):
        return True
    elif(next_edge_color == "g" and num_white_edge == 2):
        return True
    elif(next_edge_color == "b" and num_white_edge == 3):
        return True
    elif(next_edge_color == "r" and num_white_edge == 4):
        return True
    return False


def find_next_color_of_edge(cube, num_white_edge):
    if(num_white_edge == 1):
        return cube.sides["o"][1]
    elif(num_white_edge == 2):
        return cube.sides["g"][1]
    elif(num_white_edge == 3):
        return cube.sides["b"][1]
    elif(num_white_edge == 4):
        return cube.sides["r"][1]
    elif(num_white_edge == 5):
        return cube.sides["w"][3]
    elif(num_white_edge == 6):
        return cube.sides["o"][5]
    elif(num_white_edge == 7):
        return cube.sides["r"][3]
    elif(num_white_edge == 8):
        return cube.sides["y"][3]
    elif(num_white_edge == 9):
        return cube.sides["w"][7]
    elif(num_white_edge == 10):
        return cube.sides["g"][5]
    elif(num_white_edge == 11):
        return cube.sides["b"][3]
    elif(num_white_edge == 12):
        return cube.sides["y"][1]
    elif(num_white_edge == 13):
        return cube.sides["w"][5]
    elif(num_white_edge == 14):
        return cube.sides["r"][5]
    elif(num_white_edge == 15):
        return cube.sides["o"][3]
    elif(num_white_edge == 16):
        return cube.sides["y"][5]
    elif(num_white_edge == 17):
        return cube.sides["r"][7]
    elif(num_white_edge == 18):
        return cube.sides["g"][7]
    elif(num_white_edge == 19):
        return cube.sides["b"][7]
    elif(num_white_edge == 20):
        return cube.sides["o"][7]
    elif(num_white_edge == 21):
        return cube.sides["w"][1]
    elif(num_white_edge == 22):
        return cube.sides["b"][5]
    elif(num_white_edge == 23):
        return cube.sides["g"][3]
    elif(num_white_edge == 24):
        return cube.sides["y"][7]

do_moves("r2 l2 f2 b2 f2 l2 f r l d2 br f l fr r l f b l r l d b", cube)
print(find_white_edge(cube))
