/* Trapezoidal Rule C version 3
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
*/

#include <stdio.h>
#include <math.h>
#include "TrapezoidalRulev3.h"

//Main function that returns integer to the OS.
int main() {
    // Initializes vars, startx and endx are the upper and lower limits of the domain.
    double startx, endx, h;
    // h is used first as the strip number and then as the interval for the range as per the Trapezoidal Rule.
    // conf is simply used to confirm settings (y/n/q) later on in the program.
    char conf;
    // Takes the lower limit of the domain from stdin, stores to startx.
    printf("StartX: ");
    scanf("%lf", &startx);
    // Takes upper limit of domain from stdin, stores to endx.
    printf("EndX: ");
    scanf("%lf", &endx);
    // Takes number of strips from stdin, stores to h.
    printf("Enter number of strips: ");
    scanf("%lf",&h);
    // Does the calculation to find the interval number for the range, see Trapezoidal Rule equ. for details.
    h = ((endx-startx))/h;
    // Prints settings to stdout for user confirmation
    printf("\nStarting Value: %5.9lf\nEnding Value: %5.9lf\nThe step interval will be %5.9lf\nConfirm Settings? [y/n/q] ",startx,endx,h);
    // Takes user confirmation from stdin.
    scanf(" %c",&conf);
    // Simple decision making based on what char the user input.
    if(conf == 'y') {
        // Run the area2x function from the TrapezoidalRulev3.h file and pass startx, endx and h to it.
        area2x(startx, endx, h);
    }
    else if(conf == 'n') {
        // Recursively call main() again so that the program can restart and get new settings.
        main();
    } 
    else {
        // End the program and return 0 to the OS.
        printf("User quit.\n");
        return(0);
    }
    
}
