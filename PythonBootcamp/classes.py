# class Line:
#     def __init__(self, coor1, coor2):
#         self.coor1 = coor1
#         self.coor2 = coor2
#     def distance(self):
#         x1, y1 = self.coor1
#         x2, y2 = self.coor2
#
#         return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
#     def slope(self):
#         x1, y1 = self.coor1
#         x2, y2 = self.coor2
#
#         return (y2 - y1) / (x2 - x1)
#
#
# coordinate1 = (PythonBootcamp, 2)
# coordinate2 = (8, 10)
#
# li = Line(coordinate1, coordinate2)
#
# print(li.distance())
# print(li.slope())
#
# class Cylinder:
#     def __init__(self,height=1,radius=1):
#         self.height = height
#         self.radius = radius
#
#     def volume(self):
#         return self.height * 3.14 * (self.radius)**2
#
#     def surface_area(self):
#         top = 3.14 * (self.radius**2)
#
#         return (2*top) + (2*3.14*self.radius*self.height)
#
# my_cyl = Cylinder(2,3)
# print(my_cyl.volume())
# print(my_cyl.surface_area())


class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, dep):
        new_balance1 = self.balance + dep
        self.balance = new_balance1
        return "Deposit Accepted! Your new balance is: {}".format(new_balance1)

    def withdraw(self, wd):
        if wd > self.balance:
            return "Balance Exceeded!"

        new_balance2 = self.balance - wd
        self.balance = new_balance2
        return "Withdrawal Accepted! Your new balance is: {}".format(new_balance2)

    def __str__(self):
        return f"Account owner: {self.owner} \nAccount balance: {self.balance}"


acct1 = Account("Anca", 500)
print(acct1)
print(acct1.owner)
print(acct1.balance)
print(acct1.deposit(50))
print(acct1.withdraw(20))
print(acct1.withdraw(1000))
print(acct1.withdraw(100))