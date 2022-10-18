def person_info(name,birth_year,weight):
   name = input("Please enter your name: ")
   if name == "":
    name = "Josie"
   weight = int(input("Please enter your weight: "))
   birth_year = 2002
   current_year =2022
   age = int(current_year - birth_year)
   print(age)

   print(f" {name} is your name, {weight} kgs is your weight and you are {age} years old ")

person_info("josephine", 23, 34 )  



