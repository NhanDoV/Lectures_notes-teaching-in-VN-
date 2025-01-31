import sympy as sy
from sympy import E, Eq, Function, pde_separate, Derivative as D
from sympy.solvers.pde import pdsolve
from sympy.abc import x, y, t, a, b

x, n = sy.symbols('x n')

# Define all exercises as functions
def exercise_1():
    """
    Exercise 1: Find the limit of e approximated by the limit of (1 + 1/n)^n as n approaches infinity.
    This exercise calculates the limit of (1 + 1/n)^n as n approaches infinity, which is the well-known 
    limit for the Euler's number (e).
    """
    print("Exercise 1: Find the limitation of e approximated by the limit of (1 + 1/n)^n as n approaches infinity")
    print(sy.limit((1 + 1/n)**n, n, 1e10))

def exercise_2():
    """
    Exercise 2: Derivative of x^2 with various orders.
    This exercise calculates the first and second derivatives of the function x^2 with respect to x.
    """
    for order in [1,2]:
        print(f"Exercise 2: Derivative of x^2 with order {order}:")
        print(sy.diff(x**2, x, order))
        print(90*'=')

def exercise_3():
    """
    Exercise 3: Calculate indefinite and definite integrals of 2x.
    This exercise computes the indefinite integral, as well as the definite integral of the function 2x over
    the intervals (0, 1) and (a, b).
    """
    print("Exercise 3: Indefinite integral of 2x:")
    print(sy.Integral(2*x).doit())
    print("Definite integral of 2x on (0, 1):")
    print(sy.Integral(2*x, (x, 0, 1)).doit())
    print("Definite integral of 2x on (a, b):")
    print(sy.Integral(2*x, (x, a, b)).doit())    

def exercise_4():
    """
    Exercise 4: Solve a second-order linear differential equation.
    This exercise solves the differential equation f''(x) - 2f'(x) + f(x) = 0 using sympy's dsolve function.
    """
    #========== KHAI BÁO HÀM SỐ =======
    f = sy.symbols('f', cls=sy.Function)
    #================ GIẢI PT =================
    diff_eq = sy.Eq(f(x).diff(x,x) - 2*f(x).diff(x) + f(x), 0)
    print("Exercise 4: Solving differential equation")
    print(sy.dsolve(diff_eq, f(x)))

def exercise_5():
    """
    Exercise 5: Solve a PDE using separation of variables.
    This exercise demonstrates how to solve a partial differential equation (PDE) using the separation of 
    variables technique with the 'add' and 'mul' strategies.
    """
    #========== KHAI BÁO HÀM SỐ =======
    u, X, T = map(Function, 'uXT')
    eq = Eq(D(u(x, t), x), E**(u(x, t))*D(u(x, t), t))
    print("Exercise 5: Solving PDE with separation of variables (add strategy)")
    print(pde_separate(eq, u(x, t), [X(x), T(t)], strategy='add'))

    eq = Eq(D(u(x, t), x, 2), D(u(x, t), t, 2))
    print("Exercise 5: Solving PDE with separation of variables (mul strategy)")
    print(pde_separate(eq, u(x, t), [X(x), T(t)], strategy='mul'))

def exercise_6():
    """
    Exercise 6: Solve a partial differential equation (PDE).
    This exercise solves a specific PDE using sympy's pdsolve function and demonstrates the solution for
    a nonlinear PDE.
    """
    #==============KHAI BÁO HÀM SỐ ============
    f = Function('f')
    #================ GIẢI PT =================
    u = f(x, y)
    ux = u.diff(x)
    uy = u.diff(y)
    eq = Eq(1 + (2*(ux/u)) + (3*(uy/u)), 0)
    print("Exercise 6: Solving PDE")
    print(pdsolve(eq))

# Create a function to select and run an exercise
def run_exercise():
    """
    Main function to run the math exercises game.
    This function provides a menu for the user to select an exercise by entering a number (1-6).
    Based on the user's input, the corresponding exercise function is called.
    """
    exercises = {
        "1": exercise_1,
        "2": exercise_2,
        "3": exercise_3,
        "4": exercise_4,
        "5": exercise_5,
        "6": exercise_6
    }

    print("Welcome to the math exercises game!")
    print("Choose an exercise by entering the number (1-6):")
    print("1: Find the limit of e")
    print("2: Derivative of x^2")
    print("3: Integral of 2x")
    print("4: Solve differential equation")
    print("5: Solve PDE (Separation of Variables)")
    print("6: Solve PDE (Other approach)")

    choice = input("Enter the number of the exercise you want to solve: ")

    if choice in exercises:
        exercises[choice]()  # Call the selected exercise function
    else:
        print("Invalid choice, please enter a number between 1 and 6.")

if __name__ == "__main__":
    run_exercise()
