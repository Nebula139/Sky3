#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import math


if __name__ == '__main__':
    a = input('Введите время: ')
    t = 0
    A = 1
    V = int(int(a)/3)
    if V == 0:
        print('Ошибка')
    else:
        while t < int(a):
            t = t + 3
            A *= 2
        print('Через ' + a + ' часов будет ' + str(A) + ' амёбы')
