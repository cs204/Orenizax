def main():
    stoimost = 50
    while stoimost > 0:
        print("Нужная сумма: " + str(stoimost))
        coin = input("Вставьте монету: ")
        if int(coin) == 50 or 20 or 10 or 5:
            stoimost = int(stoimost) - int(coin)
            if stoimost <=0:
                break
    print("Ваша сдача: " + str(stoimost * -1))
main()
