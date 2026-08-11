name = str("Bea")
print(name)

age = int(18)
print(age)

my_weight = float(75.15)
print(my_weight)

iAmIt = bool("true")
print(iAmIt)


class Profile:
    name = "Bea S. Serrano"
    age = "18"
    address = "Dinalupihan,Bataan"
    favcolor = "Blue"
    print("My name is " + name + ". " + "I am " + age + "years old from " + address + ". My favorite color is " + favcolor + ".")


class Profile:
    name = input("Enter your name:")
    age = input("Enter your age:")
    address = input("Enter your address:")
    favcolor = input("Enter your favcolor:")
    print("My name is " + name + ". " + "I am " + age + "years old from " + address + ". My favorite color is " + favcolor + ".")
