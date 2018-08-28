# coding:utf-8

def weight_converter(weight_in_gram):
    weight_in_kilogram = weight_in_gram / 1000.0
    return weight_in_kilogram


weight_in_kilogram = weight_converter(1500)
print(weight_in_kilogram)