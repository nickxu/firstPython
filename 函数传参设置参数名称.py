# coding:utf-8
def weight_converter(weight_in_gram):
    weight_in_kilogram = weight_in_gram / 1000.0
    return weight_in_kilogram

gram_result = weight_converter(weight_in_gram=1212)
print(gram_result)


def calc_xie_bian(zhi_jiao_1, zhi_jiao_2):
    # get Math.power method like in java.
    xie_bian = zhi_jiao_1 * zhi_jiao_1 + zhi_jiao_2 * zhi_jiao_2
    return xie_bian