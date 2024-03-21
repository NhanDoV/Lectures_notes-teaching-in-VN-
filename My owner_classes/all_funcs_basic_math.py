import numpy as np
from math import sqrt, gcd, lcm, acos, asin, comb

#=============================================================================
def fibo_by_golden_rt(a, b , n):
    """
        Tổng quát cho Fibonacci với 2 số hạng đầu lần lượt là a và b
        tức là
            |-----|---------------|-------------------------------------|
            |  n  | F.standard(n) |                  F(n)               |
            |-----|---------------|-------------------------------------|
            |  0  |       1       |                   a                 |
            |  1  |       1       |                   b                 |
            |  2  |       2       |                 a + b               |
            |  3  |       3       |                 a + 2b              |
            |  4  |       5       |                2a + 3b              |
            | ... |      ...      |                  ...                |
            | k-2 |F_standard(k-2)|                                     |
            | k-1 |F_standard(k-1)|                                     |
            |  k  | F_standard(k) |a*F_standard(k-2) + b*F_standard(k-1)|
            |-----|---------------|-------------------------------------|
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
    
#=============================================================================    
def check_Smith_number(n):
    """
        Smith number: 4, 22, 27, 58, 22, 121, 378, 2050918644
        Điều kiện
            Tổng các ước số nguyên tố (dạng thừa số nguyên tố)
            bằng với
            tổng các chữ số trong chính nó
        Ví dụ
            4 = 2^2            và     0+4  = 2+2
            22 = 2 * 11        và     2+2  = 2 + (1 + 1)
            27 = 3^3           và     2+7  = 3+3+3
            58 = 2*29          và     5+8  = 2+(2+9)
            378 = 2*(3^3)*7    và    3+7+8 = 2+(3*3)+7
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
        
#=============================================================================    
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
    
#=============================================================================    
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
    
#=============================================================================
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
        
#=============================================================================
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
        
#=============================================================================
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
        
#=============================================================================
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
    
#=============================================================================    
def right_triangle_triplets(limits):
    """
        Tìm 3 cạnh a,b,c của một tam giác vuông sao cho a,b,c <= given limits
        ===================
        Example
        >> right_triangle_triplets(25)
        ..............................
                3 4 5
                8 6 10
                5 12 13
                15 8 17
                12 16 20
                7 24 25
        =====================================================================
    """
    c, m = 0, 2
    # Limiting c would limit  
    while c < limits :           
        # Now loop on n from 1 to m-1 
        for n in range(1, m) : 
            a = m * m - n * n 
            b = 2 * m * n 
            c = m * m + n * n 
  
            # if c is greater than 
            # limit then break it 
            if c > limits : 
                break
            print(a, b, c) 
        m = m + 1
        
#=============================================================================
def nCr_table(n):
    """
        In ra bảng các hệ số trong các tổ hợp khi khai triển (a + b)^n
        ================================
        Ví dụ
        >> nCr_table(5)
        ...................................................................................
                    1 2 1
                   1 3 3 1
                  1 4 6 4 1
                1 5 10 10 5 1
        >> nCr_table(20)
        ...................................................................................
                                                            1 2 1                                                     
                                                           1 3 3 1                                                    
                                                          1 4 6 4 1                                                   
                                                        1 5 10 10 5 1                                                 
                                                       1 6 15 20 15 6 1                                               
                                                     1 7 21 35 35 21 7 1                                              
                                                    1 8 28 56 70 56 28 8 1                                            
                                                 1 9 36 84 126 126 84 36 9 1                                          
                                             1 10 45 120 210 252 210 120 45 10 1                                      
                                           1 11 55 165 330 462 462 330 165 55 11 1                                    
                                         1 12 66 220 495 792 924 792 495 220 66 12 1                                  
                                     1 13 78 286 715 1287 1716 1716 1287 715 286 78 13 1                              
                                  1 14 91 364 1001 2002 3003 3432 3003 2002 1001 364 91 14 1                          
                              1 15 105 455 1365 3003 5005 6435 6435 5005 3003 1365 455 105 15 1                       
                          1 16 120 560 1820 4368 8008 11440 12870 11440 8008 4368 1820 560 120 16 1                   
                      1 17 136 680 2380 6188 12376 19448 24310 24310 19448 12376 6188 2380 680 136 17 1               
                   1 18 153 816 3060 8568 18564 31824 43758 48620 43758 31824 18564 8568 3060 816 153 18 1            
               1 19 171 969 3876 11628 27132 50388 75582 92378 92378 75582 50388 27132 11628 3876 969 171 19 1        
         1 20 190 1140 4845 15504 38760 77520 125970 167960 184756 167960 125970 77520 38760 15504 4845 1140 190 20 1 
    ===============================================================================================================================
    """
    max_length = len(' '.join([ str(comb(n, i)%10**9) for i in range(n+1)]))
    for k in range(2, n+1):
        res = ' '.join([ str(comb(k, i)%10**9) for i in range(k+1)])
        print(f"{res: ^{max_length+2}}")
        
