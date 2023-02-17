"""
Прочитайте содержимое файла в переменную, подсчитайте длину получившейся строки
Подсчитайте количество слов в тексте
Замените точки в тексте на восклицательные знаки
Сохраните результат в файл referat2.txt
"""
import string

def work_file():
    try:
        try:
            with open('referat.txt', 'r', encoding='utf-8') as f:
                content = f.read()
                print(f'Длина строки: {len(content)}')
                count_words = sum([i.strip(string.punctuation).isalpha() for i in content.split()])
                print(f'Число слов в тексте: {count_words}')
                change_res = content.replace(".","!")
        except (FileExistsError, FileNotFoundError) as fe1:
            print(f'Проверить что с файлом из которого читаем {fe1}')
        
        try:
            with open('referat2.txt', 'w', encoding='utf-8') as f:
                f.write(change_res)
                print(f'Замена "." на "!" выполнена см файл referat2.txt')
        except (FileExistsError, FileNotFoundError) as fe1:
            print(f'Проверить что с файлом в который пишем {fe1}')   
    except Exception as ex:
        print(f'Что-то сломалось {ex}')

if __name__ == '__main__':
    work_file()