print("Calculator\n")

listeditems = ["1. Addition\n" + "2. Subtraction\n" + "3. Multiplication\n" + "4. Division\n"]

for item in listeditems:
    print(item)
operation = input("Enter the number for the operation that you would like to perform.\n")

if operation == "1":
    print("Addititon\n")
    num1add = input("First Number: ")
    num2add = input("Second Number: ")
    int1add = float(num1add)
    int2add = float(num2add)
    print(int1add + int2add)
elif operation == "2":
    print("Subtraction\n")
    num1sub = input("First Number: ")
    num2sub = input("Second Number: ")
    int1sub = float(num1sub)
    int2sub = float(num2sub)
    print(int1sub - int2sub)
elif operation == "3":
    print("Multiplication")
    num1mul = input("First Number: ")
    num2mul = input("Second Number: ")
    int1mul = float(num1mul)
    int2mul = float(num2mul)
    print(int1mul * int2mul)
else:
    print("Division")
    num1div = input("First Number: ")
    num2div = input("Second Number: ")
    int1div = float(num1div)
    int2div = float(num2div)
    print(int1div / int2div)