#=============================================================================
## Ma trận lũy linh
def check_nilpotent(matrix):
    """
        Một ma trận lũy linh M phải thỏa
            - ma trận vuông 
            - tồn tại một số nguyên N sao cho M^n = 0_{n x n} (0_{n x n} tức là ma trận 0 cấp n)
        Ví dụ
            A = [[0, 1], [0, 0]] là lũy linh vì A^2 = 0
        ====================================================================
        Tuy nhiên đôi lúc chúng ta không thể sử dụng
            while n > 0:
                if M^n == 0_{n x n}
        vì nó đéo tối ưu!
        ===================================================================
        Ta có một hệ quả từ ma trận lũy linh M 
            - giả sử n là cấp của ma trận vuông M
            - khi đó tất cả các trị riêng (eigenvalue) của nó đều bằng 0 (tức là 0 là nghiệm bội n) 
        ======================================================================
        >> res=check_nilpotent([[0, 1], [0, 0]])
            lũy linh
        >> res=check_nilpotent([[2, -1], [4, -2]])
            lũy linh
        >> res=check_nilpotent([[2, 4], [-1, -2]])
            lũy linh
        >> res=check_nilpotent([[2, 4], [0, -2]])
            vuông nhưng đéo lũy linh
        >> res=check_nilpotent([[2, 4, 0], [0, -2, 1]])
            đéo vuông nên đéo care
    """    
    M = np.array(matrix)
    n_col, n_row = M.shape
    if n_col == n_row:
        eigenvalues, eigenvectors = LA.eig(M)
        # Loại trừ trường hợp các giá trị được hiển thị dưới dạng 0.000000000002
        count_zeros = [x for x in eigenvalues if np.abs(x) < 1e-9]
        if len(count_zeros) == n_col:
            print("Lũy linh")
            return 1
        else:
            print("vuông nhưng đéo lũy linh")
            return 0
    else:
        print("đéo vuông nên đéo care")
        return 0
        
#=============================================================================
# Ma trận gọi là lũy đẳng
def check_idempotent(matrix):
    """
        Một ma trận gọi là lũy đẳng (idempotent) nếu
            - nó là ma trận vuông
            - khi nhân với chính nó, sẽ cho ra chính nó
        =====================================================================
        Example
        >> res=check_idempotent([[1,0],[0,1]]) 
            Lũy đẳng
        >> res=check_idempotent([[1,2], [2,1]])
            vuông nhưng đéo lũy đẳng
        >> res=check_idempotent([[3,-6], [1,-2]])
            Lũy đẳng
        >> res=check_idempotent([[3,1], [-6,-2]])
            Lũy đẳng
        >> res=check_idempotent([[1,2,1], [0,1,-2]])
            đéo vuông nên đéo care
    """
    M = np.array(matrix)
    n_col, n_row = M.shape
    if n_col == n_row:
        mat_2 = np.matmul(matrix, matrix)
        res = (mat_2 - matrix)
        if (np.abs(res) < 1e-9).all():
            print("Lũy đẳng")
            return 1
        else:
            print("vuông nhưng đéo lũy đẳng")
            return 0
    else:
        print("đéo vuông nên đéo care")
        return 0
    
#=============================================================================
def fibo_gcd(indexes):
    """
        Cho các chỉ số trong dãy Fibonacci, tìm UCLN của giá trị tương ứng các chỉ số đó, ví dụ
        >> indexes = [2, 3, 5]
        >> fibo_gcd(indexes) = 1
        *********** Giải thích
            Fibo(2) = 1
            Fibo(3) = 2
            Fibo(5) = 5
        *******************************
        >> fibo_gcd([3,6,9,12]) = 2
        >> fibo_gcd([4*k for k in range(1,8)]) = 3
        =======================================================================================        
    """
    
    fibo_list = [fibo_by_golden_rt(1,1,idx-1) for idx in indexes]
    init_gcd = gcd(fibo_list[0], fibo_list[1]) 
    for i in range(2, len(fibo_list)):
        init_gcd = gcd(init_gcd, fibo_list[i])
    return init_gcd
