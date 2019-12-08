/* HEADER FILE for Trapezoidal Rule C Program */

// Main Equation Function. This function is the graph who's area you want to estimate.
double eq1(double x) {
    // It takes one argument (x) and uses it to do maths. The example equation is below.
    return pow(x,2)*pow(M_E,x);
}

/* This function computes the part of the Trapezoidal Rule where the values of the function (eq1) must be
multiplied by 2, then added together. See the Trapezoidal Rule equation for details. */
int area2x(double start, double end, double w) {
    // Initializes variables and assings some based on what they will be used for.
    double startx = start, endx = end, h = w, a2x, areaest;
    /*  Main loop of the function, the initialization step skips the first value in the range since that is not
    multiplied by 2 in the Trap. Rule equation. It also stops one step before the final number as that one isn't
    multiplied by 2 either. The control statement is just a workaround for comparing doubles, should be self-explanatory. */
    for (startx = startx + h; fabs(startx-(endx)) > 0.000001; startx = startx + h) {
        // calls eq1() on the value of startx and * by 2. The modification step of the for loop will advance the value of startx to the next interval.
        a2x = a2x + 2*eq1(startx);
    }
    // Adds the value of a2x to the computed values of the limits of the domain. Then, applies the final step in the Trapezoidal Rule formula and displays to user via stdout.
    areaest = a2x + eq1(start) + eq1(end);
    printf("\nThe area estimate is: %5.9lf\n",areaest*0.5*w);
    return(0);
}
