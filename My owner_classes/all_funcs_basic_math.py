import numpy as np
from math import sqrt, gcd, acos, asin

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

        S = sqrt(p*(p-a)*(p-b)*(p-c))
    """
    if triangle_type_3edges(a, b, c):
        p = (a+b+c)/2
        S = p*(p-a)*(p-b)*(p-c)
        return S**0.5
    else:
        print("Tam giác không hợp lệ")

def cosine_triangle_3edges(a, b, c):
    """
        By law of cosine, we have
            a^2 = b^2 + c^2 - 2*b*c*cos(c.vect, b.vect)
            b^2 = a^2 + c^2 - 2*a*c*cos(a.vect, c.vect)
            c^2 = b^2 + a^2 - 2*b*a*cos(a.vect, b.vect)    
        Denoted that
        * the angle between a,b is C
        * the angle between a,c is B
        * the angle between c,b is A        
        ================================================
        Example
        >> A,B,C = cosine_triangle_3edges(3, 3, 3)
        ................................................
            Angle between a:3 and b:3 is 60.00°
            Angle between b:3 and c:3 is 60.00°
            Angle between c:3 and a:3 is 60.00°
        ================================================
    """
    pi = np.pi
    deg_symbol = u"\u00b0"
    if triangle_type_3edges(a, b, c):
        # by radian
        C_rad = acos( -(c**2 - b**2 - a**2) / (2*b*a) )
        B_rad = acos( -(b**2 - a**2 - c**2) / (2*a*c) )
        A_rad = acos( -(a**2 - b**2 - c**2) / (2*b*c) )
        # convert radian to degree
        C = C_rad / pi * 180
        B = B_rad / pi * 180
        A = A_rad / pi * 180            
        print(f"Angle between a:{a} and b:{b} is {C:.2f}{deg_symbol}")
        print(f"Angle between b:{a} and c:{b} is {A:.2f}{deg_symbol}")
        print(f"Angle between c:{a} and a:{b} is {B:.2f}{deg_symbol}")
        return A, B, C
    else:
        print("Tam giác không hợp lệ")

def R_triangle_3edges(a, b, c):
    """ 
        We have
            a           b         c  
          ------- =  ------- = -------- = 2*R
          sin α      sin β      sin γ  
        
        where 
            * R is the radius of the triangle's circumcircle
            *  α, β, and γ are the opposite angles
        =====================================================
        Example
        >> R_triangle_3edges(3, 3, 3)
            -4.921088361605842
    """
    if triangle_type_3edges(a, b, c):
        A, B, C = cosine_triangle_3edges(a, b, c)
        R = a / (2*np.sin(A))
        return R
    else:
        print("Tam giác không hợp lệ")

def line_equation_via_2points(A, B):
    """        
        VTCP AB = (xB - xA, yB - yA)
        PT tham so: 
            x = xA + (xB-xA)*t
            y = yB + (yB-yA)*t
        PT tong quat:
            y*(yB-yA) - x*(xB-xA) + (xA*(xB-xA) - yA*(yB-yA)) = 0
        Slope: (yB - yA) / (xB - xA)
        ======================================================
        Example
        >> line_equation_via_2points([1,2], [2,1])
            ====================================================================================================
            Vecto chi phuong: (1.0, -1.0)
            ====================================================================================================
            Phuong trinh tham so di qua A:[1, 2] va B:[2, 1] la:
                x = 1.0*t + 1 
                y = -1.0*t + 2
            ====================================================================================================
            Phuong trinh tong quat di qua A:[1, 2] va B:[2, 1] la:
                -1.0*y + 1.0*x + 3 = 0
            Slope: -1.0/1.0
            ====================================================================================================
    """
    # assign coordinate
    xA, yA = A
    xB, yB = B
    # find AB.vect
    x_AB = (xB - xA)
    y_AB = (yB - yA)
    gcd_vec = gcd(x_AB, y_AB)
    x_AB = x_AB / gcd_vec
    y_AB = y_AB / gcd_vec
    # Pretify
    if x_AB > 0:
        b = x_AB
    else:
        b = -x_AB
    if (xA*(xB-xA) - yA*(yB-yA)) > 0:
        c= (xA*(xB-xA) - yA*(yB-yA))
    else:
        c = -(xA*(xB-xA) - yA*(yB-yA))
    print(100*"=")
    print(f"Vecto chi phuong: {(x_AB, y_AB)}")
    print(100*"=")
    print(f"Phuong trinh tham so di qua A:{A} va B:{B} la:\n\t x = {x_AB}*t + {xA} \n\t y = {y_AB}*t + {yA}")
    print(100*"=")
    print(f"Phuong trinh tong quat di qua A:{A} va B:{B} la:\n\t {y_AB}*y + {b}*x + {c} = 0")
    print(f"Slope: {y_AB}/{x_AB}")
    print(100*"=")