import math

def solve_quadratic(a, b, c):
    if a == 0:
        print("Coefficient 'a' cannot be zero for a quadratic equation.")
        return

    delta = b**2 - 4 * a * c

    print(f"Delta = {delta}")

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Two real solutions: x1 = {x1}, x2 = {x2}")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"One real solution: x = {x}")
    else:
        real_part = -b / (2 * a)
        imag_part = math.sqrt(-delta) / (2 * a)
        print(f"No real solutions. Two complex solutions:")
        print(f"x1 = {real_part} + {imag_part}i")
        print(f"x2 = {real_part} - {imag_part}i")

if __name__ == "__main__":
    print("Quadratic Equation Solver: ax² + bx + c = 0")
    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))
        solve_quadratic(a, b, c)
    except ValueError:
        print("Invalid input! Please enter numbers only.")
