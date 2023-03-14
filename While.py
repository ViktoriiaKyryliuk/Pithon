def compare_and_increment(a, b, c):
    while a < b:
        a += c
        if a >= b:
            print("Уии! А теперь равно или больше В!")
            break
        else:
            print("Уии! А увеличено на C и теперь равно", a)

compare_and_increment(2, 10, 2)