def armstrong_numb(num):
    lista = list(num)
    sum = 0
    for i in lista:
        sum += int(i) ** len(lista)
    
    if int(num) == sum:
        return True
    else:
        False

number = input("Enter a number: ")
result = armstrong_numb(number)


if result == True:
    print(f"{number} is an armstrong number!")
else:
    print(f"{number} is not an Armstrong number!")

    




