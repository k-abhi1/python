#take the input parsentsge of student

#taking the input from user
percentage=int(input("enter the percentage of student:"));

#checking the percentage of student
if percentage>=90:
    print("grade is A+");
elif percentage>=80:
    print("grade is A");
elif percentage>=70:
    print("grade is B");
elif percentage>=60:
    print("grade is C");
elif percentage>=50:
    print("grade is D");
else:
    print("fail");
