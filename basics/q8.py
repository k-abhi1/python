#take the input parsentsge of student using 'and'opearator'or'opearator

#taking the input from user
english_marks=int(input("enter the percentage of student:"));
math_marks=int(input("enter the percentage of student:"));

#checking the percentage of student

if english_marks>=90 and math_marks>=90:
    print("grade is A+");

elif english_marks>=80 or math_marks>=80:
    print("grade is A");

elif english_marks>=70 or math_marks>=70:
    print("grade is B");

elif english_marks>=60 or math_marks>=60:
    print("grade is C");

elif english_marks>=50 or math_marks>=50:
    print("grade is D");

else:
    print("fail");
