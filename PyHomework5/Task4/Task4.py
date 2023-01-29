
with open("Task4newdoc.txt", "w", encoding='utf-8') as doc:
    doc.write("ааааааааббВВВВВлоеееееееее")
    doc.close()

with open("Task4newdoc.txt", "r", encoding='utf-8') as txt:
    text = txt.read()
    txt.close()

def coding(txt):
    count = 1
    res = " "
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res += str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

c = coding(text)

def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res += txt[i] * int(number)
            number = " "
    return res

u = decoding(coding(text))

print(f"Исходный текст: {text}")
print(f"Результат rle кодирования = {c}")

with open ("Task4coddoc.txt", "w", encoding='utf-8') as txt_1:
    txt_1.write(str(c))
    txt_1.close()

print(f"Возврат исходного текста = {u}")

with open ("Task4uncoddoc.txt", "w", encoding='utf-8') as txt_2:
    txt_2.write(f"{u}")
    txt_2.close()