""" Trapezoidal Rule Python version 2
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
import numpy
import math
#ask user for expression to evaluate in terms of 'z'
expression = input('Enter Expression: ')
#ask user to input starting x value (inclusive)
startx = int(input('StartX: '))
#ask user to input ending x value (inclusive)
endx = int(input('EndX: '))
#ask user to input strip number. Then, uses that to find h (or w) for the trapezium rule equation per h=(b-a)/n.
h = ((endx-startx)/int(input('Enter strip number: ')))
#creates a list of numbers from the starting x value to the ending x value using h (or w) as increments. e.g. from 0-2 if startx was 0 and endx was 
#2 in increments of h (or w)
baselist = numpy.arange(startx,endx+h,h).tolist()
#defines starting value for the 2*(y1,y2,y3...yn-1) portion of the trapezium rule. It is required to be defined, so it will initially be zero.
area2x = 0
#tells program to loop through the list of numbers created before, excluding the first item and the last item.
for step in baselist[1:-1]:
    #replaces each instance of 'z' in the expression with the number it is currently up to in the list, then evaluates the expression, multiplies 
    # by 2 and adds the previous calculated number.
    area2x = 2*eval(expression.replace('z', str(step))) + area2x
#evaluates the expression for the first and last items in the list, and then adds them to the value calculated from the loop.
areaestimate = area2x+eval(expression.replace('z', str(baselist[-1])))-eval(expression.replace('z', str(baselist[0])))
#multiplies the number by h/2 as per the final step of the trapezoidal rule. Displays final calculated value to the user.
print(areaestimate*h*0.5, "units squared")
