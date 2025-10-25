##=============================ASSIGNMENTN(Question # 01)======================================##

# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year

    
#     def set_day(self, day):
#         self.day = day

#     def set_month(self, month):
#         self.month = month

#     def set_year(self, year):
#         self.year = year

    
#     def get_day(self):
#         return self.day

#     def get_month(self):
#         return self.month

#     def get_year(self):
#         return self.year

   
#     def __str__(self):
#         return f"{self.day:02d}-{self.month:02d}-{self.year % 100:02d}"



# d = Date(3, 5, 2008)
# print(d)  


# d.set_day(17)
# d.set_month(4)
# d.set_year(2007)
# print(d) 


# ##=============================ASSIGNMENT(Question # 02)======================================##


# class Date:
#     def __init__(self, day, month, year, format=1):
#         self.day = day
#         self.month = month
#         self.year = year
#         self.format = format  

    
#     def set_day(self, day):
#         self.day = day

#     def set_month(self, month):
#         self.month = month

#     def set_year(self, year):
#         self.year = year

#     def set_format(self, format):
#         self.format = format

    
#     def get_day(self):
#         return self.day

#     def get_month(self):
#         return self.month

#     def get_year(self):
#         return self.year

#     def get_format(self):
#         return self.format

    
#     def __str__(self):
#         month_names = ["January", "February", "March", "April", "May", "June",
#                        "July", "August", "September", "October", "November", "December"]
#         yy = self.year % 100  

#         if self.format == 1:
#             return f"{self.day:02d}-{self.month:02d}-{yy:02d}"   
#         elif self.format == 2:
#             return f"{self.month:02d}/{self.day:02d}/{yy:02d}"   
#         elif self.format == 3:
#             month_name = month_names[self.month - 1]
#             return f"{month_name} {self.day:02d}, {yy:02d}"      
#         else:
#             return "Invalid format"



# d = Date(25, 10, 2025)
# print(d)  

# d.set_format(2)
# print(d)  

# d.set_format(3)
# print(d) 


##=============================ASSIGNMENT(Question # 03)======================================##

# class Vehicles:
#     def __init__(self, noOfWheels, color, modelNo):
#         self.__noOfWheels = noOfWheels   
#         self.__color = color              
#         self.__modelNo = modelNo          

    
#     def set_noOfWheels(self, noOfWheels):
#         self.__noOfWheels = noOfWheels

#     def set_color(self, color):
#         self.__color = color

#     def set_modelNo(self, modelNo):
#         self.__modelNo = modelNo

   
#     def get_noOfWheels(self):
#         return self.__noOfWheels

#     def get_color(self):
#         return self.__color

#     def get_modelNo(self):
#         return self.__modelNo

    
#     def show_info(self):
#         print(f"Model No: {self.__modelNo}, Color: {self.__color}, Wheels: {self.__noOfWheels}")



# v1 = Vehicles(4, "Red", "Toyota123")
# v2 = Vehicles(2, "Blue", "Yamaha456")

# v1.show_info()
# v2.show_info()


# v1.set_color("Black")
# v1.set_noOfWheels(6)
# v1.show_info()


# print("Model Number:", v1.get_modelNo())


##=============================ASSIGNMENT(Question # 04)======================================##

# class Fraction:
#     def __init__(self, numerator, denominator):
#         self.numerator = numerator
#         self.denominator = denominator
#         self.simplify()

    
#     def simplify(self):
        
#         a = abs(self.numerator)
#         b = abs(self.denominator)
#         while b != 0:
#             a, b = b, a % b
#         gcd = a

#         self.numerator //= gcd
#         self.denominator //= gcd

        
#         if self.denominator < 0:
#             self.numerator *= -1
#             self.denominator *= -1

    
#     def __str__(self):
#         return f"{self.numerator}/{self.denominator}"

    
#     def __add__(self, other):
#         n = self.numerator * other.denominator + other.numerator * self.denominator
#         d = self.denominator * other.denominator
#         return Fraction(n, d)

#     def __sub__(self, other):
#         n = self.numerator * other.denominator - other.numerator * self.denominator
#         d = self.denominator * other.denominator
#         return Fraction(n, d)

#     def __mul__(self, other):
#         n = self.numerator * other.numerator
#         d = self.denominator * other.denominator
#         return Fraction(n, d)

#     def __truediv__(self, other):
#         n = self.numerator * other.denominator
#         d = self.denominator * other.numerator
#         return Fraction(n, d)

    
#     def __eq__(self, other):
#         return self.numerator * other.denominator == other.numerator * self.denominator

#     def __ne__(self, other):
#         return not self.__eq__(other)

#     def __gt__(self, other):
#         return self.numerator * other.denominator > other.numerator * self.denominator

#     def __lt__(self, other):
#         return self.numerator * other.denominator < other.numerator * self.denominator

#     def __ge__(self, other):
#         return self.numerator * other.denominator >= other.numerator * self.denominator

#     def __le__(self, other):
#         return self.numerator * other.denominator <= other.numerator * self.denominator



# f1 = Fraction(2, 4)
# f2 = Fraction(3, 9)

# print("f1 =", f1)
# print("f2 =", f2)
# print("Add:", f1 + f2)
# print("Sub:", f1 - f2)
# print("Mul:", f1 * f2)
# print("Div:", f1 / f2)
# print("f1 == f2:", f1 == f2)
# print("f1 > f2:", f1 > f2)


