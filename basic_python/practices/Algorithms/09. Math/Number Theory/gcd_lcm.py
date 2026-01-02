def gcd(a, b):
    # Thuật toán Euclid đệ quy
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Ví dụ test
if __name__ == "__main__":
    
    x = int(input("input x (integer, e.g, 4, 8, 12, etc): "))
    y = int(input("input y (integer, e.g, 6, 9, 18, etc): "))

    print(f"GCD({x},{y}) = {gcd(x,y)}")
    print(f"LCM({x},{y}) = {lcm(x,y)}")