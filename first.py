# coding:utf-8

# str by times
print("words" * 3)
a_str = "111"
print(a_str)

# open a file to write
a_file = open("E:\\workspace-python\\firstPython\\py.txt", "w")
a_file.write("22222")

# concat strings
his_name = "Robert"
what_he_does = " Play a game."
print(his_name + what_he_does)

# format a string to plus a nubmer
print(1 + int("1"))

# use times string to print
word = "it's a looooooong loop"
num = 12
bang_str = 'bang!'
total_result = bang_str * (len(word) - num)
print(total_result)

# get sub string of a string object
print(word[:5])
print(word[10:])
print(word[-4])
print(word[10:20])
print(word[10:30])

# get image name from a url
a_url = "http://www.baidu.com/this_is_a_test_img_url.jpg"
file_name = a_url[len("http://www.baidu.com/"):]
print(file_name)

# replace a phone number part to *
a_phone_number = "128-1188-2222"
b_phone_number = "112-1188-2222"
print(a_phone_number.replace(a_phone_number[:9], "*" * 9))

# format a string by template method
print("{} is a good {}".format("Jack", "boy"))
print("{firstPart} is a good {secondPart}".format(firstPart="Jack", secondPart="boy"))
print("{0} is a good {1}".format("Jack", "boy"))


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
