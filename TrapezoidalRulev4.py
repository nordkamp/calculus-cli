""" Trapezoidal Rule Python version 4
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
#import required libraries
import math

def main():
    global expression
    #ask user for expression to evaluate in terms of 'z' and make it a global variable
    expression = input("Enter expression: ")
    #ask user to input starting x value (inclusive)
    startx = float(input("Enter lower bound: "))
    #ask user to input ending x value (inclusive)
    endx = float(input("Enter upper bound: "))
    #ask user to input strip number. Then, uses that to find h (or w) for the trapezium rule equation per h=(b-a)/n.
    h = float((endx-startx)/float(input('Enter strip number: ')))
    #prints out the final value. Also runs the function area2x with the parameters specified by the user, then adds the value
    #of the first and last items evaluated with the eq1 function.
    print(0.5*h*(area2x(startx, endx, h)+eq1(startx)+eq1(endx)))

def area2x(lower, upper, h):
    #Initializes the area that will be multiplied by 2
    a2x = 0
    #This will be all values for x inside the domain
    x = lower+h
    #Loop that simply checks whether or not the difference between x and upper is greater than 0.0000001, this is done
    #as a workaround for comparing float values. In a perfect world, it would actually be while x != upper, but this
    #cannot be.
    while abs(x-(upper)) > 0.000001:
        #Runs eq1() on x, then multiplies by two and adds the previous value of a2x, then stores back to a2x.
        a2x += 2*eq1(x)
        #Adds h onto the value of x.
        x += h
    #Returns the a2x var to the program.
    return a2x

#The main equation function, this is where the evaluating of the expression will happen.
def eq1(z):
    #Replaces all instances of the string "z" with the value of the variable z which was passed as a parameter. Then,
    #evaluates the expression and returns this number back to the program.
    return float(eval(expression.replace("z", str(z))))
#Calls main() to initiate the program.
main()

#18 comment lines
