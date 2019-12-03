# trapezoidalrule-cli

These programs were written as a solution to a question on a Mathematics assignment and as such they have not been tested for ALL possible equations/scenarios. That being said, from the testing done they are accurate.

![Trapezoidal Rule formula](http://andymath.com/wp-content/uploads/2019/08/Trapezoidal-Rule.jpg)

## Python version

The latest Python version of this program requires the libraries 'math'. Install it as a prerequisite if it is not already present on your system. This version is slower than the C version but is smaller and able to take custom function inputs without modifying the source code. If you are doing large computations with lots of strips (1,000,000+) or an unreasonably complex equation, please use the C version instead, you'll thank me later.

It also is able to take custom mathematical expressions via the use of the eval() function. This function is used to execute python code stored as a string; only enter maths equations or it will break.

**THE EQUATION YOU GIVE MUST BE IN TERMS OF 'z'.**

When entering equations, use correct python syntax as if you were giving it to the intepreter, i.e. to use Euler's number you would input math.exp(number), for logarithms one would type math.log(number), powers are x\*\*y, etc. An example can be seen below:
```python
(z**2)*math.exp(z)
```

## C version
The C version of this program is much faster than the Python version given that C is a compiled language rather than an interpreted one. However, the consequence of this is that at this time, taking the function as a user input has not been implemented. Instead, one must specify the equation manually in the *TrapezoidalRulev3.h* header file, modifying the eq1() function accordingly in proper C syntax. The previous example written in C looks as such:

```C
double eq1(double x) {
    return pow(x,2)*pow(M_E,x);
}
 ```
 
 It is only necessary to change the equation after the 'return' statement. Other than that, it is able to take input for the start, end and number of strips just like the Python version.
 
 Depending on how precise, large, or small your numbers are, you might want to adjust some of the ```printf``` statements so that they display double values with larger decimal places. This can be done very simply by changing this:
 ```C
 printf("%5.9lf\n", startx);
 ```
 
 To this:
  ```C
 printf("%10.23lf\n", startx);
 ```
 Or something similar with larger/smaller numbers in all instances where ```printf``` is used.
 
 When compiling, remember to tell GCC or whatever compiler you use to link the required header files.
 
 ## Installing and Usage
 ```
 git clone https://github.com/nordkamp/calculus-cli
 cd calculus-cli/
 cd Trapezoidal\ Rule/
 ```
 If you wish to use the Python version:
 ```
 python3 TrapezoidalRulev4.py
 ```
 Note: TrapezoidalRulev2.py is deprecated as it is innacurate, and is only being kept in this repo for the author's historical record/use. It is highly recommended you use version 4 instead.
 
 Alternatively, it can be opened and run in any Python interpreter like IDLE.
 If you wish to use the C version, change the equation in the header file, then:
 ```
 cd C\ version/
 gcc TrapezoidalRulev3.c -lm -o TrapezoidalRulev3
 ./TrapezoidalRulev3
 ```
