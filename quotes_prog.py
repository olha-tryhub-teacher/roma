
with open("quotes.txt", "r", encoding="utf-8") as bobr:
    data = bobr. read()

print(data)


answer = input("Напиши прізвище")

with open("quotes.txt", "a", encoding="utf-8") as bobr:
    bobr.write("\n" + answer)


with open("quotes.txt", "r", encoding="utf-8") as bobr:
    data = bobr. read()

print(data)
