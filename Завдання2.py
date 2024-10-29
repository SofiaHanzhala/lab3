word = input("Напишіть слово кирилицею: ")
latin_letters = {"i", "a", "o"}
contains_latin = any(char in latin_letters for char in word)
if contains_latin:
    print("Є підміна літер латинського алфавіту")
else:
    print("Підміни літер немає")