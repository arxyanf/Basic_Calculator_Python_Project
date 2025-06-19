class EVERYTHING():
    def add():
        a = int(input("Enter the first number you want to add "))
        b = int(input("Enter the second number you want to add "))
        print(a+b)
        
    def multi():
        a = int(input("Enter the first number you want to multiply "))
        b = int(input("Enter the second number you want to multiply "))
        print(a*b)
    
    def sub():
        a = int(input("Enter the first number you want to subtract "))
        b = int(input("Enter the second number you want to subtract "))
        print(a-b)
    
    def div():
        a = int(input("Enter the first number you want to divide "))
        b = int(input("Enter the second number you want to divide "))
        print(a/b)
obj = EVERYTHING

print("Select Option")
print("1. Add Function")
print("2. Multi Function")
print("3. Sub Function")
print("4. Div Function")

choice = input("Enter the choice: ")

if choice == "1":
    obj.add()
elif choice == "2":
    obj.multi()
elif choice == "3":
    obj.sub()
elif choice == "4":
    obj.div()
else:
    print("Invalid Choice")

while True:
    obj.EVERYTHING()
    again = input("do you want to Calculate Again? (Yes/NO): ")
    if again.lower() !="yes":
        break
