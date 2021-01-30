# This is a body mass index calculator
# Author - Ross O'Reilly
# Date - 30/01/21

# References
# https://www.w3resource.com/python-exercises/python-basic-exercise-66.php

print("\n\n====================================")
print ("Body Mass Index\n\nPlease enter your details.")
print("====================================")
weight = float(input("Enter your weight in Kilograms:\t "))
height = float(input("Enter your height in Meters: \t "))
bmi = weight / (height*height)

print ("\nYour body mass index is:\t", round(bmi,2))
print("====================================")
print ("\nThank you!\n\n")