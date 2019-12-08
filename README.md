# calculus-cli
A collection of interactive and semi-interactive CLI applications to perform integration, differentiation, and approximation written in various languages (Python, C and R).

**Please note that this repository and the programs intended for it is still under construction. Complete programs can be found below.**

The purpose behind creating these applications was to be able to perform various things with custom user input (equations, domains/ranges, etc.), then to automate processes such as the Trapezoidal Rule and Monte-Carlo integration approximations.

Furthermore, these applications will allow you to complete these tasks with arbitrarily large numbers, unlike many of the website-based solutions. One could, for example, attempt the Trapezoidal Rule with 10,000,000 strips if they so desired (this might take a while depending on your computer).

**IMPORTANT: When entering equations make sure to remember Python's order of operations!**
If you have a negative domain, make sure to encase your variable in parentheses so the order of operations is correct.
e.g.
```python
sqrt(25-(x)**2)
```
Would be what one would right for sqrt(25-x^2) if one had a negative domain, say from -5 to 5. Ensure you are inputting your equation in a way that Python's order of operations will be correct, otherwise you will get an incorrect answer.

There are programs found here that can do a myriad of things under the umbrella of calculus. They are listed in sections below:

### Integration Approximation
* Trapezoidal/Trapezium Rule (Python and C)
* Monte Carlo Simulation (Python and C)

Installation and Usage instructions can be found in the README.md of each application in their respective folders.
