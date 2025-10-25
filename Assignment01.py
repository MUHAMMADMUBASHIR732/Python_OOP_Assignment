# ##=============================ASSIGNMENT(Question # 01)======================================##


# import math

# class Circle:
    
#     def __init__(self, radius=1.0, color="red"):
#         self.radius = radius
#         self.color = color

    
#     def setRadius(self, r):
#         self.radius = r

#     def getRadius(self):
#         return self.radius

    
#     def setColor(self, c):
#         self.color = c

#     def getColor(self):
#         return self.color

    
#     def getCircumference(self):
#         return 2 * math.pi * self.radius

    
#     def getArea(self):
#         return math.pi * (self.radius ** 2)



# c1 = Circle()  
# print("Circle 1:")
# print("Radius:", c1.getRadius())
# print("Color:", c1.getColor())
# print("Circumference:", round(c1.getCircumference(), 2))
# print("Area:", round(c1.getArea(), 2))

# print("\n")

# c2 = Circle(5, "blue")  
# print("Circle 2:")
# print("Radius:", c2.getRadius())
# print("Color:", c2.getColor())
# print("Circumference:", round(c2.getCircumference(), 2))
# print("Area:", round(c2.getArea(), 2))


# c2.setRadius(10)
# c2.setColor("green")
# print("\nAfter updating Circle 2:")
# print("Radius:", c2.getRadius())
# print("Color:", c2.getColor())
# print("Circumference:", round(c2.getCircumference(), 2))
# print("Area:", round(c2.getArea(), 2))


# ##=============================ASSIGNMENT(Question # 02)======================================##


# class BankAccount:
    
#     def __init__(self, account_number, holder_name, balance=0.0):
#         self.account_number = account_number
#         self.holder_name = holder_name
#         self.balance = balance

    
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Deposited: {amount}")
#         else:
#             print("Deposit amount must be greater than zero.")

    
#     def withdraw(self, amount):
#         if amount > 0:
#             if amount <= self.balance:
#                 self.balance -= amount
#                 print(f"Withdrawn: {amount}")
#             else:
#                 print("Insufficient balance!")
#         else:
#             print("Withdrawal amount must be greater than zero.")

   
#     def getBalance(self):
#         return self.balance




# acc1 = BankAccount("12345", "Ali", 1000.0)

# print("Account Holder:", acc1.holder_name)
# print("Account Number:", acc1.account_number)
# print("Initial Balance:", acc1.getBalance())

# print("\n--- Performing Transactions ---")
# acc1.deposit(500)       
# acc1.withdraw(200)      
# acc1.withdraw(2000)     

# print("\nFinal Balance:", acc1.getBalance())


# ##=============================ASSIGNMENT(Question # 03)======================================##


# class BankAccount:
   
#     def __init__(self, account_number, holder_name, balance=0.0):
#         self.__account_number = account_number   
#         self.__holder_name = holder_name         
#         self.__balance = balance                 
    
#     def getAccountNumber(self):
#         return self.__account_number

#     def getHolderName(self):
#         return self.__holder_name

#     def getBalance(self):
#         return self.__balance

    
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited: {amount}")
#         else:
#             print("Deposit amount must be greater than zero.")

   
#     def withdraw(self, amount):
#         if amount > 0:
#             if amount <= self.__balance:
#                 self.__balance -= amount
#                 print(f"Withdrawn: {amount}")
#             else:
#                 print("Insufficient balance!")
#         else:
#             print("Withdrawal amount must be greater than zero.")




# acc1 = BankAccount("12345", "Ali", 1000.0)


# print("Account Holder:", acc1.getHolderName())
# print("Account Number:", acc1.getAccountNumber())
# print("Initial Balance:", acc1.getBalance())

# print("\n--- Performing Transactions ---")
# acc1.deposit(500)       
# acc1.withdraw(200)      
# acc1.withdraw(2000)    

# print("\nFinal Balance:", acc1.getBalance())


# ##=============================ASSIGNMENT(Question # 04)======================================##


# class Worker:
    
#     def __init__(self, hoursWorked=0, wageRate=0.0):
#         self.__hoursWorked = hoursWorked   
#         self.__wageRate = wageRate         

    
#     def setHoursWorked(self, h):
#         if h >= 0:
#             self.__hoursWorked = h
#         else:
#             print("Hours worked cannot be negative.")

    
#     def changeRate(self, r):
#         if r > 0:
#             self.__wageRate = r
#         else:
#             print("Wage rate must be positive.")

    
#     def pay(self):
#         return self.__hoursWorked * self.__wageRate



# w1 = Worker(40, 15)   

# print("Initial Pay:", w1.pay())

# w1.setHoursWorked(50)   
# w1.changeRate(20)       
# print("Updated Pay:", w1.pay())


# w2 = Worker()
# w2.setHoursWorked(30)
# w2.changeRate(12.5)
# print("Worker 2 Pay:", w2.pay())


# ##=============================ASSIGNMENT(Question # 05)======================================##


# class Worker:
    
