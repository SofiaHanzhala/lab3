word_write = str(input("Введіть речення: "))
codes = " ".join(str(ord(char)) for char in word_write)
print("Речення, що містить замість літер їх ASCII коди, виглядає так:", codes)