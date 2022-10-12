sc = None
while sc != "Stop":
    score = float(input("Enter your score: "))
    if score < 0.0 or score > 1.0:
          print(input("Please enter a value between 0.0 and 0.1 "))
    elif score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    else:
        print("F")

    sc = input("Enter Stop to quit or any number to continue: ")                        
