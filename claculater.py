

no1=input("enter the first number :");
no2=input("enter the secoond number :");
opr=input("enter the operator (+,-,*,/) :");

if(opr=='+'):
    sum=int(no1)+int(no2);
    print("sum of two numbers is",sum);
elif(opr=='-'):
    sub=int(no1)-int(no2);
    print("sub of two numbers is",sub);
elif(opr=='*'):
    mul=int(no1)*int(no2);
    print("mul of two numbers is",mul);
elif(opr=='/'):
    div=int(no1)/int(no2);
    print("div of two numbers is",div);
else:
    print("invalid operator");