#=============================================================================
def fibo_lcm(indexes):
    """
        Cho các chỉ số trong dãy Fibonacci, tìm BCNN của giá trị tương ứng các chỉ số đó, ví dụ
        >> indexes = [2, 3, 5]
        >> fibo_lcm(indexes) = 10
        *********** Giải thích
            Fibo(2) = 1
            Fibo(3) = 2
            Fibo(5) = 5
        *******************************
        >> fibo_lcm([3,6,9,12]) = 2448
        >> fibo_lcm([1,2,6,7,9]) = 1768
        =======================================================================================
    """
    
    fibo_list = [fibo_by_golden_rt(1,1,idx-1) for idx in indexes]
    init_lcm = lcm(fibo_list[0], fibo_list[1]) 
    for i in range(2, len(fibo_list)):
        init_lcm = lcm(init_lcm, fibo_list[i])
    return init_lcm

#=============================================================================
def multiples_closest(z, mod):
    """
        Returns the multiples of mod which nearest to z
        ======================================================================================
        Example
        >> multiples_closest(10, 3) = 9
        ............... vì 3*3 = 9 gần 10 hơn là 3*4
        >> multiples_closest(11, 3) = 12
        ............... vì 3*4 = 12 gần 11 hơn là 3*3
        >> multiples_closest(28, 5) = 30
        >> multiples_closest(27, 5) = 25
    """
    if mod > 0:
        low = z // mod * mod
        high = low + mod
        return low if z - low <= high - z else high
    else:
        print(f"Your calculation is invalid since the quotient {mod} must be not equal to 0!!")
        pass

#=============================================================================
def smallest_mutilple_of_9(n):
    """
        Tìm bội số nhỏ nhất của 9 sao cho chỉ chứa các digits 0 và 9 và chia hết cho n
        ==============================================================================
        Ví dụ
        >> smallest_mutilple_of_9(1)  =    9
        >> smallest_mutilple_of_9(2)  =   90
        >> smallest_mutilple_of_9(7)  =  9009
        >> smallest_mutilple_of_9(8)  =  9000
        >> smallest_mutilple_of_9(23) = 990909
        >> smallest_mutilple_of_9(31) = 999099
        ==============================================================================        
    """
    # if n is a divisor of 9 (for instance 1, 3, 9)
    if 9 % n == 0:
        return 9
    # otherwise
    # initialize a list of only 0 and 9
    li = [['0','9']]
    while True:
        # empty list of results
        nums = []
        # Generate a list of increasing digits {0, 9 | 00, 09, 90, 99 | 000, 009 ..., 990, 999 | ...}
        oldNums = li[-1]
        # Append 0 and 9 until the num % n
        for suffix in oldNums:
            nums.append('0' + suffix)

        for suffix in oldNums:
            string = '9' + suffix
            num = int(string)
            if num % n == 0:
                return num
            nums.append(string)
        li.append(nums) 
        
#=============================================================================
def lengthOfLongestSubstring(s: str):
    """
        Tìm chuỗi con dài nhất trong một chuỗi cho trước và độ dài chuỗi con đó
        ======================================================================
        Example
        >> lengthOfLongestSubstring('aabaab!bb') 
            "ab!" 
            3
        >> lengthOfLongestSubstring('abcdas')
            "abcd"
            4
        ======================================================================                
    """
    letter_to_index = {}
    max_length = 0
    substr_begin = 0
    s_ls = []
    for i, c in enumerate(s):
        cond = str(c in letter_to_index)
        if c in letter_to_index:
            substr_begin = max(letter_to_index[c] + 1, substr_begin)
            s_ls.append( (cond, max(max_length, i + 1 - substr_begin), s[i-max_length: i]) )      
        letter_to_index[c] = i
        max_length = max(max_length, i + 1 - substr_begin)
    
    if len(s) == max_length:
        substr = s
    else:
        substr = max(s_ls, key=lambda item: item[1])[-1]
        
    return substr, len(substr)

