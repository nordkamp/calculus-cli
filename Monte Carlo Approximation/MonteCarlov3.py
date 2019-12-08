""" Monte-Carlo Integration Approximation Python version 2
    Copyright (C) 2019 Matthew Hoffman (https://github.com/nordkamp/)
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
# import required libraries
from math import *
from random import uniform

def main():
    # set expression and points as global vars, they are used in multiple other functions.
    global expression, points
    # Ask the user for the expression in terms of 'x' and the number of random points
    expression = input("Enter expression (in terms of x): ")
    points = int(input("Enter number of random points: "))
    # Ask the user for the upper and lower range of both the x and y axis. They should be seperated by commas, i.e. 2,4 or 1,2 etc.
    xdomain, yrange = input("Enter lower and upper x bounds (separated by commas): "), input("Enter lower and upper y bounds (separated by commas): ")
    # Get the upper and lower bounds from the user input by splitting the strings by ',' then store the proper values to their own variables through list indexes.
    xlower, xupper = float(xdomain.split(',')[0]), float(xdomain.split(',')[-1])
    ylower, yupper = float(yrange.split(',')[0]), float(yrange.split(',')[-1])
    # Run the pointgen() function using xlower, xupper, ylower and yupper as arguments.
    pointcount = pointgen(xlower, xupper, ylower, yupper)
    # Calculate the area of the rectangle used in this simulation by taking the absolute value of all values, adding the x,y lowers and uppers, then doing L * W.
    area = int(abs(xlower)+abs(xupper))*(abs(ylower)+abs(yupper))
    # Prints out the final answer. The formula inside the float() statement is what actually generates the answer, it takes the number of points underneath the function, divides
    # it by the total points and then multiplies it by the area of the rectangle as per what the Monte-Carlo Integration simulation requires.
    print("Points inside the curve:", pointcount, "\nThe area approximation is", float(pointcount/points*area), "units squared.")

def pointgen(xlower, xupper, ylower, yupper):
    # This count variable is used in the loop below to limit the amount of iterations of the loop to the number of points the user entered.
    count = 0
    # pointcount is used to count the number of points under the curve.
    pointcount = 0
    # this while loop will re-evaluate until the count reaches the number of points
    while count != points:
        # Generates a random number using the y values, then compares that to eq1 evaluated using the random x point.
        if uniform(ylower, yupper) < eq1(uniform(xlower, xupper)):
            # Adds 1 to the point count if the random y value falls under the curve.
            pointcount += 1
        else:
            pass
        count+=1
    # returns the number of points to the program.
    return pointcount
    

def eq1(x):
    # When called, this function takes in 'x' as an argument and evaluates the user-defined equation using its argument.
    return float(eval(expression))

# Calls main() to initiate the program.
main()
