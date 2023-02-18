# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])
print(5 * '*')


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.count('a'))
print(5 * '*')


# Вывести количество гласных букв в слове
word = 'Архангельск'.lower()
print(len([c for c in word if c in 'ауоыиэяюёе']))
print(5 * '*')


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))
print(5 * '*')


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for s in sentence.split():
    print(s[0])
print(5 * '*')


# Вывести усреднённую длину слова в предложении
#Хорошо бы дать определение усредненной длины
sentence = 'Мы приехали в гости'.split()
count = sum([len(s) for s in sentence])
print(count/len(sentence))