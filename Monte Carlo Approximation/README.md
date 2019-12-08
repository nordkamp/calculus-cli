# montecarlo-cli
The theory behind Monte Carlo approximation is, you set a domain for your function, then create a rectangle who's width will be the length of the domain
and height will be the length between the highest y value and the lowest y value. Next, generate a bunch of random points and see how many
fit underneath the curve. Then, you find out what fraction of the rectangle's whole area these approximately make up and boom, there's your answer.

A visualization can be seen below:

![MonteCarlo Example](http://barnesanalytics.com/wp-content/uploads/2017/08/figure9_3.png)

## Python version
The Python version of this program will allow you 
to input custom domains, ranges, equations and number of random points on-the-fly so you don't have to modify the source code to run a simulation.

When entering equations, use correct python syntax as if you were giving it to the intepreter, i.e. to use Euler's number you would input exp(number), for logarithms one would type log(number), powers are x\*\*y, etc.
All of your equations must be in terms of x.

An example input equation can be seen below:
```python
(x**2)*exp(x)
```

**IMPORTANT: When entering equations make sure to remember Python's order of operations!**


If you have a negative in your domain/range, make sure to encase your variable in parentheses so the order of operations is correct.
e.g.
```python
sqrt(25-(x)**2)
```
Would be what one would right for sqrt(25-x^2) if one had a negative domain, say from -5 to 5. Ensure you are inputting your equation in a way that 
Python's order of operations will be correct, otherwise you will get an incorrect answer.
## C version
Much like the Trapezoidal Rule solver, unfortunately as of now custom equation inputs are not supported in the C version. To change the equation, you will have to modify eq1() function in the MonteCarlov3.c file using proper C syntax. Some examples for different equations can be seen below:
```C
double eq1(double x) {
    return sqrt(25-pow(x,2));
}
```
for the equation sqrt(25-x^2), or
```C
double eq1(double x) {
    return pow(M_E,x)*pow(x,2);
}
```
for the equation (e^x)\*(x^2).

When compiling, remember to tell GCC or whatever compiler you use to link the required header files (stdio, stdlib, math and time).
## Installation and Usage
Clone the repository if you haven't already:
```
 $ git clone https://github.com/nordkamp/calculus-cli
 $ cd calculus-cli/
 $ cd Monte\ Carlo\ Approximation
 ```
 If you wish to use the Python version:
 ```
 $ python3 MonteCarlov3.py
```
Note: MonteCarlov1.py and MonteCarlov2.py are deprecated as they lack features/functionality and optimizations, and are only being kept in this repo for the author's historical record/use.
It is highly recommended you use version 3 instead.

Alternatively, it can be opened and run in any Python interpreter like IDLE.

Example output can be seen below:
```
$ python3 MonteCarlov3.py
Enter expression (in terms of x): sqrt(25-(x)**2)
Enter number of random points: 434343
Enter lower and upper x bounds (separated by commas): -5,5
Enter lower and upper y bounds (separated by commas): 0,5
Points inside the curve: 340730 
The area approximation is 39.22360899105085 units squared.
```

If you want to use the C version:
First, modify the equation in the source file found in the function eq1(). Then,
```
$ gcc MonteCarlov3.c -lm -o MonteCarlov3
$ ./MonteCarlov3
```
