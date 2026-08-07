# class account:
#     __user_id = "fnkdsjfkds"
#     username = "Brajesh"


# a1 = account()
# print(a1.__user_id)
# print(a1.username)

class User:
    __user_id ="sgdfhjdsg"

    def __hello(self):
        print("This is new user")

    def myuser(self):
        self.__hello()

user1 = User()
print(user1.myuser())