#=============================================================================
def square_by_dot(n, symb="o"):
    """
        Vẽ hình vuông bằng các ký tự     
        ================
        Example:
        >> square_by_dot(10)
                 o  o  o  o  o  o  o  o  o  o 
                 o  o  o  o  o  o  o  o  o  o 
                 o  o  o  o  o  o  o  o  o  o 
                 o  o  o  o  o  o  o  o  o  o 
                 o  o  o  o  o  o  o  o  o  o 
                 o  o  o  o  o  o  o  o  o  o 
                 o  o  o  o  o  o  o  o  o  o 
                 o  o  o  o  o  o  o  o  o  o 
                 o  o  o  o  o  o  o  o  o  o 
                 o  o  o  o  o  o  o  o  o  o 
        >> square_by_dot(3, "*")
             *  *  * 
             *  *  * 
             *  *  *
    """
    s = n*f" {symb} "
    for _ in range(n):
        print(f"{s: ^{n}}")
        
#=============================================================================        
def pine_plot(max_height=10, max_width=7):
    """
        Vẽ cây thông
        ====================
        Example
        >> pine_plot(5, 3)
                *    
               ***   
              *.*.*  
             *..*..* 
                *    
                *    
        >> pine_plot(8, 7)
                *        
               ***       
              *.*.*      
             *..*..*     
            *...*...*    
           *....*....*   
          *.....*.....*  
         *......*......* 
                *        
                *        
                *                
    """
    l = 2*max_width + 1
    print(f"{'*': ^{l+2}}")
    for _ in range(max_width):
        space = ' '*(max_width-_)
        symb_str = f"*{'.'*_}*{'.'*_}*"    
        print(f"{space: ^{max_width-_}}{symb_str: ^{_}}{space: ^{max_width-_}}")        
    if max_height > max_width + 1:        
        for _ in range(max_height - max_width):
            print(f"{'*': ^{l+2}}")
    else:
        for _ in range(3):
            print(f"{'*': ^{l+2}}")        

#=====================================================================================
def map_generate(n):
    """
        Tạo một bản đồ hình vuông với các ký hiệu
            | (wall): tường thành
            ^ (mountain): núi
            x (war.zone)
            $ (mine)
            ? (unknown)
            @ (village)
            # (river)
        -----------------------------------------------
        Example
        >> map_generate(8)
            o--------------------o
            |        |  @  #  ^  |
            |     @  |  #        |
            |  x  #              |
            |     #        #  #  |
            |  @  @              |
            |        @        @  |
            o--------------------o
        >> map_generate(30)
            o--------------------------------------------------------------------------------------o
            |  @  #     @     |        #                          #  |  ^        #     #        #  |
            |  x  ^  @  #     |        @  #  ^  $  #                 ^  #  |  x  |     #     #     |
            |     #  @        #  |  |           |  #           |           ^  #  #                 |
            |  #  ^        x     |                 @  #        @           ^  @     ^           |  |
            |        #  #  |  x              #        #  |     ^     |  #  #     |     |     #  ^  |
            |  @     #     x  #     @        #  @                    x  #     ^  x        #  #     |
            |        #     #        #        #  #     x        @     #  @  @  @              ^  @  |
            |  #  #  #  @        @  |  #  x  ^        ^  ^     |     @  #  ^        @           #  |
            |     |     ^  @  #  #        x           #  #  #  #        @     @  @  |  @     |     |
            |  @  #  x  #                 x              ^     #  @  |           #  ^  #  #        |
            |  #        #  ^  #  |  @        |  #  |  #  |     #     #  ^  |  #        $     #  #  |
            |              #     #           @     |     #  @              |  #  $  #        @  @  |
            |           #     ^  |     ^  #     |  #  @        #     $     @           @     @     |
            |              #     |  #  #     #  #  |  @     ^  @           #  |  #  |  #        #  |
            |        x  @  #  x     |     |           #  |  #     #           #  @  |     @        |
            |     #           |     ^     ^  |  |     #  |  ^     @     |           @  |  #        |
            |        @           @  #           |     ^  x        #  #  #  ^     @     |  #     #  |
            |  #     @     |  |  x  ^  |           #  ^  ^  #     ^        @     |     #  @     #  |
            |        x     ^  @        |     #     #     #  #  #  #     #  ^        ^  |        #  |
            |  #     |  |        |  @  #        $     #  #        #     |  @     @           ^  #  |
            |                          #     #  x  |  #  #  |  ^     @  |  #     #           @  @  |
            |  @  #     |                 x  #        |  @     #  #  @  #              #        #  |
            |  ^  #  |  @  ^     #        x        @  ^  |  |     ^                 x           |  |
            |     @  |  #  #              @  @           #  #  #        |  |  x     @  |  @  #     |
            |  @  |     ^  #  ^  ^     |  x  @  #  @     @        @  #  @     @  @        #     ^  |
            |     ^           #  #  #  $        |  #  #              #     $  |           |     x  |
            |     #     |  #  |           x           #  #  #  @           $              #  |     |
            |  #     #  @     |  @        #  #              |        x  #     #     x  ^  |  |     |
            o--------------------------------------------------------------------------------------o
    """
    A = np.random.choice([0,1,2,3,4,5,6], 
                         size=n*n, 
                         p=[0.5, 0.1, 0.1, 0.05, 0.04, 0.01, 0.2])
    A = np.array(A).reshape(n, n)
    A[0, :] = 1
    A[n-1, :] = 1
    A[:, 0] = 1
    A[:, n-1] = 1
    B = []
    for row in range(n):
        for col in range(n):
            if A[row, col] == 0:
                B.append(' ')
            elif A[row, col] == 2:
                B.append('@')
            elif A[row, col] == 3:
                B.append('^')
            elif A[row, col] == 4:
                B.append('x')
            elif A[row, col] == 5:
                B.append('$')
            elif A[row, col] == 6:
                B.append('#')
            else:
                B.append('|')
    B = np.array(B).reshape(n,n)
    for k in range(n):
        if (k==0) or (k==n-1):
            print(f"o{'-'*(3*(n-1) - 1)}o")
        else:
            print('  '.join(B[k]))