#     def __init__(self, hoursWorked=0, wageRate=0.0):
#         if hoursWorked >= 0 and wageRate >= 0:
#             self.__hoursWorked = hoursWorked   
#             self.__wageRate = wageRate         
#         else:
#             print("Invalid values! Setting defaults (0, 0.0).")
#             self.__hoursWorked = 0
#             self.__wageRate = 0.0

    
#     def setHoursWorked(self, h):
#         if h >= 0:
#             self.__hoursWorked = h
#         else:
#             print("Hours worked cannot be negative.")

    
#     def changeRate(self, r):
#         if r > 0:
#             self.__wageRate = r
#         else:
#             print("Wage rate must be positive.")

    
#     def pay(self):
#         return self.__hoursWorked * self.__wageRate

    
#     def getHoursWorked(self):
#         return self.__hoursWorked

#     def getWageRate(self):
#         return self.__wageRate




# w1 = Worker()
# print("Worker 1 Pay (default):", w1.pay())


# w2 = Worker(40, 15)
# print("Worker 2 Initial Pay:", w2.pay())


# w2.setHoursWorked(50)
# w2.changeRate(20)
# print("Worker 2 Updated Pay:", w2.pay())


# ##=============================ASSIGNMENT(Question # 06)======================================##


# class Vehicles:
    
#     def __init__(self, noOfWheels=0, color="Unknown", modelNo="N/A"):
#         self.__noOfWheels = noOfWheels   
#         self.__color = color             
#         self.__modelNo = modelNo         

   
#     def getNoOfWheels(self):
#         return self.__noOfWheels

#     def getColor(self):
#         return self.__color

#     def getModelNo(self):
#         return self.__modelNo

    
#     def setNoOfWheels(self, wheels):
#         if wheels >= 0:
#             self.__noOfWheels = wheels
#         else:
#             print("Number of wheels cannot be negative.")

#     def setColor(self, color):
#         self.__color = color

#     def setModelNo(self, modelNo):
#         self.__modelNo = modelNo




# v1 = Vehicles()
# print("Vehicle 1:")
# print("Wheels:", v1.getNoOfWheels())
# print("Color:", v1.getColor())
# print("Model:", v1.getModelNo())

# print("\n")


# v2 = Vehicles(4, "Red", "Civic-2025")
# print("Vehicle 2:")
# print("Wheels:", v2.getNoOfWheels())
# print("Color:", v2.getColor())
# print("Model:", v2.getModelNo())

# print("\nUpdating Vehicle 2 attributes...")
# v2.setNoOfWheels(2)
# v2.setColor("Black")
# v2.setModelNo("Bike-150")

# print("Updated Vehicle 2:")
# print("Wheels:", v2.getNoOfWheels())
# print("Color:", v2.getColor())
# print("Model:", v2.getModelNo())


# ##=============================ASSIGNMENT(Question # 07)======================================##


# class Engine:
   
#     def __init__(self, engineNo="N/A", dateOfManufacture="Unknown"):
#         self.__engineNo = engineNo
#         self.__dateOfManufacture = dateOfManufacture

    
#     def getEngineNo(self):
#         return self.__engineNo

#     def getDateOfManufacture(self):
#         return self.__dateOfManufacture

    
#     def setEngineNo(self, engineNo):
#         self.__engineNo = engineNo

#     def setDateOfManufacture(self, date):
#         self.__dateOfManufacture = date

   
#     def display(self):
#         print(f"Engine No: {self.__engineNo}")
#         print(f"Date of Manufacture: {self.__dateOfManufacture}")



# e1 = Engine()
# print("Engine 1:")
# e1.display()

# print("\n")


# e2 = Engine("EN-12345", "2025-10-04")
# print("Engine 2:")
# e2.display()

# print("\nUpdating Engine 2 details...")
# e2.setEngineNo("EN-67890")
# e2.setDateOfManufacture("2026-01-15")
# print("Updated Engine 2:")
# e2.display()


# ##=============================ASSIGNMENT(Question # 08)======================================##


# class Int:
    
#     def __init__(self, value=0):
#         if isinstance(value, int):
#             self.__value = value
#         else:
#             raise ValueError("Value must be an integer")

    
#     def setValue(self, value):
#         if isinstance(value, int):
#             self.__value = value
#         else:
#             print("Only integer values allowed!")

    
#     def getValue(self):
#         return self.__value

    
#     def display(self):
#         print(f"Int Value: {self.__value}")

    
#     def add(self, other):
#         if isinstance(other, Int):
#             return Int(self.__value + other.__value)
#         else:
#             print("Can only add Int objects")
#             return None



# i1 = Int()
# print("Uninitialized Int (default):")
# i1.display()

# print("\n")


# i2 = Int(10)
# i3 = Int(25)
# print("Initialized Int values:")
# i2.display()
# i3.display()

# print("\nAdding i2 and i3, storing result in i1...")
# i1 = i2.add(i3)   
# i1.display()


# ##=============================ASSIGNMENT(Question # 09)======================================##


