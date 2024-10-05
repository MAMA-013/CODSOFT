num1=int(input("Enter first number:- "))
num2=int(input("Enter second number:- "))
print("Please choose Operations given below:- \n" "1.Addition \n" "2.Substraction \n" "3.Multiplication \n" "4.Division \n" )
select=int(input("Please choose from 1,2,3,4: "))
if(select==1):
    print("Addition of two numbers is = ",num1+num2)
elif(select==2):
    print("Substraction of two numbers is = ",num1-num2)
elif(select==3):
    print("Multiplication of two numbrs is = ",num1*num2  )
elif(select==4):
    print("Division of two numbers is = ",num1/num2)
else:
    print("Please make a valid choice")