#=====================================================================================
def find_reminder(c1, c2, r1, r2, max_iter=5000):
    """
        Tổng quát, tìm một số nguyên dương N dư r1 sau khi chia cho c1 và dư r2 sau khi chia cho c2. 
        Nếu n lớn hơn (c1*c2) thì n chia cho (c1*c2) dư bao nhiêu?
        ****************************************************************************
        Ví dụ
            Số nguyên dương n dư 4 sau khi chia cho 6 và dư 3 sau khi chia cho 5. 
            Nếu n lớn hơn 30 thì n chia cho 30 dư bao nhiêu?
                n = 6a + 4
                n = 5b + 3
        Example
            # coefficients
            >> c1 = 6
            >> c2 = 5
            # reminders
            >> r1 = 4
            >> r2 = 3
            # result 
            >> find_reminder(6,5,4,3)
                58     28
            >> find_reminder(9,8,4,7)
                103    31
    """    
    for n in range(1, max_iter):
        N = c1*n + r1
        if (N % c2 == r2) and N>(c1*c2):
            print(N, N % (c1*c2))
            break

#=============================================================================================
def count_n_exactly_m_digits(n_digits, m_digits, start_with=7):
    """
        Tìm các số nguyên có n chữ số, số bé nhất bắt đầu bởi k sao cho chỉ có đúng m chữ số bằng nhau.
        - Ví dụ n=2, m=2, số bé nhất bắt đầu bởi 2 (tức là tối thiểu 20) thì ta có
            count([22, 33, 44, 55, 66, 77, 88, 99])
        - n=3, m=2 và số bé nhất bắt đầu bởi 9 thì ta có    
            # Nếu 2 số lặp lại là 9 thì nó sẽ có dạng "9?9" hoặc "99?"
                * 909, 919, ..., 989 (ta không tính 999 vì nó có 3 số giống nhau)
                * 991, 992, ..., 998
            # Nếu 2 số lặp lại khác nhau và được bắt đầu bởi 9 thì sẽ có dạng 9xx với x khác 9
                * 900, 911, ..., 988
            Do đó ta được 27 trường hợp
        - n=3, m=2 và số bé nhất bắt đầu bởi 7, thì
            từ 900-999 đã có 27 cases, tương tự cho 800-899 và 700-799 có 27 cases cho mỗi range này, do đó ta có 81 cases
        =========================================================
        Constraints:
            1 < n < 5
            1 < m < 4
            1 <= k <= 9
        =========================================================
        Hãy thiết lập một program tối ưu nhất
        ========================================================
        Example
        >> res = count_n_exactly_m_digits(3, 2, 7)
            Có 81 số nguyên thỏa điều kiện số nguyên 3 chữ số có đúng 2 chữ số bằng nhau và bắt đầu bởi số bé nhất là 7
            The first 10 values found is:
            ['700', '707', '711', '717', '722', '727', '733', '737', '744', '747']
        >> res = count_n_exactly_m_digits(2, 2, 7)
            Có 9 số nguyên thỏa điều kiện số nguyên 2 chữ số có đúng 2 chữ số bằng nhau và bắt đầu bởi số bé nhất là 1
            The first 10 values found is:
            ['11', '22', '33', '44', '55', '66', '77', '88', '99']
        >> res = count_n_exactly_m_digits(2, 4, 7)
            ---------------------------------------------------------------------------
            ValueError                                Traceback (most recent call last)
            Cell In[44], line 1
            ----> 1 res = count_n_exactly_m_digits(2, 4, 1)

            Cell In[43], line 37, in count_n_exactly_m_digits(n_digits, m_digits, start_with)
                35     b = 10**n_digits
                36 else:
            ---> 37     raise ValueError("m_digits phải bé hơn hoặc bằng n_digits")
                39 # Initialize the list of results
                40 passed_list = []

            ValueError: m_digits phải bé hơn hoặc bằng n_digits        
        >> res = count_n_exactly_m_digits(5, 4, 7)
            Có 55890 số nguyên thỏa điều kiện số nguyên 5 chữ số có đúng 4 chữ số bằng nhau và bắt đầu bởi số bé nhất là 1
            The first 10 values found is:
            ['10001', '10010', '10011', '10012', '10013', '10014', '10015', '10016', '10017', '10018']        
    """
    if m_digits < n_digits:
        a = start_with * 10**m_digits
        b = 10**n_digits
    elif m_digits == n_digits:
        a = start_with * 10**(m_digits - 1)
        b = 10**n_digits
    else:
        raise ValueError("m_digits phải bé hơn hoặc bằng n_digits")
    
    # Initialize the list of results
    passed_list = []
    cnt = 0
    #==================================================
    from collections import Counter
    
    for x in range(a, b):
        str_num = str(x)
        count_list = Counter([n for n in str_num])
        vals = list(count_list.values())
        if 2 in vals:
            passed_list.append(str_num)
            cnt += 1
    print(f"Có {cnt} số nguyên thỏa điều kiện số nguyên {n_digits} chữ số có đúng {m_digits} chữ số bằng nhau và bắt đầu bởi số bé nhất là {start_with}")
    print("The first 10 values found is:\n", passed_list[:10])

    return cnt

