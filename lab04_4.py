 #-*- coding: utf-8 -*-

import string

text = 'Задивляюсь у твої зіниці Голубі й тривожні, ніби рань. Крешуть з них червоні блискавиці Революцій, бунтів і повстань. Україно! Ти для мене диво! І нехай пливе за роком рік, Буду, мамо горда і вродлива, З тебе дивуватися повік... Одійдіте, недруги лукаві! Друзі, зачекайте на путі! Маю я святе синівське право З матір\'ю побуть на самоті. Рідко, нене, згадують про тебе, Дні занадто куці та малі, Ще не всі чорти живуть на небі, Ходить їх до біса на землі. Бачиш, з ними щогодини б\'юся, Чуєш - битви споконвічний грюк! Як же я без друзів обійдуся, Без лобів їх, без очей і рук? Україно, ти моя молитва, Ти моя розпука вікова... Гримотить над світом люта битва За твоє життя, твої права. Ради тебе перли в душу сію, Ради тебе мислю і творю... Хай мовчать Америки й Росії, Коли я з тобою говорю. Хай палають хмари бурякові, Хай сичать образи - все одно Я проллюся крапелькою крові На твоє священне знамено.'
text = text.translate(str.maketrans('', '', string.punctuation))

ALPHABET = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
ALPHABET += ALPHABET.upper()
ALPHABET += ' '

M = len(ALPHABET)

def affine_encrypt(text, key):
    return ''.join(ALPHABET[(key[0]*ALPHABET.index(t) 
    + key[1] ) % M] for t in text)

def affine_decrypt(cipher, key):
    return ''.join(ALPHABET[(modinv(key[0]) * (ALPHABET.index(c) - key[1])) % M] for c in cipher)

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y
 
def modinv(a):
    gcd, x, y = egcd(a, M)
    if gcd != 1:
        return None  
    else:
        return x % M

cipher = affine_encrypt(text, [3,5])
print(cipher)

print(affine_decrypt(cipher,[3,5]))