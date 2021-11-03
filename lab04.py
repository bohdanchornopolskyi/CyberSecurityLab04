from collections import Counter
import os, string
import pandas

myFiles = os.listdir('text')  # зберігаємо назви всіх файлів х папки text
count = 0
for file in myFiles:
    print(count, file)  # виводимо назви всіх файлів в консоль
    count += 1
chosenFile = int(input("Введіть номер файлу(зi списку вище) для обробки алгоритмом: "))  # просимо ввести номер файлу

if chosenFile <= len(myFiles):  # перевіряємо що був введений правильний символ
    fileName = 'text\\' + myFiles[chosenFile]  # зберігаємо назву файлу в змінну
    bigrams = dict()
    trigrams = dict()
    with open(fileName, "r", encoding="utf-8") as openedFile:  # відкриваємо файл
        textOfTheFile = openedFile.read()  # зберігаємо текст файлу в змінну
        text_len = len(textOfTheFile)
        textOfTheFile = textOfTheFile.translate(str.maketrans('', '', string.punctuation)) #видаляємо пунктуацію
        allLetters = Counter(textOfTheFile)
        textOfTheFile.replace(" ", "")
        for i in range(len(textOfTheFile)): # знаходження і збереження біграм
            try:
                b = textOfTheFile[i:i+2]
                if b in bigrams:
                    bigrams[b] += 1
                else:
                    bigrams[b] = 1  
            except:
                break
        for i in range(len(textOfTheFile)): # знаходження і збереження триграм
            try:
                t = textOfTheFile[i:i+3]
                if t in trigrams:
                    trigrams[t] += 1 
                else:
                    trigrams[t] = 1  
            except:
                break
    # зберігаємо в змінну словник в якому ключами будуть символи з тексту а їх значеннями кількість разів появи цього
    # символу в тексті + сортуємо в алфавітному порядку
    rows_list_letters = []
    rows_list_bigrams = []
    rows_list_trigrams = []
    for letter in allLetters:
        row = {}
        row.update(Letter = letter, Count = allLetters[letter],Frequency = allLetters[letter] / text_len)
        rows_list_letters.append(row)

    for letter in bigrams:
        row = {}
        row.update(Bigram = letter, Count = bigrams[letter],Frequency = bigrams[letter] / text_len)
        rows_list_bigrams.append(row)

    for letter in trigrams:
        row = {}
        row.update(Trigram = letter, Count = trigrams[letter],Frequency = trigrams[letter] / text_len)
        rows_list_trigrams.append(row)

    letters_frequencies = pandas.DataFrame(rows_list_letters)
    bigrams_frequencies = pandas.DataFrame(rows_list_bigrams)
    trigrams_frequencies = pandas.DataFrame(rows_list_trigrams)
    letters_frequencies.to_csv(f"{os.path.splitext(fileName)[0]}_letters.csv")
    bigrams_frequencies.to_csv(f"{os.path.splitext(fileName)[0]}_bigrams.csv")
    trigrams_frequencies.to_csv(f"{os.path.splitext(fileName)[0]}_trigrams.csv")

    print("Успішно")

else:
    print('Введений номер файлу є не правильним, спробуйте ще раз...')
