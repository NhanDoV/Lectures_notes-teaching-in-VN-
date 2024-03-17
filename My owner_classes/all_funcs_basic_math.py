from math import sqrt, gcd

def fibo_by_golden_rt(a, b , n):
    """
        Tổng quát cho Fibonacci với 2 số hạng đầu lần lượt là a và b
    """
    def fibo_coef(n):
        """
            Sử dụng tỷ lệ vàng để tính Fibonacci tổng quát
        """
        n = n+1
        return int((phi**n - (1 - phi)**n) / sqrt(5))
    phi = (1 + sqrt(5)) / 2
    fa = fibo_coef(n-2)
    fb = fibo_coef(n-1)
    if n == 0:
        return a
    else:
        return (a*fa + b*fb)
    
def check_Smith_number(n):
    """
        Smith number: 4, 27, 58, 22, 121, 378, 2050918644
    """
    prime_factors = []
    N = n 
    for i in range(2, 1+n//2):        
        while N%i == 0:
            prime_factors.append(i)
            N = N // i
        if i < N:
            i = i + 1
        else:
            break
    def sum_digit(n):
        str_num = str(n)
        digit_of_num = [str_num[idx] for idx in range(len(str_num))]
        return sum([int(u) for u in digit_of_num])
    
    sum_of_input = sum_digit(n)
    sum_digit_of_num = sum([sum_digit(primef) for primef in prime_factors])

    if sum_of_input == sum_digit_of_num:
        print(f"{n} is a Smith number")
    else:
        print(f"{n} is not a Smith number")
    
def is_prime(x):
    """
        Kiểm tra số nguyên tố
    """
    prime_factors = []
    for k in range(2, x):
        if x % k == 0:
            prime_factors.append(k)
            break
    if (len(prime_factors) == 0) or (x == 2):
        return 1
    else:
        return 0
    
def triangle_type_3edges(a, b, c):
    """
        Nhập vào 3 cạnh của 1 tam giác, kiểm tra xem nó có hợp lệ hay không
    """
    if (a+b > c) * (a+c > b) * (b+c > a):
        if (a==b)*(a != c) or (a==c)*(a!=b) or (b==c)*(a!=c):
            print("Tam giác cân")
        elif (a==b)*(b==c)*(a==c):
            print("tam giác đều")
        elif (a**2+b**2 == c**2) or (a**2+c**2 == b**2) or (c**2+b**2 == a**2):
            print("tam giác vuông")
        elif (a**2+b**2 < c**2) or (a**2+c**2 < b**2) or (c**2+b**2 < a**2):
            print("tam giác tù")
        else:
            print("tam giác nhọn")            
        return 1
    else:
        print("Not a triangle")
        return 0

def triangle_area_3edges(a, b, c):
    """
        Tính diện tích của một tam giác dựa vào 3 cạnh cho trước
    """
    if triangle_type_3edges(a, b, c):
        p = (a+b+c)/2
        S = p*(p-a)*(p-b)*(p-c)
        return S**0.5
    else:
        print("Tam giác không hợp lệ")