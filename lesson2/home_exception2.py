def discounted(price, discount, max_discount=20):
    try:
        price = float(abs(price))
        discount = float(abs(discount))
        max_discount = int(abs(max_discount))
        if max_discount >= 100:
            raise ValueError('Слишком большая максимальная скидка')
        if discount >= max_discount:
            print(price, max_discount)
        else:
            print(price - (price * discount / 100))
    except TypeError:
        print("введите число!")

discounted(0400.9990, 50, 030.9999)