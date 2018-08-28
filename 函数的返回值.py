# coding:utf-8

def fahrenheit_converter(c):
    fahrenheit = c * 9 / 5 + 32
    return str(fahrenheit) + 'F'

temper = fahrenheit_converter(0)
print(temper)