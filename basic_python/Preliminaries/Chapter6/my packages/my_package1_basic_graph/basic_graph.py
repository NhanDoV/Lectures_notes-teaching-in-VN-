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
