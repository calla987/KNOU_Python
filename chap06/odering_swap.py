# 세 수를 입력받는다.

number1 ,number2, number3 = eval(input("세수를 입력하세요. ,입력 =="))


if number1 > number2:
    number1 ,number2 = number2, number1
    
if number2 > number3:
    number2,number3 = number3,number2;
    
if number1 > number2:
    number1,numbeer2 = number2, number1
    
print ("정렬된 수는 ", number1 , number2, number3, "입니다.")   
    
        