class UserAccount:
    def __init__(self, userid, balance):
        self.userid = userid
        self.balance = balance
    
    def __add__(self, other):
        # When adding two UserAccount objects, return a new one
        return UserAccount("Total", self.balance + other.balance)

    def __str__(self):
        return f"User ID: {self.userid}, Balance: {self.balance}"

user1 = UserAccount("user1", 500)
user2 = UserAccount("user2", 300)
user3 = UserAccount("user3", 200)

total_user = user1 + user2 + user3
print(total_user)        # Uses __str__
print("Total Balance:", total_user.balance)
