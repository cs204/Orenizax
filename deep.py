a = input("Какой ответ на главный вопрос жизни, вселенной и всего такого? ")
match a:
    case "42" | "сорок два":
        print("Да")
    case _:
        print("Нет")
