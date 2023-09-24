#!/usr/bin/env python3
# Created by: Santiago Hewett
# Date: Sep. 22,2023
# This program calculates the area and circumference of a circle


import math


def main():
    print("For a circle with a radius of 11cm:")
    print()
    print("The area is: {}cm^2".format(math.pi * (11**2)))
    print("For a circle with a radius of 11.29cm:")
    print()
    print("The circumference is: {}cm".format(2 * math.pi * 11.29))


if __name__ == "__main__":
    main()
