# Создадим новый текстовый файл

txt = open("Task1_newtxt.txt", "w", encoding="utf-8")
txt.write("Ой как долабвго я маялся абв что бы абв в файлах увидеть вместо абв каракулей абв родненькуюабв кириллицу! абв абв ")
txt.close()

# Чтение из файла

intxt = open("Task1_newtxt.txt", 'r', encoding="utf-8")
text = intxt.read()
print(f'Исходный текст:     {text}')                                       

# Преобразуем в список. Выполняем условие в функции

def del_words(str):
    str = list(filter(lambda x: 'абв' not in x, str.split()))
    return " ".join(str)

text = del_words(text)
print(f'Результат операций: {text}')

# Записываем в новый файл

txt2 = open("Task1_cortxt.txt", "w", encoding="utf-8")
txt2.write(text)
txt2.close()