# class TollBooth:
    
#     def __init__(self):
#         self.__totalCars = 0
#         self.__totalCash = 0

    
#     def payingCar(self):
#         self.__totalCars += 1
#         self.__totalCash += 50

    
#     def nopayCar(self):
#         self.__totalCars += 1

    
#     def display(self):
#         print("\n--- TollBooth Report ---")
#         print(f"Total Cars Passed: {self.__totalCars}")
#         print(f"Total Cash Collected: Rs. {self.__totalCash}")
#         print("-------------------------")



# toll = TollBooth()

# print("TollBooth System")
# print("Press 'p' for paying car, 'n' for non-paying car, any other key to exit & show report.\n")

# while True:
#     choice = input("Enter choice (p/n/other to quit): ").lower()
#     if choice == 'p':
#         toll.payingCar()
#         print("Paying car recorded ")
#     elif choice == 'n':
#         toll.nopayCar()
#         print("Non-paying car recorded ")
#     else:
#         toll.display()
#         break


# ##=============================ASSIGNMENT(Question # 10)======================================##


# class Time:
    
#     def __init__(self, hours=0, minutes=0, seconds=0):
#         self.__hours = hours
#         self.__minutes = minutes
#         self.__seconds = seconds
#         self.__normalize()

    
#     def __normalize(self):
#         if self.__seconds >= 60:
#             self.__minutes += self.__seconds // 60
#             self.__seconds = self.__seconds % 60
#         if self.__minutes >= 60:
#             self.__hours += self.__minutes // 60
#             self.__minutes = self.__minutes % 60
#         if self.__hours >= 24:  
#             self.__hours = self.__hours % 24


#     def display(self):
#         print(f"{self.__hours:02}:{self.__minutes:02}:{self.__seconds:02}")

    
#     def addTime(self, other):
#         self.__hours += other.__hours
#         self.__minutes += other.__minutes
#         self.__seconds += other.__seconds
#         self.__normalize()



# t1 = Time(10, 59, 45)
# t2 = Time(2, 15, 30)

# print("Time 1:")
# t1.display()

# print("Time 2:")
# t2.display()


# print("\nAdding Time 2 to Time 1...")
# t1.addTime(t2)

# print("Updated Time 1:")
# t1.display()


# ##=============================ASSIGNMENT(Question # 11)======================================##


# class Angle:
    
#     def __init__(self, degrees=0, minutes=0.0, direction='N'):
#         self.__degrees = degrees
#         self.__minutes = minutes
#         self.__direction = direction

   
#     def inputAngle(self):
#         self.__degrees = int(input("Enter degrees: "))
#         self.__minutes = float(input("Enter minutes: "))
#         self.__direction = input("Enter direction (N/S/E/W): ").upper()

    
#     def display(self):
#         print(f"{self.__degrees}\u00B0{self.__minutes:.1f}' {self.__direction}")



# a1 = Angle(149, 34.8, 'W')
# print("Initialized Angle:")
# a1.display()

# print("\n--- Enter new Angles (press Ctrl+C to stop) ---")
# while True:
#     a2 = Angle()          
#     a2.inputAngle()       
#     print("You entered:", end=" ")
#     a2.display()


# ##=============================ASSIGNMENT(Question # 12)======================================##


# class Tracker:
   
#     count = 0

#     def __init__(self):
       
#         Tracker.count += 1
        
#         self.serial_number = Tracker.count

#     def report(self):
#         print(f"I am object number {self.serial_number}")



# obj1 = Tracker()
# obj2 = Tracker()
# obj3 = Tracker()

# obj1.report()  
# obj2.report()   
# obj3.report()  


# ##=============================ASSIGNMENT(Question # 13)======================================##


# class Angle:
#     def __init__(self, degrees=0, minutes=0.0, direction='N'):
#         self.degrees = degrees
#         self.minutes = minutes
#         self.direction = direction

#     def setAngle(self):
#         self.degrees = int(input("Enter degrees: "))
#         self.minutes = float(input("Enter minutes: "))
#         self.direction = input("Enter direction (N/S/E/W): ").upper()

#     def display(self):
#         return f"{self.degrees}\xB0{self.minutes:.1f}' {self.direction}"


# class Ship:
    
#     count = 0

#     def __init__(self):
#         Ship.count += 1
#         self.serial_number = Ship.count
        
#         self.latitude = Angle()
#         self.longitude = Angle()

#     def setPosition(self):
#         print(f"\nEnter position for Ship #{self.serial_number}:")
#         print("Latitude:")
#         self.latitude.setAngle()
#         print("Longitude:")
#         self.longitude.setAngle()

#     def reportPosition(self):
#         print(f"\nShip #{self.serial_number} Position:")
#         print(f"Latitude: {self.latitude.display()}")
#         print(f"Longitude: {self.longitude.display()}")



# ships = [Ship(), Ship(), Ship()]

# for ship in ships:
#     ship.setPosition()

# for ship in ships:
#     ship.reportPosition()
