a = input("Верблюжий стиль: ")
for c in a:
    if c.isupper():
        a = a.replace(c, "_" + c.lower())
print(a)
