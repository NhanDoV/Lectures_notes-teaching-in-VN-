import numpy as np
#================================================================================================
## Ve tam giac vuong
def draw_sq_triag(level, style = '*'):
    """
        Ve tam giac vuong can!
    """
    for lv in range(level):
        print((lv + 1)*(style + ' '))
    
## Ve hinh chu nhat
def draw_rect(level_1, level_2, style = '*'):
    """
        Ve hinh chu nhat voi cap canh (level_1, level_2)
        ---------------------------------------------------
        Arguments: level_1, level_2 must be the integers
    """
    style = ' ' + style
    for k in range(level_2):
        print(level_1*style)

## Ve chu vi cua hinh chu nhat
def draw_rect_boundary(level_1, level_2, b_style = '*', i_style = ' '):
    """
    ------------------------------
        level_1, level_2 (int) : edges of the rectangle
        b_style (str) : style of the perimeters
        i_style (str) : style of the interior
    ------------------------------
        Returns : rectangle with boundary
    """
    b_style = ' ' + b_style
    i_style = ' ' + i_style
    for k in range(1, level_2 + 1):
        if (k == 1) or (k == level_2):
            print((level_1)*b_style)
        else:
            print(b_style, (level_1 - 3)*i_style, b_style)

## Ve hinh vuong chia boi hinh thoi va tam giac
def draw_splited_sqr(level, style = '*'):
    """
        Ve hinh vuong duoc chia boi hinh thoi va cac tam giac; vi du:
        level = 6
                * * * * * *
                * *     * *
                *         *
                *         *
                * *     * *
                * * * * * *
        level = 5
                * * * * *       
                * *   * *
                *       *
                * *   * *
                * * * * *
    """
    style = ' ' + style
    if level % 2 == 0:
        n = int(level / 2)
        for k in range(level):
            if k < n:
                print('%s%s%s'%((n-k)*style, 4*k*' ', (n-k)*style))
            else: ## k = n, n+1,...
                print('%s%s%s'%((k - n + 1)*style, 4*(2*n - k - 1)*' ', (k - n + 1)*style))
    else:
        n = int((level + 1) / 2)
        for k in range(level):
            if k == 0:
                print(level*style)
            elif k < n:
                print((n-k)*style, (4*(k- 1))*' ', (n-k)*style)                
            elif (k >= n) and (k < level - 1):
                print((k - n + 2)*style, 4*(level - 2 - k)*' ', (k - n + 2)*style)
            else:
                print(level*style)

## Ve cay thong!!
def draw_pine(leaf = '*', trunk = '#', n = 5, verbose = True):
    """  
    Chú thích:
        leaf (str) : biểu diễn của lá 
        trunk (str): biểu diễn gốc cây
        n (int) : chiều cao cây
        verbose (bool): = True thì sẽ in ra cây thông; ngược lại không in!
    """
    if((n < 0) | (n != int(n))):
        print('gia tri cua n khong hop le! gia tri cua n phai la so nguyen duong!!')
    else:
        if(verbose == True):
            for k in range(n+1):
                if k != n:
                    print('%s%s%s'%((n-k)*' ', (2*k+1)*leaf, (n-k)*' '))
                else:
                    print("%s%s%s"%(n*' ', trunk, n*' '))
        else:
            ## khong can lam gi
            end;

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