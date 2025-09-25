class Cube_model:
    def __init__(self):
        self.sides: dict[str, list[str]] = {
            "w": ["w"]*9,
            "g": ["g"]*9,
            "r": ["r"]*9,
            "b": ["b"]*9,
            "y": ["y"]*9,
            "o": ["o"]*9,
        } # ["1","2","3","4","5","6","7","8","9",]
    def upload(self):
        print('Введите состояние своего кубика, держа белым сверху, ' \
        'зеленым слева, красным к себе, синим справа, желтым снизу и оранжевым сзади')
        input('Нажмите Enter, чтобы продолжить...')
        print('Введите белую сторону сверху вниз и слева направо')
        self.sides["w"] = input()
        print('Введите зеленую сторону сверху вниз и слева направо')
        self.sides["g"] = input()
        print('Введите красную сторону сверху вниз и слева направо')
        self.sides["r"] = input()
        print('Введите синюю сторону сверху вниз и слева направо')
        self.sides["b"] = input()
        print('Введите желтую сторону сверху вниз и слева направо')
        self.sides["y"] = input()
        print('Введите оранжевую сторону сверху вниз и слева направо')
        self.sides["o"] = input()

    def rotate_r(self):
        temp = [self.sides["r"][2], self.sides["r"][5], self.sides["r"][8]]

        self.sides["r"][2] = self.sides["y"][2]
        self.sides["r"][5] = self.sides["y"][5]
        self.sides["r"][8] = self.sides["y"][8]

        self.sides["y"][2] = self.sides["o"][6]
        self.sides["y"][5] = self.sides["o"][3]
        self.sides["y"][8] = self.sides["o"][0]

        self.sides["o"][0] = self.sides["w"][8]
        self.sides["o"][3] = self.sides["w"][5]
        self.sides["o"][6] = self.sides["w"][2]

        self.sides["w"][2] = temp[0]
        self.sides["w"][5] = temp[1]
        self.sides["w"][8] = temp[2]
    
        self.rotate_face_clockwise("b")

    
    def rotate_r2(self):
        self.rotate_r()
        self.rotate_r()

    def rotate_reverse_r(self):
        self.rotate_r()
        self.rotate_r()
        self.rotate_r()
    
    def rotate_l(self):
        temp = [self.sides["r"][0], self.sides["r"][3], self.sides["r"][6]]
    
        self.sides["r"][0] = self.sides["w"][0]
        self.sides["r"][3] = self.sides["w"][3]
        self.sides["r"][6] = self.sides["w"][6]
    
        self.sides["w"][0] = self.sides["o"][8]
        self.sides["w"][3] = self.sides["o"][5]
        self.sides["w"][6] = self.sides["o"][2]
    
        self.sides["o"][8] = self.sides["y"][0]
        self.sides["o"][5] = self.sides["y"][3]
        self.sides["o"][2] = self.sides["y"][6]
    
        self.sides["y"][0] = temp[0]
        self.sides["y"][3] = temp[1]
        self.sides["y"][6] = temp[2]
        self.rotate_face_clockwise("g")
    
    def rotate_l2(self):
        self.rotate_l()
        self.rotate_l()


    def rotate_reverse_l(self):
        self.rotate_l()
        self.rotate_l()
        self.rotate_l()
    
    def rotate_face_clockwise(self, face: str):
        s = self.sides[face]
        self.sides[face] = [
            s[6], s[3], s[0],
            s[7], s[4], s[1],
            s[8], s[5], s[2]
        ]

    def rotate_m(self):
        self.rotate_r()
        self.rotate_reverse_l()

    def rotate_reverse_m(self):
        self.rotate_reverse_r()
        self.rotate_l()

    def rotate_rw(self):
        self.rotate_l()

    def rotate_reverse_rw(self):
        self.rotate_r()

    def rotate_u(self):
        temp = [self.sides["r"][0], self.sides["r"][1], self.sides["r"][2]]

        self.sides["r"][0] = self.sides["b"][0]
        self.sides["r"][1] = self.sides["b"][1]
        self.sides["r"][2] = self.sides["b"][2]

        self.sides["b"][0] = self.sides["o"][0]
        self.sides["b"][1] = self.sides["o"][1]
        self.sides["b"][2] = self.sides["o"][2]

        self.sides["o"][0] = self.sides["g"][0]
        self.sides["o"][1] = self.sides["g"][1]
        self.sides["o"][2] = self.sides["g"][2]

        self.sides["g"][0] = temp[0]
        self.sides["g"][1] = temp[1]
        self.sides["g"][2] = temp[2]

        self.rotate_face_clockwise("w")

    def rotate_reverse_u(self):
        self.rotate_u()
        self.rotate_u()
        self.rotate_u()

    def rotate_uw(self):
        self.rotate_d()

    def rotate_u2(self):
        self.rotate_u()
        self.rotate_u()

    def rotate_d(self):
        temp = [self.sides["r"][6], self.sides["r"][7], self.sides["r"][8]]

        self.sides["r"][6] = self.sides["g"][6]
        self.sides["r"][7] = self.sides["g"][7]
        self.sides["r"][8] = self.sides["g"][8]

        self.sides["g"][6] = self.sides["o"][6]
        self.sides["g"][7] = self.sides["o"][7]
        self.sides["g"][8] = self.sides["o"][8]

        self.sides["o"][6] = self.sides["b"][6]
        self.sides["o"][7] = self.sides["b"][7]
        self.sides["o"][8] = self.sides["b"][8]

        self.sides["b"][6] = temp[0]
        self.sides["b"][7] = temp[1]
        self.sides["b"][8] = temp[2]

        self.rotate_face_clockwise("y")
    
    def rotate_d2(self):
        self.rotate_d()
        self.rotate_d()

    def rotate_reverse_d(self):
        self.rotate_d()
        self.rotate_d()
        self.rotate_d()

    def rotate_dw(self):
        self.rotate_u()

    def rotate_f(self):
        temp = [self.sides["w"][6], self.sides["w"][7], self.sides["w"][8]]

        self.sides["w"][6] = self.sides["g"][8]
        self.sides["w"][7] = self.sides["g"][5]
        self.sides["w"][8] = self.sides["g"][2]

        self.sides["g"][2] = self.sides["y"][0]
        self.sides["g"][5] = self.sides["y"][1]
        self.sides["g"][8] = self.sides["y"][2]

        self.sides["y"][0] = self.sides["b"][6]
        self.sides["y"][1] = self.sides["b"][3]
        self.sides["y"][2] = self.sides["b"][0]

        self.sides["b"][0] = temp[0]
        self.sides["b"][3] = temp[1]
        self.sides["b"][6] = temp[2]

        self.rotate_face_clockwise("r")

    def rotate_reverse_f(self):
        self.rotate_f()
        self.rotate_f()
        self.rotate_f()

    def rotate_f2(self):
        self.rotate_f()
        self.rotate_f()

    def rotate_fw(self):
        self.rotate_b()

    def rotate_b(self):
        temp = [self.sides["w"][0], self.sides["w"][1], self.sides["w"][2]]

        self.sides["w"][0] = self.sides["b"][2]
        self.sides["w"][1] = self.sides["b"][5]
        self.sides["w"][2] = self.sides["b"][8]

        self.sides["b"][2] = self.sides["y"][8]
        self.sides["b"][5] = self.sides["y"][7]
        self.sides["b"][8] = self.sides["y"][6]

        self.sides["y"][6] = self.sides["g"][0]
        self.sides["y"][7] = self.sides["g"][3]
        self.sides["y"][8] = self.sides["g"][6]

        self.sides["g"][0] = temp[2]
        self.sides["g"][3] = temp[1]
        self.sides["g"][6] = temp[0]

        self.rotate_face_clockwise("o")

    def rotate_reverse_b(self):
        self.rotate_b()
        self.rotate_b()
        self.rotate_b()

    def rotate_b2(self):
        self.rotate_b()
        self.rotate_b()

    
        
