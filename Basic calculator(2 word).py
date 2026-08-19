number1 = int(input("enter your frist number : "))
sign = input("enter your operation (+, -, *, /, avg) : ")
number2 = int(input("enter your second number : "))

if sign == "+" :
    print("result : ", number1 + number2)

elif sign == "-" :
    print("result : " , number1 - number2)

elif sign == "*" :
    print("result : " , number1 * number2)

elif sign == "/" :
    print("result : " , number1 / number2)

elif sign == "avg" :
    print("result : " , (number1 + number2)/2)

else :
    print("your operation is invalid")