# coding:utf-8
# get image name from a url
a_url = "http://www.baidu.com/this_is_a_test_img_url.jpg"
file_name = a_url[len("http://www.baidu.com/"):]
print(file_name)


# city_name = input("Please input a city name:")
# weather_url = "http://www.baidu.com/weather:{}"
# print(weather_url)

def tri_times_words(arg1, arg2):
    print("words" * 3)
    return "words" * 3


tri_times_words(1, 2)


def fahrenheit_converter(c):
    fahrenheit = c * 9 / 5 + 32
    return str(fahrenheit) + 'F'


def fahrenheit_converter_no_return(c):
    fahrenheit = c * 9 / 5 + 32
    print(str(fahrenheit) + 'F')


temper = fahrenheit_converter(0)
print(temper)

temper = fahrenheit_converter_no_return(0)
print(temper)

lyric_length = len("I cry out for magic")
print(lyric_length)


def weight_converter(weight_in_gram):
    weight_in_kilogram = weight_in_gram / 1000.0
    return weight_in_kilogram


weight_in_kilogram = weight_converter(1500)
print(weight_in_kilogram)


def calc_xie_bian(zhi_jiao_1, zhi_jiao_2):
    # get Math.power method like in java.
    xie_bian = zhi_jiao_1 * zhi_jiao_1 + zhi_jiao_2 * zhi_jiao_2
    return xie_bian


gram_result = weight_converter(weight_in_gram=1212)
print(gram_result)
