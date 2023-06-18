# ФАКТОРИАЛ

def fact(n):
    result = 1
    for i in range (1, n + 1):
        result *= i
    return result

print(fact(5))


def simple(a):
    if a <= 1:
        return False
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
        return True


print(simple(49))


def reverse_str(n):
    n = n[::-1]
    return n

print(reverse_str('ooov'))

def count_vowel(s):
    vowels = 'aeiouyAEIOUY'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

print(count_vowel('hello world'))

import math


def area(fig_type, *args):
    if fig_type == 'circle':
        r = args[0]
        return math.pi * r ** 2
    elif fig_type == 'rectangle':
        a, b = args
        return a * b
    elif fig_type == 'triangle':
        a, b, c = args
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))
    else:
        return 'не верная фигура'

print(area('circle', 5))
print(area('rectangle', 5, 8))
print(area('triangle', 7, 10, 5))
print(area('lkjfikji', 6))


def palindrome(s):
    s = "".join(letter for letter in s if s.isalpha()).lower()
    #s = s.lower()
    reverse_s = s[::-1]
    if s == reverse_s:
        return True
    else:
        return False

print(palindrome('afYeWWEq'))
print(palindrome('а роза, упала на, лапу Азора'))

even = lambda x: x % 2 == 0
print(even(10))


def greet(name: str) -> str:
    return 'Hello, ' + name

def add(x: int, y):
    return x + y