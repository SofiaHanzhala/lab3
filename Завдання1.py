word = str(input("Введіть слово, яке не перевищує 10 символів: "))
while (len(word) > 10):
    word = str(input("Введіть ще раз слово, так як воно перевищує 10 символів: "))
print("Після зрізу від 2-го символа з початку і до 2-го символа з кінця (2-й символ з кінця включається: ", word[2:-1])