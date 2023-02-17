import csv

def work_csv():
   dict = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]
   
   try:
    with open('export.csv', 'w', encoding='utf-8', newline='') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for user in dict:
            writer.writerow(user)
   except (FileExistsError, FileNotFoundError) as fe1:
      print(f'Ошибка с файлом: {fe1}')
   except Exception as ex:
      print(f'Ошибка {ex}')



if __name__ == '__main__':
    work_csv()