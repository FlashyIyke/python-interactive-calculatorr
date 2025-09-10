#!/usr/bin/env python
# coding: utf-8

# In[ ]:


memory = 0

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): 
    return "Error: Cannot divide by zero!" if y == 0 else x / y

while True:
    print("\n--- Python Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Use Memory (last answer)")
    print("Type 'exit' to quit")

    choice = input("Enter choice: ")

    if choice.lower() == "exit":
        print("Goodbye!")
        break

    if choice == "5":
        print(f"Memory: {memory}")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        continue

    if choice == "1":
        memory = add(num1, num2)
    elif choice == "2":
        memory = subtract(num1, num2)
    elif choice == "3":
        memory = multiply(num1, num2)
    elif choice == "4":
        memory = divide(num1, num2)
    else:
        print("Invalid choice.")
        continue

    print(f"Result: {memory}")


# In[ ]:




