# Python функциялары

# Функция - бул кандайдыр бир ишти аткаруучу сөз
# print() # маалымат чыгарат
# type() # маалымат түрүн аныктайт
# int() # санга айландырат
# str() # сапка айландырат
# sum() # сандардын суммасын аныктайт
# len() # саптын же тизменин узундугун аныктайт



# print("hello world!")
# print("hello world!")
# print("hello world!")
# print("hello world!")
# print("hello world!")


# def - define - жарыялоо

def hello():
    print("hello world!") # денеси

hello()
hello()
hello()
hello()
hello()


def exp():
    san = int(input("Sandy jaz: "))
    result = san * 2
    print(result)

# exp()
# exp()
# exp()

def parameters(name):
    print(f"Hello {name}")

parameters("Baiaman")


def bio(name, age):
    print(f"My name is {name}. I'm {age} years old")

bio("Temirlan", 18) # позициялык аргументтоо
bio(18, "temirlan")

bio(age = 18,name = "Temirlan") # аты боюнча аргументтоо



def secret():
    import random
    random_san = random.randint(1, 10)
    return random_san


# lambda - anonym
a = lambda x: x * 2
print(a(5))

# Үй тапшырма:

# 1.  Атыңарды ЧОҢ ТАМГА менен чыгарган функция түзгүлө

def print_name_upper(name):
    print(name.upper())

# 2.  Аргумент менен функция түзгүлө.
#     Функция төмөнкү аргументтерди кабыл алыш керек:
#     аты, жашы, жашаган жери
#     аргументтерди алып мисалдагы сүйлөмдү чыгарыш керек
#     Мисал: Менин атым Марсель. Мен 12 жаштамын.
#            Мен Кыргызстанда жашаймын.

def print_profile(name, age, city):
    print(f"Менин атым {name}. Мен {age} жаштамын.")
    print(f"Мен {city}да жашаймын.")

print_name_upper("мээрим")
print_profile("Мээрим", 14, "Кыргызстан")



