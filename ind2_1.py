#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import math


if __name__ == '__main__':
    a = int(input("Введите значение a= "))
    b = int(input("Введите значение b= "))
    c = int(input("Введите значение c= "))
    if a == 0:
        print('Oшибка')
    else:
        d = b ** 2 - 4 * a * c
        if d < 0:
            print("Корней нет")
        else:
            x1 = (-b + math.sqrt(d)) / (2 * a)
            x2 = (-b - math.sqrt(d)) / (2 * a)
            print(x1)
            print(x2)
