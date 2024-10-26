print(" Welcome to the unıversity grade calculation application ")
print("In this application we will chech whether yo have passed the courses or not")
print("Please enter your visa note :")
vize = float(input())
print("Please enter your finall note :")
final = float(input())
def grade_calculation():
    grade = vize * 0.4 + final * 0.6
    if grade < 50 :
        print("You failed the class")
        print("You failed the class note :" + str(grade))
    else :
        print("You passed the class")
        print("You class note :" + str(grade))
grade = vize * 0.4 + final * 0.6
if final < 50 :
    print("You failed the class")
    print("You failed the class note : " + str(grade))
else :
    grade_calculation()
