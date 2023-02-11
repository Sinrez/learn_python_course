def format_price(price):
    try:
        price = int(price)
        return f"Цена: {price} руб."
    except ValueError as ve:
        return f'Нужно ввести число! {ve}'
    
if __name__ == '__main__':
    res = format_price(56.24)
    # res = format_price('t')
    print(res)