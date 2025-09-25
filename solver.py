from cube_model import Cube_model
from pprint import pprint


text_src = "r2 l2 u2 b2 r l u b"
cube = Cube_model()

def do_moves(text, cube):
    moves = [
    "r2","b","b2","d","d2","dw","f","f2","fw","l","l2","m","r",
    "br","dr","fr","lr","mr","rr","rwr","ur","rw","u","u2","uw"
    ]

    lower_text = text.lower()

    scramble = lower_text.split()
    scramble = [move.replace("'", "r") for move in scramble]


    actions = {
        "r2": cube.rotate_r2,
        "b": cube.rotate_b,
        "b2": cube.rotate_b2,
        "d": cube.rotate_d,
        "d2": cube.rotate_d2,
        "dw": cube.rotate_dw,
        "f": cube.rotate_f,
        "f2": cube.rotate_f2,
        "fw": cube.rotate_fw,
        "l": cube.rotate_l,
        "l2": cube.rotate_l2,
        "m": cube.rotate_m,
        "r": cube.rotate_r,
        "br": cube.rotate_reverse_b,
        "dr": cube.rotate_reverse_d,
        "fr": cube.rotate_reverse_f,
        "lr": cube.rotate_reverse_l,
        "mr": cube.rotate_reverse_m,
        "rr": cube.rotate_reverse_r,
        "rwr": cube.rotate_reverse_rw,
        "ur": cube.rotate_reverse_u,
        "rw": cube.rotate_rw,
        "u": cube.rotate_u,
        "u2": cube.rotate_u2,
        "uw": cube.rotate_uw,
    }

    for move in scramble:
        if move not in actions:
            print(f"Wrong scramble: {move}")
            break
        actions[move]()  # вызов метода
