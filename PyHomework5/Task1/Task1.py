# Создадим новый текстовый файл

txt = open("newtxt.txt", "w", encoding="utf-8")
txt.write("Ой как долго я маялся абв что бы абв в файлах увидеть вместо абв каракулей абв родненькую кириллицу! абв абв ")
txt.close()

# Чтение из файла

intxt = open("newtxt.txt", 'r', encoding="utf-8")
text = intxt.read()
print(f'Исходный текст:     {text}')                                        # Читаем в строку
new_lst = [j for j in text.split() if j not in 'абв']                        # Изменяем строку в списке с условием
print(f'Результат операций: {" ".join(new_lst)}')                            # Выводим список через строку












