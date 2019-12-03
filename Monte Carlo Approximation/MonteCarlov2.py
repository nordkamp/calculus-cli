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
import math
from random import uniform

def main():
    # set expression and points as global vars, they are used in multiple other functions.
    global expression, points
    # Ask the user for the expression in terms of 'z' and the number of random points
    expression = input("Enter expression (in terms of z): ")
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
    # pointslist is used to store a list of points in pairs form, so the list will look like this: [(1,2), (4,3), (6,2)] etc.
    pointslist = []
    # This while loop 
    while count != points:
        pointslist.append((uniform(xlower, xupper), uniform(ylower, yupper)))
        count+=1
    return pointcheck(pointslist)
    
def pointcheck(pointslist):
    # the pointcount variable is used to store how many points have been found inside the rectangle.
    pointcount = 0
    # Uses Tuple Unpacking to loop through every set of points in the pointslist.
    for xpoint, ypoint in pointslist:
        # Essentially this is checking to see if the ypoint is underneath the function or not. If so, add one to the pointcount.
        if ypoint < eq1(xpoint) :
            pointcount += 1
        else:
            pass
    # Returns pointcount to the program.
    return pointcount

def eq1(x):
    # When called, this function takes in 'x' as an argument and evaluates the user-defined equation using its argument.
    return float(eval(expression.replace("z", str(x))))

# Calls main() to initiate the program.
main()
