#!/usr/bin/python3

import math
def main():
#Get input from user
    radius = float(input("Enter the radius: "))
    #Calculate volume and area
    volume = 4/3 * math.pi * math.pow(radius, 3)
    area = 4 * math.pi * math.pow(radius, 2)
#Output volume and area rounded to 2 decimal places
print("Volume: ", math.ceil(volume * 100)/100)
print("Area: ", math.ceil(area * 100)/100)
if __name__ == "__main__": main()