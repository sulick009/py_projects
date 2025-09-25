from solver import do_moves
from cube_model import Cube_model
from pprint import pprint


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

def solve_cross(cube):
    while not is_cross_solved(cube):
        num_of_edge = find_white_edge(cube)
        curr_edge = {num_of_edge: find_next_color_of_edge(cube, num_of_edge)}

        if curr_edge[num_of_edge] == "g":
            move_edge(num_of_edge, 2)
        elif curr_edge[num_of_edge] == "r":
            move_edge(num_of_edge, 4)
        elif curr_edge[num_of_edge] == "b":
            move_edge(num_of_edge, 3)
        elif curr_edge[num_of_edge] == "o":
            move_edge(num_of_edge, 1)

def is_cross_solved(cube):
    if(cube.sides["w"][1] == "w" and cube.sides["o"][1] == "o" 
       and cube.sides["w"][3] == "w" and cube.sides["g"][1] == "g"
       and cube.sides["w"][5] == "w" and cube.sides["b"][1] == "b"
       and cube.sides["w"][7] == "w" and cube.sides["r"][1] == "r"):
        return True
    return False


def move_edge(start_pos, target):
    if(target == 4):
        if(start_pos == 1):
            do_moves("b u2 br u2", cube)
        elif(start_pos == 2):
            do_moves("l u lr ur", cube)
        elif(start_pos == 3):
            do_moves("r ur rr u", cube)
        elif(start_pos == 4):
            return
        elif(start_pos == 5):
            do_moves("l f", cube)
        elif(start_pos == 6):
            do_moves("l2 f", cube)
        elif(start_pos == 7):
            do_moves("f", cube)
        elif(start_pos == 8):
            do_moves("lr f", cube)
        elif(start_pos == 9):
            do_moves("f ur r u", cube)
        elif(start_pos == 10):
            do_moves("u lr u", cube)
        elif(start_pos == 11):
            do_moves("u r ur", cube)
        elif(start_pos == 12):
            do_moves("fr u r ur", cube)
        elif(start_pos == 13):
            do_moves("rr fr", cube)
        elif(start_pos == 14):
            do_moves("fr", cube)
        elif(start_pos == 15):
            do_moves("r2 fr", cube)
        elif(start_pos == 16):
            do_moves("r fr", cube)
        elif(start_pos == 17):
            do_moves("f2", cube)
        elif(start_pos == 18):
            do_moves("d f2", cube)
        elif(start_pos == 19):
            do_moves("dr f2", cube)
        elif(start_pos == 20):
            do_moves("d2 f2", cube)
        elif(start_pos == 21):
            do_moves("br ur rr u", cube)
        elif(start_pos == 22):
            do_moves("ur rr u", cube)
        elif(start_pos == 23):
            do_moves("b2 ur rr u", cube)
        elif(start_pos == 24):
            do_moves("b ur rr u", cube)
    elif(target == 2):
        if(start_pos == 1):
            do_moves("ur l u lr", cube)
        elif(start_pos == 2):
            return
        elif(start_pos == 3):
            do_moves("r u2 rr u2", cube)
        elif(start_pos == 4):
            do_moves("fr u f ur", cube)
        elif(start_pos == 5):
            do_moves("l ur f u", cube)
        elif(start_pos == 6):
            do_moves("u br ur", cube)
        elif(start_pos == 7):
            do_moves("ur f u", cube)
        elif(start_pos == 8):
            do_moves("d f lr fr", cube)
        elif(start_pos == 9):
            do_moves("fr lr", cube)
        elif(start_pos == 10):
            do_moves("lr", cube)
        elif(start_pos == 11):
            do_moves("f2 lr f2", cube)
        elif(start_pos == 12):
            do_moves("f lr fr", cube)
        elif(start_pos == 13):
            do_moves("r u b ur", cube)
        elif(start_pos == 14):
            do_moves("r2 u b ur r2", cube)
        elif(start_pos == 15):
            do_moves("u b ur", cube)
        elif(start_pos == 16):
            do_moves("rr u b ur r", cube)
        elif(start_pos == 17):
            do_moves("dr l2", cube)
        elif(start_pos == 18):
            do_moves("l2", cube)
        elif(start_pos == 19):
            do_moves("d2 l2", cube)
        elif(start_pos == 20):
            do_moves("d l2", cube)
        elif(start_pos == 21):
            do_moves("b l", cube)
        elif(start_pos == 22):
            do_moves("b2 l", cube)
        elif(start_pos == 23):
            do_moves("l", cube)
        elif(start_pos == 24):
            do_moves("br l", cube)
    elif(target == 3):
        if(start_pos == 1):
            do_moves("u rr ur r", cube)
        elif(start_pos == 2):
            do_moves("l u2 lr u2", cube)
        elif(start_pos == 3):
            return
        elif(start_pos == 4):
            do_moves("f u fr ur", cube)
        elif(start_pos == 5):
            do_moves("l u f ur", cube)
        elif(start_pos == 6):
            do_moves("ur br u", cube)
        elif(start_pos == 7):
            do_moves("u f ur", cube)
        elif(start_pos == 8):
            do_moves("d fr r f", cube)
        elif(start_pos == 9):
            do_moves("f r", cube)
        elif(start_pos == 10):
            do_moves("f2 r f2", cube)
        elif(start_pos == 11):
            do_moves("r", cube)
        elif(start_pos == 12):
            do_moves("fr r f", cube)
        elif(start_pos == 13):
            do_moves("rr u fr ur", cube)
        elif(start_pos == 14):
            do_moves("u fr ur", cube)
        elif(start_pos == 15):
            do_moves("rr u fr ur", cube)
        elif(start_pos == 16):
            do_moves("dr fr r f", cube)
        elif(start_pos == 17):
            do_moves("d r2", cube)
        elif(start_pos == 18):
            do_moves("d2 r2", cube)
        elif(start_pos == 19):
            do_moves("r2", cube)
        elif(start_pos == 20):
            do_moves("dr r2", cube)
        elif(start_pos == 21):
            do_moves("br rr", cube)
        elif(start_pos == 22):
            do_moves("rr", cube)
        elif(start_pos == 23):
            do_moves("b2 rr b2", cube)
        elif(start_pos == 24):
            do_moves("b rr br", cube)
    elif(target == 1):
        if(start_pos == 1):
            return
        elif(start_pos == 2):
            do_moves("l ur lr u", cube)
        elif(start_pos == 3):
            do_moves("r u rr ur", cube)
        elif(start_pos == 4):
            do_moves("f u2 fr u2", cube)
        elif(start_pos == 5):
            do_moves("lr br", cube)
        elif(start_pos == 6):
            do_moves("br", cube)
        elif(start_pos == 7):
            do_moves("l2 br l2", cube)
        elif(start_pos == 8):
            do_moves("l br lr", cube)
        elif(start_pos == 9):
            do_moves("f u r ur", cube)
        elif(start_pos == 10):
            do_moves("ur lr u", cube)
        elif(start_pos == 11):
            do_moves("u r ur", cube)
        elif(start_pos == 12):
            do_moves("d rr b r", cube)
        elif(start_pos == 13):
            do_moves("r b", cube)
        elif(start_pos == 14):
            do_moves("r2 b r2", cube)
        elif(start_pos == 15):
            do_moves("b", cube)
        elif(start_pos == 16):
            do_moves("rr b r", cube)
        elif(start_pos == 17):
            do_moves("d2 b2", cube)
        elif(start_pos == 18):
            do_moves("dr b2", cube)
        elif(start_pos == 19):
            do_moves("d b2", cube)
        elif(start_pos == 20):
            do_moves("b2", cube)
        elif(start_pos == 21):
            do_moves("b ur l u", cube)
        elif(start_pos == 22):
            do_moves("u rr ur", cube)
        elif(start_pos == 23):
            do_moves("ur l u", cube)
        elif(start_pos == 24):
            do_moves("b u rr ur", cube)

do_moves("B2 D2 B2 U L2 F2 D L2 F2 D' U F2 L' F L2 D' R D' R2 D'", cube)
solve_cross(cube)
pprint(cube.sides)
