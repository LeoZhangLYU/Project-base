from sympy import Symbol, Derivative, plot

x = Symbol('x')
y = x * x + x * 3 + 2
d = Derivative(y, x)
d.doit()
d.doit().subs({x: 10})
plot(y, (x, -10, 10))
