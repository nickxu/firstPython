# coding:utf-8
word = 'My name is Mike'
print(word[:5])
print(word[10:])
print(word[-4])
print(word[10:20])
print(word[10:30])

a_url = "http://www.baidu.com/this_is_a_test_img_url.jpg"
file_name = a_url[len("http://www.baidu.com/"):]
print(file_name)
