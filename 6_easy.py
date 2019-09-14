__author__ = 'Попцов А.В.'

import math

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class Triangle:
    # конструктор
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = x3

    # площадь
    def Ploschad(self):
        return 0.5 * abs(((int(self.x2) - int(self.x1)) * (int(self.y3) - int(self.y1))) - ((int(self.x3) - int(self.x1)) * (int(self.y2) - int(self.y1))))

    # периметр
    def Perimetr(self):
        return math.sqrt((int(self.x2) - int(self.x1))**2 + (int(self.y2) - int(self.y1))**2) + math.sqrt((int(self.x3) - int(self.x2))**2 + (int(self.y3) - int(self.y2))**2) + math.sqrt((int(self.x3) - int(self.x1))**2 + (int(self.y3) - int(self.y1))**2)

    # Вычислим высоту, например опущенную из точки В на сторону АС
    def Vysota(self):
        # Назовем вершины треугольника цифрами: А - 1, В - 2, С - 3. Тогда АВ = 12, ВС = 23, АС = 13
        # L1 - Длина АВ, L2 - длина ВС, L3 - длина АС
        L1 = math.sqrt((int(self.x2) - int(self.x1))**2 + (int(self.y2) - int(self.y1))**2)
        L2 = math.sqrt((int(self.x3) - int(self.x2))**2 + (int(self.y3) - int(self.y2))**2)
        L3 = math.sqrt((int(self.x3) - int(self.x1))**2 + (int(self.y3) - int(self.y1))**2)

        # Находим косинус угла АСВ
        с = (L3**2 + L2**2 - L1**2)//(2 * L3 * L2)

        # Находим синус угла АСВ
        s = math.sqrt(1 - с**2)

        # Находим высоту, опущенную из точки В
        L4 = L2 * s

        return L4

Triangle1 = Triangle(1,2,3,4,5,6)
print(Triangle1.Ploschad())
print(Triangle1.Perimetr())
print(Triangle1.Vysota())

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trap:
    # конструктор
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = x3
        self.x4 = x4
        self.y4 = y4

        # длины сторон
        self.len_12 = math.sqrt((int(self.x2) - int(self.x1))**2 + (int(self.y2) - int(self.y1))**2)
        self.len_23 = math.sqrt((int(self.x3) - int(self.x2))**2 + (int(self.y3) - int(self.y2))**2)
        self.len_34 = math.sqrt((int(self.x4) - int(self.x3))**2 + (int(self.y4) - int(self.y3))**2)
        self.len_41 = math.sqrt((int(self.x1) - int(self.x4))**2 + (int(self.y1) - int(self.y4))**2)

    # является ли фигура равнобочной трапецией?
    # трапеция будет равнобочной при равенстве длин её диагоналей и попарном равестве сторон
    def Is_Ravnob(self):

        # != приверка на квадрат, прямоугольник
        if (self.len_12 == self.len_34) and (self.len_23 == self.len_41) and ((self.len_12 != self.len_23) and (self.x1 != self.x2) and (self.x3 != self.x4)):
            v_res = 1 # равнобочная
        else:
            v_res = 0 # неравнобочная, не трапеция вовсе!
        return str(v_res)

    # площадь
    def Ploschad(self):
        return 0.5 * abs(((int(self.x2) - int(self.x1)) * (int(self.y3) - int(self.y1))) - ((int(self.x3) - int(self.x1)) * (int(self.y2) - int(self.y1))))

    # периметр
    def Perimetr(self):
        return str(float(self.len_12) + float(self.len_23) + float(self.len_34) + float(self.len_41))

Trap1 = Trap(1,1,2,2,3,2,4,1)
print("Признак равнобочности трапеции = " + Trap1.Is_Ravnob())
print("Периметр трапеции = " + Trap1.Perimetr())