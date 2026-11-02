import math

def circle_area(radius: float) -> float:
    return math.pi * radius ** 2

if __name__ == "__main__":
    radius = float(input("Enter radius: "))
    print(f"Area of the circle: {circle_area(radius):.2f}")
