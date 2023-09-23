print("Task1.1")
print(f"{4} {8} {15} {16} {23} {42}")
print("Task1.2")
print(f"{4}\n{8}\n{15}\n{16}\n{23}\n{42}")
print ("Task1.3")
try:
    # Get the first number from the user
    num1 = int(input("Enter the first number: "))

    # Calculate the second and third numbers
    num2 = num1 + 1
    num3 = num1 + 2

    # Display the consecutive numbers on separate lines
    print(f"The consecutive numbers are:")
    print(num1)
    print(num2)
    print(num3)

except ValueError:
    print("Invalid input. Please enter a valid integer.")

except Exception as e:
    print(f"An error occurred: {e}")

print("Task1.4")
# Считываем три целых числа, каждое с новой строки
num1 = int(input("Введите первое целое число: "))
num2 = int(input("Введите второе целое число: "))
num3 = int(input("Введите третье целое число: "))

# Считаем сумму трех чисел
total = num1 + num2 + num3

# Выводим сумму на экран
print("Сумма трех чисел:", total)
print("Task1.5")
num=int(input("Please enter a valid integer"))
v=num*num*num
v2=6*num*num
print("cube",v)
print("surface",v2)
print("Task 2.1")
schol=int(input("schol"))
integ=int(input("integ"))
print (integ/schol)
print(integ%schol)
print("Task 2.2")
number=int(input("num"))

if 9999<number>1000:
    n1 = number // 1000
    n2 = (number // 100) % 10
    n3 = (number % 100) // 10
    n4 = number % 10
    print('Цифра в позиции тысяч равна', n1)
    print('Цифра в позиции сотен равна', n2)
    print('Цифра в позиции десятков равна', n3)
    print('Цифра в позиции единиц равна', n4)
else:
    print("ERROR")
    print("Task2.3")
    population = int(input("Enter the population of the universe: "))

    # Check if the population is even or odd
    if population % 2 == 0:
        # If the population is even, Thanos will destroy half of it
        survivors = population // 2
    else:
        # If the population is odd, Thanos will round up the number of survivors
        survivors = (population // 2) + 1

    # Display the number of survivors
    print(f"Number of survivors: {survivors}")
    print("Task 2.4")
    # Get a number as input from the user
    num = int(input("Enter a number: "))

    # Perform the left shift operation
    result = num << 1

    # Check if the result is zero
    if result == 0:
        print("Warning: The result is zero.")
    else:
        print(f"The result of the left shift (<<) operation is: {result}")
        print("task2.5")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Ask the user to choose an operation
        print("Choose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        choice = input("Enter the operation number (1/2/3/4): ")

        # Perform the selected operation and display the result
        if choice == "1":
            result = num1 + num2
            print(f"The result of addition is: {result}")
        elif choice == "2":
            result = num1 - num2
            print(f"The result of subtraction is: {result}")
        elif choice == "3":
            result = num1 * num2
            print(f"The result of multiplication is: {result}")
        elif choice == "4":
            if num2 == 0:
                print("Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"The result of division is: {result}")
        else:
            print("Invalid choice. Please enter a valid operation number (1/2/3/4).")



