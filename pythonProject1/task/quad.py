import math


def quadratic_cal(num, num1, num2):
    # num = float(input("Enter the coefficient of x^2: "))
    # num1 = float(input("Enter the coefficient of x: "))
    # num2 = float(input("Enter the constant term: "))

    discriminant = (num1 ** 2) - (4 * num * num2)

    root1 = (-num1 + math.sqrt(discriminant)) / (2 * num)
    root2 = (-num1 - math.sqrt(discriminant)) / (2 * num)

    print(f"The roots are {root1} and {root2}")


# print(quadratic_cal(1, , 6))
if __name__ == '__main__':
    quadratic_cal(1, -5, -14)
