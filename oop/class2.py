class user:
    def __init__(self,email,password):
        self.useremail=email
        self.userpassword=password
    def logout(self):
        print("logout")
firstuser=user("king@gmail.com","king123")
seconduser = user("king@gmail.com", "king123")
thirduser = user("king@gmail.com", "king123")
fourthuser = user("king@gmail.com", "king123")
print(seconduser.useremail)
firstuser.logout()
