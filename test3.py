correct_username="bobbyandrew"
correct_password="123456"

while True:
    username=(input("enter username: "))
    password=(input("enter password: "))

    if username == correct_username and password == correct_password:
     print("Login succesful")
     break
    else:
        print("wrong user and pass try again")