name = input("Please Enter Your Name:")
print(f"Hello {name}, How are you? " )

if name=="Jack" or name=="Jackie":
    print(f"Hello {name} ")
    print(f"Goodbye {name}! ")

else:
    print("Hello Friend")

    age =int(input("How old are you? "))

if age < 18:
    print("You are below the working age ")
elif age > 18 and age < 25:
    print("You are of the right age to look for the Job ")
elif age >= 25 and age < 30:
    print("You should be having a job ")
elif age >= 30 and age < 60:
    print("Please think about having a family ")
elif age >= 60 and age < 90:
    print("Please retire ") 
else:
    print(f"Goodbye {name}! You are {age} years old. And you are an alien. ")                      