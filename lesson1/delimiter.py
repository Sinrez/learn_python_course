def get_summ(one, two, delimiter='&'):
    return f'{one}{delimiter}{two}'.upper()

if __name__ == '__main__':
   res = get_summ("Learn", "python")
   print(res)