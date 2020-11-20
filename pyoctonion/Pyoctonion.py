import numpy as np
import sympy as sym
import math
import pyquaternion as pqu
import __future__


class Octonion:
    def __init__(self, x_0, x_1, x_2, x_3, x_4, x_5, x_6, x_7):
        self.x_0 = x_0
        self.x_1 = x_1
        self.x_2 = x_2
        self.x_3 = x_3
        self.x_4 = x_4
        self.x_5 = x_5
        self.x_6 = x_6
        self.x_7 = x_7
        self.norm = self.cal_norm()
        # self.conjugate = self.cal_conjugate()

    # self.inverse = self.cal_inverse()

    def Octon(self, x_0, x_1, x_2, x_3, x_4, x_5, x_6, x_7):  # define Octonion
        r_1 = [x_0, x_1, x_2, x_3, x_4, x_5, x_6, x_7]
        a_1 = np.array(r_1, float)
        return a_1

    def cal_norm(self):  # define norm
        b_1 = math.sqrt(
            self.x_0 ** 2
            + self.x_1 ** 2
            + self.x_2 ** 2
            + self.x_3 ** 2
            + self.x_4 ** 2
            + self.x_5 ** 2
            + self.x_6 ** 2
            + self.x_7 ** 2
        )
        return b_1

    def cal_conjugate(self):
        r_2 = [
            self.x_0,
            -(self.x_1),
            -(self.x_2),
            -(self.x_3),
            -(self.x_4),
            -(self.x_5),
            -(self.x_6),
            -(self.x_7),
        ]
        a_2 = np.array(r_2, float)
        return a_2

    @property
    def conjugate(self):
        conj = Octonion(
            self.x_0,
            -(self.x_1),
            -(self.x_2),
            -(self.x_3),
            -(self.x_4),
            -(self.x_5),
            -(self.x_6),
            -(self.x_7),
        )
        return conj

    def cal_multiply(self, x, y):  # define octonion multiplication
        # from pyquaternion import Quaternion
        a = pqu.Quaternion(x.x_0, x.x_1, x.x_2, x.x_3)
        b = pqu.Quaternion(x.x_4, x.x_5, x.x_6, x.x_7)
        c = pqu.Quaternion(y.x_0, y.x_1, y.x_2, y.x_3)
        d = pqu.Quaternion(y.x_4, y.x_5, y.x_6, y.x_7)
        a_1 = a * c - (d.conjugate) * b
        b_1 = (d * a) + (b * (c.conjugate))
        # print(np.array(a_1, float))
        # print(np.array(b_1, float))
        print(
            self.Octon(a_1[0], a_1[1], a_1[2], a_1[3], b_1[0], b_1[1], b_1[2], b_1[3])
        )
        xy = [a_1[0], a_1[1], a_1[2], a_1[3], b_1[0], b_1[1], b_1[2], b_1[3]]
        xyz = np.array(xy, float)
        return xyz

    @property
    def inverse(self):  # define inverse
        # from pyquaternion import Quaternion
        b = self.cal_conjugate()
        # print("conjugate:{}".format(b))
        c = self.norm
        d = c ** 2
        e = [
            b[0] / d,
            b[1] / d,
            b[2] / d,
            b[3] / d,
            b[4] / d,
            b[5] / d,
            b[6] / d,
            b[7] / d,
        ]
        # x = np.array(e, float)
        x = Octonion(
            b[0] / d,
            b[1] / d,
            b[2] / d,
            b[3] / d,
            b[4] / d,
            b[5] / d,
            b[6] / d,
            b[7] / d,
        )
        return x

    def __div__(x, y):
        if isinstance(y, Octonion) and isinstance(x, Octonion):
            conj = Octonion(
                y.x_0,
                -(y.x_1),
                -(y.x_2),
                -(y.x_3),
                -(y.x_4),
                -(y.x_5),
                -(y.x_6),
                -(y.x_7),
            )
            top = x * conj
            bottom = (
                y.x_0 ** 2
                + y.x_1 ** 2
                + y.x_2 ** 2
                + y.x_3 ** 2
                + y.x_4 ** 2
                + y.x_5 ** 2
                + y.x_6 ** 2
                + y.x_7 ** 2
            )

            addition = Octonion(
                top.x_0 / bottom,
                top.x_1 / bottom,
                top.x_2 / bottom,
                top.x_3 / bottom,
                top.x_4 / bottom,
                top.x_5 / bottom,
                top.x_6 / bottom,
                top.x_7 / bottom,
            )
            return addition
        elif isinstance(x, Octonion) and not isinstance(y, Octonion):
            bottom = float(y)
            addition = Octonion(
                x.x_0 / bottom,
                x.x_1 / bottom,
                x.x_2 / bottom,
                x.x_3 / bottom,
                x.x_4 / bottom,
                x.x_5 / bottom,
                x.x_6 / bottom,
                x.x_7 / bottom,
            )
            return addition
        raise NotImplementedError

    def __rdiv__(y, x):
        if isinstance(y, Octonion):
            conj = Octonion(
                y.x_0,
                -(y.x_1),
                -(y.x_2),
                -(y.x_3),
                -(y.x_4),
                -(y.x_5),
                -(y.x_6),
                -(y.x_7),
            )
            top = float(x) * conj
            bottom = (
                y.x_0 ** 2
                + y.x_1 ** 2
                + y.x_2 ** 2
                + y.x_3 ** 2
                + y.x_4 ** 2
                + y.x_5 ** 2
                + y.x_6 ** 2
                + y.x_7 ** 2
            )
            addition = Octonion(
                top.x_0 / bottom,
                top.x_1 / bottom,
                top.x_2 / bottom,
                top.x_3 / bottom,
                top.x_4 / bottom,
                top.x_5 / bottom,
                top.x_6 / bottom,
                top.x_7 / bottom,
            )
            return addition
        raise NotImplementedError

    def __truediv__(x, y):
        if isinstance(y, Octonion) and isinstance(x, Octonion):
            conj = Octonion(
                y.x_0,
                -(y.x_1),
                -(y.x_2),
                -(y.x_3),
                -(y.x_4),
                -(y.x_5),
                -(y.x_6),
                -(y.x_7),
            )
            top = x * conj
            bottom = (
                y.x_0 ** 2
                + y.x_1 ** 2
                + y.x_2 ** 2
                + y.x_3 ** 2
                + y.x_4 ** 2
                + y.x_5 ** 2
                + y.x_6 ** 2
                + y.x_7 ** 2
            )

            addition = Octonion(
                top.x_0 / bottom,
                top.x_1 / bottom,
                top.x_2 / bottom,
                top.x_3 / bottom,
                top.x_4 / bottom,
                top.x_5 / bottom,
                top.x_6 / bottom,
                top.x_7 / bottom,
            )
            return addition
        elif isinstance(x, Octonion) and not isinstance(y, Octonion):
            bottom = float(y)
            addition = Octonion(
                x.x_0 / bottom,
                x.x_1 / bottom,
                x.x_2 / bottom,
                x.x_3 / bottom,
                x.x_4 / bottom,
                x.x_5 / bottom,
                x.x_6 / bottom,
                x.x_7 / bottom,
            )
            return addition
        raise NotImplementedError

    def __rtruediv__(y, x):
        if isinstance(y, Octonion):
            conj = Octonion(
                y.x_0,
                -(y.x_1),
                -(y.x_2),
                -(y.x_3),
                -(y.x_4),
                -(y.x_5),
                -(y.x_6),
                -(y.x_7),
            )
            top = float(x) * conj
            bottom = (
                y.x_0 ** 2
                + y.x_1 ** 2
                + y.x_2 ** 2
                + y.x_3 ** 2
                + y.x_4 ** 2
                + y.x_5 ** 2
                + y.x_6 ** 2
                + y.x_7 ** 2
            )
            addition = Octonion(
                top.x_0 / bottom,
                top.x_1 / bottom,
                top.x_2 / bottom,
                top.x_3 / bottom,
                top.x_4 / bottom,
                top.x_5 / bottom,
                top.x_6 / bottom,
                top.x_7 / bottom,
            )
            return addition
        raise NotImplementedError

    def __mul__(x, y):
        if isinstance(y, Octonion) and isinstance(x, Octonion):
            a = pqu.Quaternion(x.x_0, x.x_1, x.x_2, x.x_3)
            b = pqu.Quaternion(x.x_4, x.x_5, x.x_6, x.x_7)
            c = pqu.Quaternion(y.x_0, y.x_1, y.x_2, y.x_3)
            d = pqu.Quaternion(y.x_4, y.x_5, y.x_6, y.x_7)
            a_1 = a * c - (d.conjugate) * b
            b_1 = (d * a) + (b * (c.conjugate))
            # xy = [a_1[0], a_1[1], a_1[2], a_1[3], b_1[0], b_1[1], b_1[2], b_1[3]]
            # xyz = np.array(xy, float)
            mul = Octonion(
                a_1[0], a_1[1], a_1[2], a_1[3], b_1[0], b_1[1], b_1[2], b_1[3]
            )
            return mul
        elif isinstance(x, Octonion) and not isinstance(y, Octonion):
            mul = [
                x.x_0 * y,
                x.x_1 * y,
                x.x_2 * y,
                x.x_3 * y,
                x.x_4 * y,
                x.x_5 * y,
                x.x_6 * y,
                x.x_7 * y,
            ]
            multi = Octonion(
                mul[0], mul[1], mul[2], mul[3], mul[4], mul[5], mul[6], mul[7]
            )
            return multi
        raise NotImplementedError

    def __rmul__(y, x):
        # print(x)
        # print(y)
        if isinstance(y, Octonion):
            mul = [
                x * y.x_0,
                x * y.x_1,
                x * y.x_2,
                x * y.x_3,
                x * y.x_4,
                x * y.x_5,
                x * y.x_6,
                x * y.x_7,
            ]
            addition = Octonion(
                mul[0], mul[1], mul[2], mul[3], mul[4], mul[5], mul[6], mul[7]
            )
            return addition
        raise NotImplementedError

    def __add__(x, y):
        if isinstance(y, Octonion) and isinstance(x, Octonion):
            total = [
                x.x_0 + y.x_0,
                x.x_1 + y.x_1,
                x.x_2 + y.x_2,
                x.x_3 + y.x_3,
                x.x_4 + y.x_4,
                x.x_5 + y.x_5,
                x.x_6 + y.x_6,
                x.x_7 + y.x_7,
            ]
            addition = Octonion(
                total[0],
                total[1],
                total[2],
                total[3],
                total[4],
                total[5],
                total[6],
                total[7],
            )
            return addition
        elif isinstance(x, Octonion) and not isinstance(y, Octonion):
            total = [x.x_0 + y, x.x_1, x.x_2, x.x_3, x.x_4, x.x_5, x.x_6, x.x_7]
            addition = Octonion(
                total[0],
                total[1],
                total[2],
                total[3],
                total[4],
                total[5],
                total[6],
                total[7],
            )
            return addition
        raise NotImplementedError

    def __radd__(y, x):
        # print(x)
        # print(y)
        if isinstance(y, Octonion):
            total = [x + y.x_0, y.x_1, y.x_2, y.x_3, y.x_4, y.x_5, y.x_6, y.x_7]
            addition = Octonion(
                total[0],
                total[1],
                total[2],
                total[3],
                total[4],
                total[5],
                total[6],
                total[7],
            )
            return addition
        raise NotImplementedError

    def __sub__(x, y):
        if isinstance(y, Octonion) and isinstance(x, Octonion):
            total = [
                x.x_0 - y.x_0,
                x.x_1 - y.x_1,
                x.x_2 - y.x_2,
                x.x_3 - y.x_3,
                x.x_4 - y.x_4,
                x.x_5 - y.x_5,
                x.x_6 - y.x_6,
                x.x_7 - y.x_7,
            ]
            addition = Octonion(
                total[0],
                total[1],
                total[2],
                total[3],
                total[4],
                total[5],
                total[6],
                total[7],
            )
            return addition
        elif isinstance(x, Octonion) and not isinstance(y, Octonion):
            total = [x.x_0 - y, x.x_1, x.x_2, x.x_3, x.x_4, x.x_5, x.x_6, x.x_7]
            addition = Octonion(
                total[0],
                total[1],
                total[2],
                total[3],
                total[4],
                total[5],
                total[6],
                total[7],
            )
            return addition
        raise NotImplementedError

    def __rsub__(y, x):
        # print(x)
        # print(y)
        if isinstance(y, Octonion):
            total = [x - y.x_0, -y.x_1, -y.x_2, -y.x_3, -y.x_4, -y.x_5, -y.x_6, -y.x_7]
            addition = Octonion(
                total[0],
                total[1],
                total[2],
                total[3],
                total[4],
                total[5],
                total[6],
                total[7],
            )
            return addition
        raise NotImplementedError

    def __repr__(self):
        return "%+.4f %+0.4fi %+0.4fj %+0.4fk %+0.4fl %+0.4fil %+0.4fjl %+0.4fkl" % (
            self.x_0,
            self.x_1,
            self.x_2,
            self.x_3,
            self.x_4,
            self.x_5,
            self.x_6,
            self.x_7,
        )

    def __pow__(x, pow):
        if isinstance(x, Octonion):
            y = Octonion(x.x_0, x.x_1, x.x_2, x.x_3, x.x_4, x.x_5, x.x_6, x.x_7)
            while pow > 1:
                # print(y)
                a = pqu.Quaternion(x.x_0, x.x_1, x.x_2, x.x_3)
                b = pqu.Quaternion(x.x_4, x.x_5, x.x_6, x.x_7)
                c = pqu.Quaternion(y.x_0, y.x_1, y.x_2, y.x_3)
                d = pqu.Quaternion(y.x_4, y.x_5, y.x_6, y.x_7)
                a_1 = a * c - (d.conjugate) * b
                b_1 = (d * a) + (b * (c.conjugate))
                y = Octonion(
                    a_1[0], a_1[1], a_1[2], a_1[3], b_1[0], b_1[1], b_1[2], b_1[3]
                )
                pow -= 1
            return y
        raise NotImplementedError


b = Octonion(1, 0, 0, 0, 0, 0, 1, 1)
# c = Octonion(1, 0, 0, 0, 0, 0, 0, 1)
print(b ** 300)
# print(b ** 3)
# print('b*b*b')
# print(b*b*b)
# print('c**4')
# print(c ** 4)
# print('c*c*c*c')
# print(c*c*c*c)


# print(b / c)
# print(2 / b)
# print(b / 2)
# print(b * 5)
# print(5 * b)
# print(2 / b)

# print(b * c)
# print(b * 2)
# print(2 * b)
# print(c)
# print(b.conjugate)
# print(b.inverse)
# print(2 * b)
# print(b + c)
# print(b - c)
# print(2 + b)
# print(b + 2)
# print(b - 2)
# print(2 - b)


# octonion.oct_quad(0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0)

# octonion.oct_quad(2/3,0,0,-1/3,-1/3,0,0,0,-1/3,0,0,2/3,2/3,0,0,0)

# octonion.oct_quad(0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0)

# octonion.oct_quad(0,0,0,0,0,0,0,0,1,2,3,4,5,6,7,8)

# octonion.oct_quad(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)
