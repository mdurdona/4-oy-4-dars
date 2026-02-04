# --------------4- dars uyga vazifa-------------
# -----------1.MASALA---------------
# class Student:
#     def __init__(self,name,student_id):
#         self.name = name
#         self.student_id = student_id
#         self.__grades = []

#     def add_grade(self,grade):
#         if 0 <= grade <= 100:
#             self.__grades.append(grade)
#         else:
#             print("Xato: Noto'g'ri baho")    

#     def calculate_average(self):
#         if len(self.__grades) == 0:
#             return 0 
#         return sum(self.__grades) / len(self.__grades)   

#     def get_status(self):
#         avr = self.calculate_average()
#         if avr >= 90:
#             return "A'lo"
#         elif avr >= 80:
#             return "Yaxshi"
#         elif avr >= 70:
#             return "Qonoqarli"
#         else:
#             return "Qoniqarsiz"


# s = Student("Durdona", "IQT-123")

# s.add_grade(85)
# s.add_grade(90)

# print(s.calculate_average())
# print(s.get_status())

# s.add_grade(150)

# -----------2.MASALA---------------
# class Employee:
#     def __init__(self,name,employee_id,hourly_rate):
#         self.name = name
#         self.employee_id = employee_id
#         self.hourly_rate = hourly_rate
#         self.__working_hours = []

#     def log_hours(self,hour):
#         if 0 <= hour <= 24:
#             self.__working_hours.append(hour)
#             return True
#         else:
#             return False

#     def total_hours(self):
#         return sum(self.__working_hours)

#     def calculate_salary(self):
#         return self.total_hours() * self.hourly_rate

#     def reset_hours(self):
#         self.__working_hours.clear()                   


# e = Employee("Durdona","IQT 123", hourly_rate = 20.0)

# print(e.log_hours(5))


# print(e.total_hours())
# print(e.calculate_salary())

# e.reset_hours()
# print(e.total_hours())
# print(e.calculate_salary())

# -----------3.MASALA---------------
# class User:
#     def __init__(self,username):
#         self.username  = username
#         self.friends = []
#     def add_friend(self,friend):
#         if friend in self.friends:
#             return False
#         self.friends.append(friend)
#         return True 

#     def remove_friend(self,friend):
#         if friend in self.friends:
#             self.friends.remove(friend)
#             return True
#         return False
#     def list_friends(self):
#         return self.friends

#     def is_friend(self, friend) :
#         return friend in self.friends

#     def mutual_friends(self, other_user: 'User'):
#         return list(set(self.friends) & set(other_user.friends))             

# user1 = User("Ali")
# user2 = User("Vali")

# print(user1.add_friend("Sami"))    # True
# print(user1.add_friend("Vali"))    # True
# print(user1.add_friend("Sami"))    # False



