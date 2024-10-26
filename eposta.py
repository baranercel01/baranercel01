print("Welcome to our application ")
print("We will check if your email is available ")
print("If there is , we will check suitability")
print("Otherwise we will create an email adress")

def control():
    print("Do you have an email adress you currently use ? ")
    print("Yes or No")
    emailcontrol = input()
    one_letter_upper = emailcontrol.capitalize()
    if one_letter_upper == "Yes" :
        email_creation()
    elif one_letter_upper == "No" :
        email_control()
    else :
        control()


def email_creation() :
    print("Please enter your name ")
    name = input()
    print("Please enter your surname ")
    surname = input()
    print("Please enter the license plate of the "
          "city you live in")
    numberplate = input()
    new_email = name + surname +numberplate +"@" + "gmail.com"
    print(new_email)
    print("if you can like , you can this use email adress ")


def email_control():
    print("Please enter your email adress ")
    email = input()
    while not (("." in email) and ("@" in email)) :
        print("Unfortunately , this email adress is not available "
              "example = oguztasdemir@gmail.com ")
        print("Please enter a valid email adress ")
        email = input()
    if ("edu" in email ):
        print("This is unıversity email adress")

    else :
        print("Bu e posta adresi kisisel kullanım alanına uygundur ")
control()