#============================================================================================
def find_all_triangle_2given_edges(a, b, min_level, max_level, n_examples=1):
    """
        Tìm tất cả các cạnh nguyên của một tam giác, biết rằng
            * 2 cạnh được biết là a, b
            * cạnh c là một số nguyên nằm trong [min_level, max_level]
        output:
            đếm số các cạnh c thỏa điều kiện trên
            in ra một số ví dụ của nó (ít nhất n_examples ví dụ)
        >> find_all_triangle_2given_edges(6, 9, 11, 16, 5)
            Có 4 tam giác có các cạnh nguyên (6, 9) và cạnh còn lại thuộc đoạn [11, 16] 
            Minh họa với n_examples : 5
            [(6, 9, 11), (6, 9, 12), (6, 9, 13), (6, 9, 14)]
        >> find_all_triangle_2given_edges(69, 96, 110, 160, 8)
            Có 51 tam giác có các cạnh nguyên (69, 96) và cạnh còn lại thuộc đoạn [110, 160] 
            Minh họa với n_examples : 8
            [(69, 96, 110), (69, 96, 111), (69, 96, 112), (69, 96, 113), (69, 96, 114), (69, 96, 115), (69, 96, 116), (69, 96, 117)]
    """
    triag_list = []
    for c in range(min_level, max_level+1):
        if (c > abs(a-b)) * (c < a+b):
            triag_list.append((a, b, c))
    triag_list.sort(key=lambda a: a[2])
    print(f"Có {len(triag_list)} tam giác có các cạnh nguyên ({a}, {b}) và cạnh còn lại thuộc đoạn [{min_level}, {max_level}] ")
    print(f"Minh họa với n_examples : {n_examples}")
    print(triag_list[:n_examples])
    
    return len(triag_list)