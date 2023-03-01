#illustration of classes
class Student:
    name ="mark"
    email="m@gmail.com"
    

    #methods
    # init methods self helps us identify the specific object init in fill is initialization
    def __init__(self, my_name, my_access_no,my_reg_no):
        self.my_name = my_name
        self.my_access_no = my_access_no
        self.my_reg_no = my_reg_no

student1= Student("NINA", "A998345", "S22B23/231")
print(type(student1))


    # def greeting(self):
    #     print("what is your name: ")