import random
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
from scipy.stats import t, norm
from scipy.stats import norm, t, chisquare

# =========================================== SUDOKU SQUARE =====================================================
class Sudoku:
    """
        A Sudoku generator and validator using backtracking.

            This class can:
            - Generate a valid `9 x 9` Sudoku grid using a randomized backtracking algorithm.
            - Validate rows, columns, and `3 x 3` sub-blocks.
            - Generate random invalid grids for testing (brute-force method).
            - Check if a number can be placed at a given position.

            Attributes:
                grid (list[list[int]]): A 9 x 9 Sudoku grid initialized with zeros.
    
        EXAMPLES:
            >>> GSudoku = Sudoku()
            >>> sud_mat = GSudoku.back_tracking_generate()
            >>> for row in sud_mat:
                    print(row)
            
            Output:

                        [4, 2, 5, 3, 8, 9, 1, 6, 7]
                        [3, 8, 9, 1, 6, 7, 5, 2, 4]
                        [6, 7, 1, 4, 2, 5, 9, 3, 8]
                        [8, 3, 6, 7, 1, 2, 4, 9, 5]
                        [9, 1, 4, 8, 5, 6, 2, 7, 3]
                        [7, 5, 2, 9, 4, 3, 6, 8, 1]
                        [2, 9, 7, 5, 3, 1, 8, 4, 6]
                        [5, 6, 8, 2, 7, 4, 3, 1, 9]
                        [1, 4, 3, 6, 9, 8, 7, 5, 2]            
                    
            >>> GSudoku.check_block(sud_mat), GSudoku.check_row(sud_mat), GSudoku.check_col(sud_mat)

            Output:
                        (True, True, True)

    """
    def __init__(self):
        # create a grid 9x9 of 0-values
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
            
    def random_num_gen(self) -> list[list[int]]:        
        sudoku_mat = []
        for r in range(9):
            valid_nums = list(range(1, 10))
            new_row = []
            for c in range(9):
                rand_num = random.choice(valid_nums)
                new_row.append(rand_num) 
                valid_nums.remove(rand_num)
            sudoku_mat.append(new_row)
        return sudoku_mat

    def get_dict_count(self, arr: list[int]) -> dict:
        # Initialize a count-dictionary
        hashmap = {num: 0 for num in range(1, 10)}
        for num in arr:
            if num in hashmap:
                hashmap[num] = hashmap.get(num, 0) + 1
        return hashmap
    
    def check_col(self, mat: list[list[int]]) -> bool:
        for col in range(9):
            check_arr = [mat[row][col] for row in range(9)]
            hashmap = self.get_dict_count(check_arr)
            
            # if count_max > 1 that meant exists duplicated ; otherwise return True
            if max(hashmap.values()) > 1:
                # print(f"Look at column {col + 1}; value {max(hashmap, key=hashmap.get)} has appeared {max(hashmap.values())} times")
                return False
        return True

    def check_row(self, mat: list[list[int]]) -> bool:
        for row in range(9):
            check_arr = mat[row]
            hashmap = self.get_dict_count(check_arr)
            if max(hashmap.values()) > 1:
                # print(f"Look at row {row + 1}; value {max(hashmap, key=hashmap.get)} has appeared {max(hashmap.values())} times")
                return False
        return True
    
    def check_block(self, mat: list[list[int]]) -> bool:
        # note_rows = {0: "Top", 3: "Middle", 6: "Bottom"}
        # note_cols = {0: "Left", 3: "Middle", 6: "Right"}
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                check_arr = [mat[r + i][c + j] for i in range(3) for j in range(3)]
            hashmap = self.get_dict_count(check_arr)
            if max(hashmap.values()) > 1:
                # print(f"Look at block [{r}:{r+2} x {c}:{c+2}] \t [ {note_rows[r]}-{note_cols[c]} ]")
                # for idx in range(0,9,3):
                #     print([ check_arr[idx + _] for _ in range(3)])
                # print(f"value {max(hashmap, key=hashmap.get)} has appeared {max(hashmap.values())} times")
                return False
        return True
    
    def brute_force_generate(self, max_iter: int) -> list[list[int]]:
        while max_iter > 1:
            mat = self.random_num_gen()
            res = self.check_col(mat) and self.check_block(mat)
            if res:
                return mat
            max_iter -= 1
        print(f"Can not find a valid-Sudoku by this way, please try BACKTRACKING method `back_tracking_generate` or type `help(Sudoku)` ")

    def if_valid(self, row, col, num) -> bool:
        if num in self.grid[row]:
            return False
        
        if num in [self.grid[r][col] for r in range(9)]:
            return False
        
        box_row, box_col = (row // 3)*3, (col // 3)*3
        for r in range(box_row, box_row + 3):
            for c in range(box_col, box_col + 3):
                if self.grid[r][c] == num:
                    return False
                
        return True

    def fill_val_to_grid(self) -> bool: 
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    nums = list(range(1, 10))
                    random.shuffle(nums)
                    for num in nums:
                        if self.if_valid(row, col, num):
                            self.grid[row][col] = num
                            if self.fill_val_to_grid():
                                return True
                            self.grid[row][col] = 0
                    return False
        return True
    
    def back_tracking_generate(self) -> list[list[int]]:
        self.fill_val_to_grid()
        return self.grid

# =========================================== MAGIC SQUARE =====================================================
class MagicSquare:
    """
        DEFINITION:
            - MAGIC SQUARE of order n is an `n x n` grid filled with the numbers 1 through n**2 so that 
            every row, every column, and both main diagonals each add up to the same total, 
            called the magic constant (or magic sum) M. 
            - Because it uses each integer from 1 to n² exactly once, the value of M depends only on n, 
            and has the value `n * (n**2 + 1) / 2`

        EXAMPLE:
            >>> magic_sq = MagicSquare()
            >>> mat = magic_sq.magic_sq_generate(3)
            [Output]: [[2, 7, 6], [9, 5, 1], [4, 3, 8]]

            >>> mat = magic_sq.magic_sq_generate(4)
            [Output]: [[16, 2, 3, 13], [5, 11, 10, 8], [9, 7, 6, 12], [4, 14, 15, 1]]


            >>> magic_sq.check_valid(mat)
            [Output]: True

            >>> magic_sq.check_valid([[3, 5, 7], [2, 4, 9], [6, 1, 8]])
            [Output]: False

    """
    def random_generate_matrix(self, n_dim: int) -> list[list[int]]:
        valid_nums = list(range(1, 1 + n_dim**2))
        pseduo_sq = []
        for _ in range(n_dim):
            new_row = []
            for _ in range(n_dim):
                rand_num = random.choice(valid_nums)
                new_row.append(rand_num)
                valid_nums.remove(rand_num)
            pseduo_sq.append(new_row)

        return pseduo_sq

    def get_valid_sum(self, n_dim: int) -> int:
        return (n_dim**2 + 1)*n_dim // 2

    def check_rows(self, mat: list[list[int]], n_dim: int) -> bool:
        for r in range(n_dim):
            if sum(mat[r]) != self.get_valid_sum(n_dim):
                return False
        return True

    def check_cols(self, mat: list[list[int]], n_dim: int) -> bool:
        for col in range(n_dim):
            col_to_check = []
            for row in range(n_dim):
                col_to_check.append( mat[col][row] )
            if sum(col_to_check) != self.get_valid_sum(n_dim):
                return False
        return True

    def check_diag(self, mat: list[list[int]], n_dim: int) -> bool:
        left_diag, right_diag = 0, 0
        valid_sum = self.get_valid_sum(n_dim)
        for r in range(n_dim):
            left_diag += mat[r][r]
            right_diag += mat[r][n_dim - r - 1]
        if (left_diag == valid_sum) and (right_diag == valid_sum):
            return True
        else:
            return False

    def check_valid(self, mat: list[list[int]]) -> bool:
        n_row, n_col = len(mat), len(mat[0])
        if n_row != n_col:
            return False
        else:
            valid_sum = self.get_valid_sum(n_row)
            if self.check_rows(mat, n_row) and self.check_cols(mat, n_row) and self.check_diag(mat, n_row):
                return True
            else:
                return False

    def brute_force_trials(self, n_dim: int, max_iter: int) -> list[list[int]]:
        if (n_dim <= 4) and (max_iter < 1e9 ) and (max_iter > 1):
            for iter in range(max_iter):
                mat = self.random_generate_matrix(n_dim)
                if self.check_rows(mat, n_dim) and self.check_cols(mat, n_dim) and self.check_diag(mat, n_dim):
                    print(f"Success at iter = {iter + 1}")
                    return mat
        else:
            print("this method is only for small dimension (3 or 4) and max_iter is lower than 1e9")
            return None

    def siamase_rule(self, n_dim: int) -> list[list[int]]:
        # initialize magic square
        mat = [[0 for _ in range(n_dim)] for _ in range(n_dim)]

        # Initialize position for 1
        i = n_dim // 2
        j = n_dim - 1

        # One by one put all values in magic square
        for num in range(1, n_dim**2 + 1):

            # put the current element at (i, j)
            mat[i][j] = num

            # if we get multiple of n, move left
            if num % n_dim == 0:
                j -= 1

            # else move to top-right
            else:
                i -= 1
                j += 1

            # add n and take modulo to avoid out of bounds
            i = (i + n_dim) % n_dim
            j = (j + n_dim) % n_dim

        return mat

    def doublyEven(self, n_dim: int) -> list[list[int]]:
        # 2-D matrix with all entries as 0
        mat = [[(n_dim * y) + x + 1 for x in range(n_dim)] 
                for y in range(n_dim)
              ]

        # Change value of array elements at fix location as per the rule (n*n+1)-arr[i][[j]        
        # Corners of order (n/4)*(n/4)
        # Top left corner
        for i in range(0, n_dim//4):
            for j in range(0, n_dim//4):
                mat[i][j] = (n_dim**2 + 1) - mat[i][j]
        
        # Top right corner
        for i in range(0, n_dim//4):
            for j in range(3 * (n_dim//4), n_dim):
                mat[i][j] = (n_dim**2 + 1) - mat[i][j]

        # Bottom Left corner
        for i in range(3 * (n_dim // 4), n_dim):
            for j in range(0, n_dim//4):
                mat[i][j] = (n_dim**2 + 1) - mat[i][j]
        
        # Bottom Right corner
        for i in range(3 * (n_dim//4), n_dim):
            for j in range(3 * (n_dim//4), n_dim):
                mat[i][j] = (n_dim**2 + 1) - mat[i][j]
                
        # Centre of matrix,order (n/2)*(n/2)
        for i in range(n_dim//4, 3 * (n_dim//4)):
            for j in range(n_dim//4, 3 * (n_dim//4)):
                mat[i][j] = (n_dim**2 + 1) - mat[i][j]

        return mat

    def magic_sq_generate(self, n_dim):
        if n_dim % 2 == 1:
            return self.siamase_rule(n_dim)
        else:
            return self.doublyEven(n_dim)

# =========================================== CONVERT OPERATOR =================================================
class Convert:
    """
        A collection of converter functions between decimal, binary, ASCII, and Excel-style indices.
    """
    # From decimal to other forms
    def from_decimal(self, form: str, num: int) -> str:
        """
            Convert a decimal number to a target number system.

            Supported forms:
                - "bin" : binary (base 2)
                - "oct" : octal (base 8)
                - "hex" : hexadecimal (base 16)

            Examples:
                dec=8,  form="bin" --> "1000"
                dec=15, form="hex" --> "F"
                dec=31, form="hex" --> "1F"

            Args:
                form (str): Target format ("bin", "oct", "hex").
                num (int): Decimal integer to convert.

            Returns:
                str: Converted representation in the target system.

            Raises:
                ValueError: If `form` is not supported.
        """
        base_dict = {'bin':2, 'oct': 8, 'hex': 16}
        if form not in base_dict:
            raise ValueError("Form must be one of: 'bin', 'oct', 'hex'.")

        base = base_dict[form]

        # digits for hex
        digits = "0123456789ABCDEF"

        if num == 0:
            return "0"

        result = []
        # here output is string (to easier handle the hexan)
        while num > 0:                          # in case your output is an integer, change it to
            reminder = num % base               # update your target
            result.append(digits[reminder])     #                   target += reminder * (base ** deg)
            num //= base                        #                   num //= base        deg += 1

        return ''.join(reversed(result))

    # From binary to other forms
    def from_binary(self, form: str, num: str) -> str:
        """
            Convert a binary number into another number system.

            Supported forms:
                - "dec" : decimal
                - "oct" : octal
                - "hex" : hexadecimal

            Examples:
                binary 110 -> dec 6
                binary 1111 -> hex "F"
                binary 100000 -> oct "20"

            Args:
                form (str): Target format ("dec", "oct", "hex").
                num (int): Binary number represented as an integer (e.g., 1011).

            Returns:
                str: Converted value in the requested format.

            Raises:
                ValueError: If form is invalid or num contains non-binary digits.
        """
        base_dict = {"dec": 10, "oct": 8, "hex": 16}
        if form not in base_dict:
            raise ValueError("Form must be one of: 'dec', 'oct', 'hex'.")

        # --- validate binary input ---
        if any(d not in "01" for d in str(num)):
            raise ValueError("Input must be a binary number (only 0 and 1).")

        # --- Step 1: binary → decimal ---
        dec_val = 0
        deg = 0
        tmp = num

        while tmp > 0:
            dec_val += (tmp % 10) * (2 ** deg)
            tmp //= 10
            deg += 1

        # if output is decimal → return int
        if form == "dec":
            return str(dec_val)

        # --- Step 2: decimal → oct or hex ---
        digits = "0123456789ABCDEF"
        base = base_dict[form]

        result = []
        temp = dec_val

        while temp > 0:
            result.append(digits[temp % base])
            temp //= base

        return ''.join(reversed(result))

    def from_hex(self, form: str, num: str) -> str:
        """
            Convert a hexadecimal number into another number system.

            Supported forms:
                - "dec" : decimal
                - "bin" : binary
                - "oct" : octal

            Examples:
                hex "1F"   -> dec "31"
                hex "A3"   -> bin "10100011"
                hex "FF"   -> oct "377"

            Args:
                form (str): Target number system ("dec", "bin", "oct").
                num (str): Hexadecimal string using digits 0–9 and A–F.

            Returns:
                str: Converted number as a string.

            Raises:
                ValueError: If form is invalid or input contains invalid hex characters.
        """
        base_dict = {"dec": 10, "bin": 2, "oct": 8}

        if form not in base_dict:
            raise ValueError("Form must be one of: 'dec', 'bin', 'oct'.")

        # Validate hex input
        num = num.upper()
        if any(ch not in "0123456789ABCDEF" for ch in num):
            raise ValueError("Input must be a valid hexadecimal string.")

        # Step 1: hex → decimal
        dec_val = 0
        for ch in num:
            dec_val = dec_val * 16 + int(ch, 16)

        if form == "dec":
            return str(dec_val)

        # Step 2: decimal → target (bin or oct)
        digits = "0123456789ABCDEF"
        base = base_dict[form]

        result = []
        temp = dec_val

        if temp == 0:
            return "0"

        while temp > 0:
            result.append(digits[temp % base])
            temp //= base

        return ''.join(reversed(result))

    def from_oct(self, form: str, num: int) -> str:
        """
            Convert an octal number into another number system.

            Supported forms:
                - "dec" : decimal
                - "bin" : binary
                - "hex" : hexadecimal

            Examples:
                oct 17    -> dec "15"
                oct 20    -> bin "10000"
                oct 377   -> hex "FF"

            Args:
                form (str): Target number system ("dec", "bin", "hex").
                num (int): Octal number represented as an integer (digits 0–7).

            Returns:
                str: Converted number as a string.

            Raises:
                ValueError: If form is invalid or num is not valid octal.
        """
        base_dict = {"dec": 10, "bin": 2, "hex": 16}

        if form not in base_dict:
            raise ValueError("Form must be one of: 'dec', 'bin', 'hex'.")

        # Validate oct input
        if any(ch not in "01234567" for ch in str(num)):
            raise ValueError("Input must be a valid octal number (digits 0–7).")

        # Step 1: oct → decimal
        dec_val = 0
        for ch in str(num):
            dec_val = dec_val * 8 + int(ch)

        if form == "dec":
            return str(dec_val)

        # Step 2: decimal → target (bin or hex)
        digits = "0123456789ABCDEF"
        base = base_dict[form]

        result = []
        temp = dec_val

        if temp == 0:
            return "0"

        while temp > 0:
            result.append(digits[temp % base])
            temp //= base

        return ''.join(reversed(result))

    def to_excelNums(self, columnIndex: str) -> int:
        """
            Convert an Excel-style column label into its corresponding numeric index.

            Examples:
                "A"  -> 1
                "Z"  -> 26
                "AA" -> 27
                "AB" -> 28

            Args:
                columnIndex (str): Excel column label. Must be uppercase A–Z characters.

            Returns:
                int: The corresponding Excel column index.

            Raises:
                ValueError: If the input is not uppercase alphabetic.
        """
        if columnIndex.isalpha() and columnIndex.isupper():
            res = 0
            for letter in columnIndex:
                res = res * 26 + (ord(letter) - 64)
            return res
        else:
            raise ValueError("Input must be uppercase and contain only alphabet letters.")


    def to_exlcelIndex(self, columnNumber: int) -> str:
        """
            Convert a numeric index into its corresponding Excel-style column label.

            Examples:
                1  -> "A"
                5  -> "E"
                26 -> "Z"
                27 -> "AA"
                52 -> "AZ"

            Args:
                columnNumber (int): Positive column number (>= 1).

            Returns:
                str: Excel column label.

            Raises:
                ValueError: If columnNumber is not a positive integer.
        """
        result = []
        while columnNumber > 0:
            columnNumber -= 1
            result.append( chr(columnNumber % 26 + 65) )
            columnNumber //= 26
        return ''.join(reversed(result))

# ========================================= Timestamps puzzle ==================================================
class Special_TimeStamps:
    """
        Summary:
            ------------------------------
                Func 1: Find all timestamps-format YYYYMMDD such that there exists an integer num such that num**pow = YYYYMMDD
                
                >>> sol = Special_TimeStamps()
                >>> sol.datetime_is_power_num(2, 1990, 2025)                 
                Output:
                        1990-May-21 since 4461^2 = 19900521
                        2015-Nov-21 since 4489^2 = 20151121
                        2024-Oct-01 since 4499^2 = 20241001
                
                >>> sol.datetime_is_power_num(3, 1990, 2025)
                Output:
                        From 1990 to 2025, there doesnt exist any integer such that num^3 
                
                >>> sol.datetime_is_power_num(4, 1990, 2025)
                Output:
                        2015-Nov-21 since 67^4 = 20151121
                                        
            ------------------------------
                Func 2: Find all 13-Fri in a given years
            ------------------------------
                Func 3: A date is palindromic if the digits read the same forwards and backwards
            ------------------------------
                Func 4: primes date
            ------------------------------
                Func 5: Labour date is a weekend
    """
    def if_valid_timestamps(self, timestamp: str) -> bool:
        try:
            datetime.strptime(timestamp, "%Y%m%d")
            return True
        except:
            return False

    def is_prime(self, num: int) -> bool:
        if num == 2:
            return True
        for factor in range(2, int(num**0.5) + 1):
            if num % factor == 0:
                return False
        return True

    def datetime_is_power_num(self, pow: int, count_from: int, lookback_year: int):
        cnt = 0
        for year in range(count_from, lookback_year + 1):
            for month in range(1, 13):
                for day in range(1, 32):
                    ts_str = f"{year}{month:02d}{day:02d}"
                    if sol.if_valid_timestamps(ts_str):
                        res = int(ts_str)**(1 / pow)
                        if res == int(res):
                            print(f"{datetime.strptime(ts_str, '%Y%m%d').strftime('%Y-%b-%d')} since {int(res)}^{pow} = {ts_str}")
                            cnt += 1
        if cnt == 0:
            print(f"From {count_from} to {lookback_year}, there doesnt exist any integer such that num^{pow} ")

    def check_Fri_13(self, year: int):
        cnt = 0
        for month in range(1, 13):
            ts_str = f"{year}{month:02d}13"
            if self.if_valid_timestamps(ts_str):
                dt = datetime.strptime(ts_str, "%Y%m%d")
                res = dt.strftime("%a-%d-%b-%Y")
                if res.split("-")[0] == 'Fri':
                    print(f"{ts_str} is {res}")
                    cnt += 1
        if cnt == 0:
            print(f"In {year} there is no Fri-13")

    def palindromic_date(self, count_from: int, lookback_year: int):
        cnt = 0
        for year in range(count_from, lookback_year + 1):
            for month in range(1, 13):
                for day in range(1, 32):
                    ts_str = f"{year}{month:02d}{day:02d}"
                    # check if date is valid & it is equals to its reverse value
                    if self.if_valid_timestamps(ts_str) and ts_str == ts_str[::-1]:
                        dt = datetime.strptime(ts_str, "%Y%m%d")
                        print(f"{dt.strftime("%d-%m-%Y")} or {ts_str} is palindromic")
                        cnt += 1
        if cnt == 0:
            print(f"From {count_from} to {lookback_year} there is no any datetime is palindromic")

    def prime_date(self, year: int):
        res_dates = []
        for month in range(1, 13):
            for day in range(1, 32):
                ts_str = f"{year}{month:02d}{day:02d}"
                # check if the input date is valid timestamps and also is a prime
                if self.if_valid_timestamps(ts_str) and self.is_prime(int(ts_str)):
                    dt = datetime.strptime(ts_str, "%Y%m%d")
                    res_dates.append(f"{dt.strftime("%d-%m-%Y")} ({ts_str})")
        if len(res_dates) == 0:
            print(f"In {year} there is no any datetime is a prime")
        return res_dates    

    def labour_dt_is_wk(self, count_from: int, lookback_year: int):
        cnt = 0
        for year in range(count_from, lookback_year + 1):
            ts_str = f"{year}0501"
            if self.if_valid_timestamps(ts_str):
                dt = datetime.strptime(ts_str, "%Y%m%d")
                res = dt.strftime("%a-%d-%b-%Y")
                if res.split("-")[0] in ["Sat", "Sun"]:
                    print(f"{ts_str} is {res}")
                    cnt += 1
        if cnt == 0:
            print(f"In {year} there is no Labour day is weekend from {count_from} to {lookback_year} ")

# ====================================== SOME PROBA-STATS SIMULATIONS ==========================================
class ProbaStatSims:
    """
        Some simulations come from the well-known puzzles 
    """
    # Problem 1.
    def balance_event_from_biased_coin(self, q: float, prob_H: float, n_sims: int) -> int:
        """
            Generate an event with probability q using only an unfair coin.

            This function shows how to convert a biased coin (Head with probability prob_H) into an unbiased coin using the Von Neumann trick, 
            and then how to use fair bits to construct a uniform random variable U ~ Uniform(0,1). The event returned is:
                        1   if   U < q
                        0   otherwise

            Args:
                q (float): Target probability for the event (0 <= q <= 1).
                prob_H (float): Probability that the unfair coin returns Head.
                n_sims (int): Number of fair bits used to approximate U.

            Returns:
                int: 1 with probability approximately q, otherwise 0.
            
            Application:
                Given a unfair coin with p_head, how can we simulate an event with equal-proba (or even the desired proba)
            
            Example:
                >>> sol = ProbaStatSims()
                >>> cnt = 0
                >>> q = 0.25
                >>> n_sims = 320
                >>> N = 1000
                >>> for _ in range(N):
                        cnt += sol.balance_event_from_biased_coin(q, 0.8, n_sims)
                >>> print(cnt / N)   # ≈ 0.25

        """
        # ========================== Define support functions ======================
        def unfair_coin(prob_H: float) -> int:
            # 1 for Head and 0 for Tail
            return 1 if random.random() < prob_H else 0

        def make_fair_coint(prob_H: float) -> int:        
            while True:
                a = unfair_coin(prob_H)
                b = unfair_coin(prob_H)
                if a == 1 and b == 0:
                    return 1
                elif a == 0 and b == 1:
                    return 0
        # ===============================================================================
        # Step 1: Build a uniform [0,1) random number using fair bits
        u = 0.0
        for i in range(n_sims):
            bit = make_fair_coint(prob_H)
            u += bit * (0.5 ** (i + 1))
        # Step 2: Compare to q
        return 1 if u < q else 0

    # Problem 2.
    def prob_to_meet_a_triangle_from_stick(self, n_sims: int, max_iter: int) -> float:
        """
            Estimate the probability that a randomly broken stick forms a triangle.

            A unit stick is broken into three pieces by choosing two independent, uniformly distributed cut points in (0,1).  
            Let the resulting segment lengths be a, b, c. The three segments form a triangle iff:

                    a + b > c
                    a + c > b
                    b + c > a

            This simulation repeats the experiment max_iter times for each of n_sims outer simulations, and averages the estimated probabilities.

            Args:
                n_sims (int): Number of independent simulations to average over.
                max_iter (int): Number of stick-break experiments per simulation.

            Returns:
                float: Estimated probability that three random segments form a triangle.
                    The true theoretical value is 1/4.

            Example:
                >>> sol = ProbaStatSims()
                >>> sol.prob_to_meet_a_triangle_from_stick(200, 10000)
                0.2492    # close to 0.25
        """
        def valid_triangle(a: float, b: float, c: float) -> bool:
            return (a + b > c) & (a + c > b) & (b + c > a)

        probs = []
        for _ in range(n_sims):
            cnt = 0
            for _ in range(max_iter):
                # First, define 2 random points on the interval (0, 1)
                ab = np.sort(np.random.uniform(0, 1, 2))
                # The two random cut points divide the stick into 3 parts:
                # segment a (from 0 to first cut), segment b (between cuts), and segment c (from second cut to end)
                a = ab[0]
                b = ab[1] - ab[0]
                # the last one
                c = 1 - (a + b)
                # check if them formed a triangle
                if valid_triangle(a, b, c):
                    cnt += 1
            probs.append(cnt / max_iter)
        return sum(probs) / n_sims
    
    # Problem 3.
    def expected_cost(self, a: float, b: float, X: float, Y: float,  
                      n_sims: int = 1000, seed: int|None = None) -> float:
        """
            Compute the analytic optimal forecast under asymmetric linear loss for
            B ~ Uniform(a, b), then estimate expected cost by Monte Carlo.

            Loss definition:
                loss(g, b) = X * max(g - b, 0) + Y * max(b - g, 0)

            For asymmetric absolute loss the minimiser is the quantile F(g*) = Y/(X+Y).
            For Uniform(a, b) this gives:
                g* = a + (Y / (X + Y)) * (b - a)

            Args:
                a (float): left endpoint of the uniform distribution.
                b (float): right endpoint of the uniform distribution (b > a).
                X (float): per-unit cost for over-estimation (g > b).
                Y (float): per-unit cost for under-estimation (b > g).
                n_sims (int): number of Monte Carlo draws to estimate expected cost.
                seed (int | None): random seed for reproducibility.

            Returns:
                dict: {
                    "g_opt": float,          # analytic optimal forecast
                    "exp_cost_opt": float,   # simulated expected cost at g_opt
                    "exp_cost_mid": float,   # simulated expected cost at midpoint (a+b)/2
                    "exp_cost_random": float,# simulated expected cost for 1 random g (for reference)
                    "n_sims": int
                }

            Raises:
                ValueError: if b <= a or X < 0 or Y < 0.
        """
        if b <= a:
            raise ValueError("b must be greater than a.")
        if X < 0 or Y < 0:
            raise ValueError("X and Y must be non-negative.")

        rng = np.random.default_rng(seed)

        # analytic optimal forecast (quantile)
        q = Y / (X + Y) if (X + Y) > 0 else 0.5  # if both zero, any g is fine; choose median
        g_opt = a + q * (b - a)

        # helper to estimate expected cost of forecast g
        def simulate_expected_cost(g: float) -> float:
            draws = rng.uniform(a, b, size=n_sims)
            # vectorized loss
            over = np.maximum(g - draws, 0.0)   # g > b
            under = np.maximum(draws - g, 0.0) # b > g
            losses = X * over + Y * under
            return float(np.mean(losses))

        exp_cost_opt = simulate_expected_cost(g_opt)
        exp_cost_mid = simulate_expected_cost((a + b) / 2)

        # random g for reference
        g_random = rng.uniform(a, b)
        exp_cost_random = simulate_expected_cost(g_random)

        res = {
            "g_opt": g_opt,
            "exp_cost_opt": exp_cost_opt,
            "exp_cost_mid": exp_cost_mid,
            "g_random": g_random,
            "exp_cost_random": exp_cost_random,
            "n_sims": n_sims,
        }

        return res

    # Problem 4.
    def dice_order(self, n_dice: int, n_sims: int) -> float:
        """
            What is the proba when tossing n_dice and obtain n_points in strictly increasing order
            Args:
                n_dice : number of dice
                n_sims : number of simulations
            Example:
                n_dice = 3      -->     prob = P[difference number in all 3 tosses] * P[increasing order | different nums]

                                             =          1 * (5 / 6) * (4 / 6)       *       (1 / 6)        
                                             
                                             =                  5 / 54
        """
        cnt = 0
        for _ in range(n_sims):
            rolls = [random.randint(1, 6) for _ in range(n_dice)]
            if all(rolls[i] < rolls[i+1] for i in range(n_dice - 1)):
                cnt += 1
        return cnt / n_sims

    # Problem 5.
    def coin_winning_prob(self, winning_state : str, n_sims: int) -> float:
        """
            Estimate the expected number of fair-coin tosses needed for a given pattern (winning_state) to appear for the first time.

            The state is a string of 'H' and 'T', e.g.:
                                            "H"        "HT"        "HHT"        "TTH"

            Example:
                >>> sol = ProbaStatSims()
                >>> sol.coin_winning_prob("HT", 5000)
                Output:
                        4.01   (true theoretical value = 4)

            Method:
                For each simulation:
                    - Flip a fair coin until the sequence of flips ends with winning_state
                    - Count number of flips
                Return the average over n_sims simulations
        """
        expected_time_to_win = 0
        for _ in range(n_sims): # numbers of simulations
            init_state = ''
            cnt = 0
            while winning_state not in init_state:
                p_temp = random.random()
                if p_temp > 0.5:
                    init_state += 'H'
                else:
                    init_state += 'T'
                cnt += 1
            expected_time_to_win += cnt

        return expected_time_to_win / n_sims

# ========================================== MARKOV CHAIN & MCMC ===============================================
class MarkovChain:
    def get_transition_matrix(self, mat: list[list]) -> float:
        pass

# ===================================== STATISTICAL TESTING HYPOTHESIS =========================================
# Hypothesis class 
class prop_testing:
    """
        Input parameters:
            alternative = {"equal (two_side)", "lower_tail (less)", "upper_tail (greater)"}
            alpha (float in [0, 1]) = significance level / then (1 - alpha) be the confidence_level
        =================================================================================
        Attributes:
            prop_1_test(n, y, p0)
            prop_2_test(n1, n2, p1, p2)
        =================================================================================
        Example
            >> my_prop_test = prop_testing(alter='two_side', alpha=0.05)
            >> my_prop_test.prop_1_test(n=800, y=600, p0=0.77)
            -----------------------
                0.17888190308175522
                {'p_value': 0.17888190308175522,
                 'statistical_testing': -1.3442056254199006,
                 'sample_estimates': 0.75,
                 'conf_interval': [0.7199943020227793, 0.7800056979772207],
                 'final_claim': 'Not engough evidence to reject H0',
                 'alternative': 'p != p0 (not.equal)'}
            -----------------------
            # Testing tỷ lệ 2 mẫu
            >> my_prop_test.prop_2_test(n1=600,n2=800,y1=350,y2=390)
            -----------------------
                {'p_value': 0.00037828752742052885,
                 'statistical_testing': 3.5547855260901673,
                 'sample_estimates (prop_samp1, prop_samp2)': (0.5833333333333334, 0.4875),
                 'conf_interval': [0.043337122902925504, 0.14832954376374125],
                 'final_claim': 'Reject H0',
                 'alternative': 'p != p0 (not.equal)'}         
    """
    def __init__(self, alpha, alter = "equal"):
        valid_alter = ["less", "equal", "greater", "two_side", "lower_tail", "upper_tail"]
        self.alpha = alpha
        self.alter = alter
        if alter not in valid_alter:
            raise ValueError("Alternative (đối thuyết) phải là một trong các dạng sau đây,\n", valid_alter)
        if (alpha < 0) or (alpha > 1):
            raise ValueError("Mức ý nghĩa (significance level) alpha phải nằm trong (0, 1)")
    
    def prop_1_test(self, n, y, p0):
        """
            Testing tỷ lệ cho cùng một mẫu
            Input params:
                p0: theorictic_proportion
                n: sample size
                y: total the elements in population that satisfies a property
            Lý thuyết:
                ************************************************************************
                |   Case   |      Test statistics (Z0)        |        p_value         |
                |----------|----------------------------------|------------------------|
                | two_side | (p.hat - p0) / sqrt(p0*(1-p0)/n) | 2 min(P(Z<Z0), P(Z>Z0))|
                | less     | (p.hat - p0) / sqrt(p0*(1-p0)/n) | P(Z < Z0)              |
                | greater  | (p.hat - p0) / sqrt(p0*(1-p0)/n) | P(Z > Z0)              |
                ************************************************************************     
        """
        p_hat = y / n # proportion in empirical sample
        Z0 = (p_hat - p0)/np.sqrt(( p0 * (1 - p0))/n) # statistical testing'
        
        # for two_sided alternative
        if self.alter in ["equal", "two_side"]:
            p_value = 2*min(1 - norm.cdf(Z0), norm.cdf(Z0))
            dung_sai = abs(norm.ppf(self.alpha / 2))*np.sqrt(( p_hat * (1 - p_hat))/n)
            conf_int = [p_hat - dung_sai, p_hat + dung_sai]
            alter = "p != p0 (not.equal)"
            
        # if alternative = "p < p0"
        elif self.alter in ["less", "lower_tail"]:
            p_value = norm.cdf(Z0)
            dung_sai = abs(norm.ppf(self.alpha))*np.sqrt(( p_hat * (1 - p_hat))/n)
            conf_int = [0, p_hat + dung_sai]
            alter = "p < p0 (less)"
            
        elif self.alter in ["greater", "upper_tail"]:
            p_value = 1 - norm.cdf(Z0)
            dung_sai = abs(norm.ppf(self.alpha))*np.sqrt(( p_hat * (1 - p_hat))/n)
            conf_int = [p_hat - dung_sai, 1]
            alter = "p > p0 (greater)"
        print(p_value)
        if p_value < self.alpha:
            claim = "Reject H0"
        else:
            claim = "Not engough evidence to reject H0"
            
        return {'p_value': p_value, 
                "statistical_testing": Z0,
                'sample_estimates': p_hat, 
                "conf_interval": conf_int,
                "final_claim": claim,
                "alternative": alter
               }
    
    def prop_2_test(self, n1, n2, y1, y2):
        """
            Testing tỷ lệ cho 2 mẫu
            Input params:
                n1, n2: sample_size of 2 samples
                y1, y2: total the elements in population that satisfies a property
            Lý thuyết:
                *********************************************************
                |   Case   |  Test statistics  |        p_value         |
                |----------|-------------------|------------------------|
                | two_side |        Z0         | 2 min(P(Z<Z0), P(Z>Z0))|
                | less     |        Z0         | P(Z < Z0)              |
                | greater  |        Z0         | P(Z > Z0)              |
                *********************************************************
            trong đó:
                Z0 = (p1_hat - p2_hat) / np.sqrt(p_hat*(1 - p_hat)*( 1/n1 + 1/n2))
            và
                p1 = y1 / n1
                p2 = y2 / n2
                p_hat = (y1 + y2) / (n1 + n2)            
        """
        p1_hat = y1 / n1
        p2_hat = y2 / n2
        p_hat = (y1 + y2) / (n1 + n2)
        Z0 = (p1_hat - p2_hat) / np.sqrt(p_hat*(1 - p_hat)*( 1/n1 + 1/n2))
        diff_prop = p1_hat - p2_hat
        
        # for two_sided alternative
        if self.alter in ["equal", "two_side"]:
            p_value =  2*min(1 - norm.cdf(Z0), norm.cdf(Z0))
            dung_sai = abs(norm.ppf(self.alpha / 2))*np.sqrt((p1_hat*(1-p1_hat)/ n1) + (p2_hat*(1-p2_hat)/ n2) )
            conf_int = [diff_prop - dung_sai, diff_prop + dung_sai]
            alter = "p != p0 (not.equal)"
            
        # if alternative = "p < p0"
        elif self.alter in ["less", "lower_tail"]:
            p_value = norm.cdf(Z0)
            dung_sai = abs(norm.ppf(self.alpha))*np.sqrt((p1_hat*(1-p1_hat)/ n1) + (p2_hat*(1-p2_hat)/ n2) )
            conf_int = [0, diff_prop + dung_sai]
            alter = "p < p0 (less)"
            
        elif self.alter in ["greater", "upper_tail"]:
            p_value = 1 - norm.cdf(Z0)
            dung_sai = abs(norm.ppf(self.alpha))*np.sqrt((p1_hat*(1-p1_hat)/ n1) + (p2_hat*(1-p2_hat)/ n2) )
            conf_int = [diff_prop - dung_sai, 1]
            alter = "p > p0 (greater)"
        
        if p_value < self.alpha:
            claim = "Reject H0"
        else:
            claim = "Not engough evidence to reject H0"
            
        return {'p_value': p_value, 
                "statistical_testing": Z0,
                'sample_estimates (prop_samp1, prop_samp2)': (p1_hat, p2_hat), 
                "conf_interval": conf_int,
                "final_claim": claim,
                "alternative": alter
               }
    
## testing on sample-mean
class mean_test:
    """
        Kiểm định trung bình của một / 2 mẫu với các giả định
            - 1 mẫu khi biết phương sai tổng thể (known variance)
            - 1 mẫu khi không biết phương sai tổng thể (Unknown variance)
            - 2 mẫu khi biết phương sai
        =====================================================================
        Attributes:
            avg_1sample(x, muy0, alter, sigma)
            unpaired_data_equal_var(x1, x2, muy1, muy2, alter, sigma)
            unpaired_data_non_equal_var(x1, x2, muy1, muy2, alter, sigma)
    """
    def __init__(self, alpha, alter = "equal", sigma="unknown"):
        valid_alter = ["less", "equal", "greater", "two_side", "lower_tail", "upper_tail"]
        self.alpha = alpha
        self.alter = alter
        self.sigma = sigma        
        if alter not in valid_alter:
            raise ValueError("Alternative (đối thuyết) phải là một trong các dạng sau đây,\n", valid_alter)
        if (alpha < 0) or (alpha > 1):
            raise ValueError("Mức ý nghĩa (significance level) alpha phải nằm trong (0, 1)")
        if (sigma != 'unknown') and (type(sigma) not in [int, float]) and (sigma != None):
            raise ValueError("giá trị hợp lệ của sigma là `unknown` hay một số thực cụ thể, e.g. 5.1, 1.0 ")
    
    def get_params(self):
        print(f"Alternative (đối thuyết): {self.alter}")
        print(f"significance value (alpha): {self.alpha}")
        print(f"sigma (giả thuyết phương sai): {self.sigma}")

    def avg_1sample(self, x, muy0):
        """
            Kiểm định giả thuyết trung bình của 1 mẫu
            ============================================
            kịch bản 1. alternative = 2 side
                *************************************************************************************************************
                |         Case             |           Test Statistic         |                    p.value                  |
                *************************************************************************************************************
                | X is normal, σ known     |(X.bar - muy) / (sigma / sqrt(n)) |2*min(P[X>Z0], 1-P[X>Z0]) where X is normal  |       
                | n_large, X is not normal |(X.bar - muy) / (std.X / sqrt(n)) |2*min(P[X>Z0], 1-P[X>Z0]) where X apprx norm |
                | X is normal, σ un-known  |(X.bar - muy) / (std.X / sqrt(n)) |2*min(P[X>Z0], 1-P[X>Z0]) where X is St(n-1) | 
                ************************************************************************************************************|
            trong đó
                St(n-1) là phân phối Student với n-1 bậc tự do
             ============================================
             kịch bản 2. alternative = greater
                 Được thực hiện tương tự như kịch bản 1, ta chỉ thay đổi p.value thành P[X > Z0], tức là                 
                *************************************************************************************************
                |         Case             |           Test Statistic         |               p.value           |
                *************************************************************************************************
                | X is normal, σ known     |(X.bar - muy) / (sigma / sqrt(n)) |P[X > Z0]     where X is normal  |      
                | n_large, X is not normal |(X.bar - muy) / (std.X / sqrt(n)) |P[X > Z0]     where X apprx norm |
                | X is normal, σ un-known  |(X.bar - muy) / (std.X / sqrt(n)) |P[X > Z0]     where X is St(n-1) | 
                ************************************************************************************************|                 
             ============================================
             kịch bản 3. alternative = less
                 Lúc này ta cũng chỉ thay đổi p.value thành P[X < Z0]
                *************************************************************************************************
                |         Case             |           Test Statistic         |               p.value           |
                *************************************************************************************************
                | X is normal, σ known     |(X.bar - muy) / (sigma / sqrt(n)) |P[X < Z0]     where X is normal  |      
                | n_large, X is not normal |(X.bar - muy) / (std.X / sqrt(n)) |P[X < Z0]     where X apprx norm |
                | X is normal, σ un-known  |(X.bar - muy) / (std.X / sqrt(n)) |P[X < Z0]     where X is St(n-1) | 
                ************************************************************************************************|       
            ==================================================================================================================
            Example
            >> obj = mean_test(alpha=0.05, alter='less', sigma=1)
            >> obj.avg_1sample([1,2,4,5], 3)
            ...........................
                Not enough evidence to reject H0
                {'p-value': 0.5, 'T_stats': 0.0}
            ==================================================================================================================                           
        """
        n = len(x)
        # Biện luận Test-statistics theo sigma
        if self.sigma != None:
            Z0 = (np.mean(x) - muy0) / (self.sigma / n**0.5)
            
            # Biện luận p_value theo các đối thuyết
            if self.alter in ["equal", "two_side"]:
                p_value = 2*min(1 - norm.cdf(Z0), norm.cdf(Z0))
            elif self.alter in ["less", "lower_tail"]:
                p_value = norm.cdf(Z0)
            elif self.alter in ["greater", "upper_tail"]:
                p_value = 1 - norm.cdf(Z0)
            
        else:
            std_x = np.std(x)
            Z0 = (np.mean(x) - muy0) / (std_x / n**0.5)
            
            # trước khi biện luận theo đối thuyết cần chú ý kỹ giả thuyết sample-size 
            # vì nó tương ứng với Student hoặc normal distribution
            if n > 30:
                if self.alter in ["equal", "two_side"]:
                    p_value = 2*min(1 - norm.cdf(Z0), norm.cdf(Z0))
                elif self.alter in ["less", "lower_tail"]:
                    p_value = norm.cdf(Z0)
                elif self.alter in ["greater", "upper_tail"]:
                    p_value = 1 - norm.cdf(Z0)
            # Lúc này nó tương ứng với pp student n-1 bậc tự do
            # note: df meant degree of freedom
            else:
                if self.alter in ["equal", "two_side"]:
                    p_value = 2*min(1 - t.cdf(Z0), t.cdf(Z0, df=n-1))
                elif self.alter in ["less", "lower_tail"]:
                    p_value = t.cdf(Z0, df=n-1)
                elif self.alter in ["greater", "upper_tail"]:
                    p_value = 1 - t.cdf(Z0, df=n-1)
        if p_value < self.alpha:
            print("Bác bỏ H0 nếu p_value < alpha")
        else:
            print("Not enough evidence to reject H0")

        return {'p-value':p_value, 'T_stats': Z0}
    
    def unpaired_data_equal_var(self, x1, x2, muy1, muy2):
        """
            ==================================================================================================================
            unpaired data and equal_variance
            Reference: https://www.itl.nist.gov/div898/handbook/eda/section3/eda353.htm
            ==================================================================================================================
            Example
            >> obj = mean_test(alpha=0.05, alter='less', sigma=1)
            >> obj.unpaired_data_equal_var([1,2,4,5], [2,3,3], 3, 4)
            ...................
                Not enough evidence to reject H0
                {'p-value': 0.2237139366373361, 'T_stats': -0.8240395855065445}
            ==================================================================================================================
        """
        # sample-sizes
        n1 = len(x1)
        n2 = len(x2)

        # difference of mean in 2 samples
        muy_diff = muy1 - muy2

        # common variance
        sd1 = np.std(x1)
        sd2 = np.std(x2)
        cmn_var = ( (n1 - 1)*sd1**2 + (n2 - 1)*sd2**2 ) / (n1 + n2 - 2)

        # Stastistical-testing
        T_stats = muy_diff / (cmn_var * (1/n1 + 1/n2)**0.5 )

        # degree of freedoms
        dfs = n1+n2-2
        # p.value
        # bien luan
        if self.alter in ["equal", "two_side"]:
            p_value = 2*min(1 - t.cdf(T_stats), t.cdf(T_stats, df=dfs))
        elif self.alter in ["less", "lower_tail"]:
            p_value = t.cdf(T_stats, df=dfs)
        elif self.alter in ["greater", "upper_tail"]:
            p_value = 1 - t.cdf(T_stats, df=dfs)

        if p_value < self.alpha:
            print("Bác bỏ H0 nếu p_value < alpha")
        else:
            print("Not enough evidence to reject H0")

        return {'p-value':p_value, 'T_stats': T_stats}

    def unpaired_data_non_equal_var(self, x1, x2, muy1, muy2):
        """
            unpaired data and non-equal_variance
            Reference: https://www.itl.nist.gov/div898/handbook/eda/section3/eda353.htm        
            =========================================================================
            Example
            >> obj = mean_test(alpha=0.05, alter='two_side', sigma=1)
            >> obj.unpaired_data_non_equal_var([1,2,4,5], [2,3,3], 3, 4)    
            ...........................................
                Not enough evidence to reject H0
                {'p-value': nan, 'T_stats': 1.1960198895331717}
        """
        # sample-sizes
        n1 = len(x1)
        n2 = len(x2)

        # difference of mean in 2 samples
        muy_diff = muy1 - muy2

        # common variance
        sd1 = np.std(x1)
        sd2 = np.std(x2)
        cmn_var = (sd1**2 / n1 + sd2**2 / n2)

        # Stastistical-testing        
        T_stats = muy_diff / (cmn_var**0.5)

        # degree of freedoms
        tu_so = (sd1**2 / n1 + sd2**2 / n2)**2
        mau_so = (n1-1)*(sd1**2 / n1)**2 + (n2-1)*(sd2**2 / n2)**2
        dfs = int(tu_so / mau_so)

        # p.value
        # Bien luan
        if self.alter in ["equal", "two_side"]:
            p_value = 2*min(1 - t.cdf(T_stats, df=dfs), t.cdf(T_stats, df=dfs))
        elif self.alter in ["less", "lower_tail"]:
            p_value = t.cdf(T_stats, df=dfs)
        elif self.alter in ["greater", "upper_tail"]:
            p_value = 1 - t.cdf(T_stats, df=dfs)

        if p_value < self.alpha:
            print("Bác bỏ H0 nếu p_value < alpha")
        else:
            print("Not enough evidence to reject H0")

        return {'p-value':p_value, 'T_stats': T_stats}
    
#======================= DEFINE KERNEL FUNCTION =========================
def rect_kernel(t):
    """
        rectangle shape
    """
    return 0.5 * (abs(t) <= 1)

def biw_kernel(t):
    """
        bi-weight kernel
    """
    return (15/16)*(1-t**2)**2*(abs(t) <= 1)

def trig_kernel(t):
    """
        Triangular kernel
    """
    return (1 - abs(t))*(abs(t) <= 1)

def epa_kernel(t):
    """
        Epanechnikov kernel
    """
    return 0.75*(1 - t**2)*(abs(t) <= 1)

def gau_kernel(t):
    """
        Gaussian kernel
    """
    return (1/np.sqrt(2*np.pi))*np.exp(-t**2/2)

def silv_kernel(t):
    """
        Silverman kernel    
    """
    return 0.5*np.exp(-abs(t / np.sqrt(2)))*np.sin(abs(t / np.sqrt(2)) + np.pi/4)

def sigm_kernel(t):
    """ 
        Sigmoid kernel
    """
    pi = np.pi
    return 2/(pi*(np.exp(t) + np.exp(-t)))

def logis_kernel(t):
    """
        Logistic kernel
    """
    return 1/(2 + np.exp(t) + np.exp(-t))

def tricube_kernel(t):
    """
        Tricube kernel
    """
    return (70/81)*((1 - abs(t**3))**3)*(abs(t) <= 1)

## Define the class
class kernel_density_est:
    """ 
        ***********************************************************************
        *    This class used for:
        *        - 1) Find the optimal_bins
        *        - 2) Display many k.d.e with different type of kernel_function
        *        - 3) Given the ecdf of the data.
        *    
        *     of the 1-D data input.
        ************************************************************************
        * Parameters :
        *-------------------------------------------------------------------------
        *     data : must be 1-D dataset
        *     kernel_type (str): type of kernel, can be {"gauss", "bi-weight", "rectangle".
        *                                               "triangle", "Epanechnikov", "silverman",
        *                                               "sigmoid", "logistic", "tri-cube"}
        *     normed : normed your kde and histogram or not?
        *------------------------------------------------------------------------------------------------
        * Attributes:
        * -----------------
        *    get_params: returns the parameters in this class
        *    get_bins: returns the bins-width of histogram_kde
        *    display : show the kde
        *    show_ecdf: display the empirical cummulative distribution function
        *************************************************************************
    """
    def __init__(self, data, kernel_type = "gauss", normed = True):
        
        self.data = data
        self.kernel_type = kernel_type
        self.normed = normed
        
    def get_params(self):
        """ Returns the initial parameters """
        return {'kernel': self.kernel_type, 'normed': self.normed}
    
    def get_bins(self):
        return 1 / np.sqrt(len(self.data))
    
    def display(self):
        n = len(self.data)
        h = self.get_bins()
        is_normed = self.normed
        
        kde_constant = (1 / (2*n*h))**(is_normed)
        kernel_type = self.kernel_type
        
        u = np.linspace(min(self.data), max(self.data), 1000)
        kde = np.zeros(len(u))
        
        for x_k in self.data:
            if kernel_type == "gauss":
                kde = kde + gau_kernel((x_k -  u)/h) * kde_constant
            elif kernel_type == "bi-weight":
                kde = kde + biw_kernel((x_k -  u)/h) * kde_constant
            elif kernel_type == "rectangle":
                kde = kde + rect_kernel((x_k -  u)/h) * kde_constant
            elif kernel_type == "triangle":
                kde = kde + trig_kernel((x_k -  u)/h) * kde_constant
            elif kernel_type == "Epanechnikov":
                kde = kde + epa_kernel((x_k -  u)/h) * kde_constant
            elif kernel_type == "silverman":
                kde = kde + silv_kernel((x_k -  u)/h) * kde_constant
            elif kernel_type == "tricube":
                kde = kde + tricube_kernel((x_k -  u)/h) * kde_constant
            elif kernel_type == "sigmoid":
                kde = kde + sigm_kernel((x_k -  u)/h) * kde_constant
            elif kernel_type == "logistic":
                kde = kde + logis_kernel((x_k -  u)/h) * kde_constant
            else:
                raise TypeError("No kernel named: "+str(kernel_type))
        
        
        plt.plot(u, kde, '-', label = 'kde')
        plt.title('kernel = '+str(kernel_type))
        plt.xlabel("normed = "+str(is_normed))
                
    def show_ecdf(self):
        """
            Display the ecdf (empirical cumulative distribution function)
        """
        x = self.data
        x = np.sort(x)
        n = len(x)
        y = np.arange(1, n + 1, 1) / n
        plt.plot(x, y, label = 'ecdf')
        plt.legend()
    plt.show()

#============================================
from sklearn.base import clone 
from itertools import combinations
from sklearn.metrics import accuracy_score
from sklearn import neighbors, datasets
from sklearn.model_selection import train_test_split

class Sequential_Backwar_Selection:
    """

    """
    def __init__(self, estimator, k_features, scoring=accuracy_score,                 
                 test_size=0.25, random_state=1):        
 
        self.scoring = scoring        
        self.estimator = clone(estimator)        
        self.k_features = k_features        
        self.test_size = test_size
        self.random_state = random_state
        
    def fit(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = self.test_size, 
                                                             random_state = self.random_state)
        dim = X_train.shape[1]        
        self.indices_ = tuple(range(dim))        
        self.subsets_ = [self.indices_]        
        score = self._calc_score(X_train, y_train, X_test, y_test, self.indices_)        
        self.scores_ = [score]
        while dim > self.k_features:            
            scores = []            
            subsets = []
            for p in combinations(self.indices_, r=dim - 1):                
                score = self._calc_score(X_train, y_train, X_test, y_test, p)
                scores.append(score)
                subsets.append(p)
            best = np.argmax(scores)
            self.indices_ = subsets[best]
            self.subsets_.append(self.indices_)            
            dim -= 1 
            self.scores_.append(scores[best])
        self.k_score_ = self.scores_[-1]
        return self
    def transform(self, X):        
        return X[:, self.indices_]
    def _calc_score(self, X_train, y_train, X_test, y_test, indices):        
        self.estimator.fit(X_train[:, indices], y_train)        
        y_pred = self.estimator.predict(X_test[:, indices])        
        score = self.scoring(y_test, y_pred)        
        return score    

#============================================
class Polynomial_Univariate_Regression:
    """
        This class is used to solve the polynomial assumption of univariate-regression

                Y = a0 + a1 X + a2 X^2 + ... + a_d X^d
        ================================================================================
        Example.
            ############################################################################
            >> X = [1, 2, -1]
            >> y = [1, -1, -1]
            >> clf = Polynomial_Univariate_Regression(X, deg = 3)
            >> clf.coef()
            -------------------
                w_0:  -1.0000000000000004
                w_1:  1.0000000000000007
                w_2:  1.000000000000001
            #*********************************************
            #
            # this meant y = w2 * x^2 + w1 * x + w0
            # or         y =    x^2   +    x  -  1
            #
            #*********************************************
            >> clf.predict(np.array([1,2,4]))
            ---------------------
                [ 1.  5. 19.]
            #*********************************************
            # Note that
            #              1 = w2*1^2 + w1*1 + w0
            #              5 = w2*2^2 + w1*2 + w0
            #             19 = w2*4^2 + w1*4 + w0
            #*********************************************
            >> clf.MSE_score([1,2,4], [2,3,3])
            ----------------------
                87.00000000000023
            ############################################################################
    """
    def __init__(self, X, y, deg):
        self.X = np.array(X)
        self.y = np.array(y)
        self.deg = deg
        
    def coef(self, if_printed=True):
        coefs = np.polyfit(self.X, self.y, self.deg)
        if if_printed:
            for d in range(self.deg + 1):
                print(f"w_{d}: \t {coefs[d]}")
        return coefs
    
    def predict(self, X_new):
        coefs = self.coef(if_printed=False)
        X_new = np.array(X_new)
        X_bar = np.array([X_new**k for k in range(self.deg + 1)])
        y_pred = np.sum(np.array(coefs.reshape(-1, 1)*X_bar), axis = 0)
        
        return y_pred

    def MSE_score(self, X_new, y_new):
        coefs = self.coef(if_printed=False)
        y_pred = self.predict(X_new)
        return np.mean([(y_new[k] - y_pred[k])**2 for k in range((np.array(X_new).shape[0]))])
    
    def R2_score(self, X_new, y_new):
        coefs = self.coef(if_printed=False)
        y_pred = self.predict(X_new)
        
        # sum of square_error
        SSE = np.sum([(self.y[k] - y_pred[k])**2 for k in range((np.array(self.X).shape[0]))])
        
        # total_sum of square = SSE + Sum_squared_regression
        SST = SSE + np.sum([(y_pred[k] - np.mean(y_new))**2 for k in range((np.array(X_new).shape[0]))])
        
        return 1 - (SSE / SST)
    
    def plot(self):
        coefs = self.coef(if_printed=False)
        y_pred = self.predict()
        plt.plot(self.X, self.y, '*', label = 'actual')
        plt.plot(self.X, y_pred, '--', label = 'pred')
        plt.legend()
        plt.plot()

#========================== cartoon transformation
#
#       See more: https://github.com/NhanDoV/All-of-my-projects./tree/main/Jan2022-Jan2024/4.%20Cartoon-transform-sketch
#        
#=======================================================================#
import cv2
from sklearn.cluster import KMeans

def KMean_transform(img, nb_clusters=6):
    """
        Image segmentation is the classification of an image into different groups. 
        Many kinds of research have been done in the area of image segmentation 
        using clustering, here is KMeans.
        This will reduce the number of color-range from the original images and make
        your output look like a cartoon image.
    """
    ## Flatten the image_array
    X = img.reshape((img.shape[0]*img.shape[1], img.shape[2]))
    kmeans = KMeans(n_clusters = nb_clusters)
    kmeans.fit(X)

    ## create labels and centroids
    label = kmeans.predict(X)
    temp_img = np.zeros_like(X)

    # replace each pixel by its center
    for k in range(nb_clusters):
        centroids_val =  np.uint8(kmeans.cluster_centers_[k])
        temp_img[label == k] = centroids_val 

    out_img = temp_img.reshape(img.shape[0], img.shape[1], img.shape[2])

    return out_img

def smoothing_image(img, size=(960, 640)):
    """
        Smoothing image by using median-bluring into the gray-scale image
    """
    ReSized1 = cv2.resize(img, size)

    # converting an image to grayscale
    grayScaleImage= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ReSized2 = cv2.resize(grayScaleImage, size)

    # applying median blur to smoothen an image
    smoothGrayScale = cv2.medianBlur(grayScaleImage, 5)
    ReSized3 = cv2.resize(smoothGrayScale, size)

    getEdge = cv2.adaptiveThreshold(smoothGrayScale, 255, 
        cv2.ADAPTIVE_THRESH_MEAN_C, 
        cv2.THRESH_BINARY, 9, 9)

    ReSized4 = cv2.resize(getEdge, size)

    return ReSized1, getEdge, ReSized4

def to_cartoon(ImagePath, nb_clusters, size=(960, 640)):
    """
        Wrapping up all the techniques (gray-scale + Smoothing + KMeans-clustering)
    """
    # read the image
    originalmage = cv2.imread(ImagePath)
    originalmage = cv2.cvtColor(originalmage, cv2.COLOR_BGR2RGB)
    #print(image)  # image is stored in form of numbers

    # retrieving the edges for cartoon effect by using thresholding technique
    ReSized1, getEdge, ReSized4 = smoothing_image(originalmage, size)

    # applying bilateral filter to remove noise & keep edge sharp as required
    colorImage = cv2.bilateralFilter(originalmage, 5, 300, 300)
    ReSized5 = cv2.resize(colorImage, size)
    
    # masking edged image with our "BEAUTIFY" image
    cartoonImage = cv2.bitwise_and(colorImage, colorImage, mask=getEdge)
    ReSized6 = KMean_transform(cv2.resize(cartoonImage, size), nb_clusters)

    return ReSized6

# ==================================================
from PIL import Image,ImageDraw, ImageColor
import random as rnd
import re
# ==================================================
class Maze:
    """
        newMaze = Maze(10,10)
        newMaze.makeMazeGrowTree(weightHigh = 99, weightLow = 97)
        mazeimg = newMaze.makePP()
        #can or can not work, see Pillow documentation. For debuging only
        mazeimg.show() 
    """
    class __MazeTile:
        """ 
        
        """        
        def __init__(self, X, Y, isWall = True):
            """
            
            """
            self.workedOn = False   # Needed for certain generation algorithm to define if a tile as already be touched
            self.wall = isWall      # Is the tile a wall (True) or a floor (False). Mostly for future proving
            self.coordinateX = X    # Defining the X coordinate
            self.coordinateY = Y    # Defining the Y coordinate 
            self.connectTo = []     # A list of strings that describe the tiles this tile is connected to (North, South, West, East)
            
        def __str__(self):
            return "X: " + str(self.coordinateX)+" "+ "Y: " + str(self.coordinateY) + " " + str(self.connectTo)
                    
        def __repr__(self):
            return "__MazeTile, wall = {}, worked on = {} ,x = {}, y = {} ---".format(self.wall , self.workedOn, self.coordinateX, self.coordinateY)
            
    class __MazeError(Exception):
        """ 
        
        """
        def __init__(self, string, errorcode):
            self.string = string
            self.errorcode = errorcode
        def __str__(self):
            return (str(self.string) + " |Errorcode: {}".format(self.errorcode))
    
    def __init__(self, dimensionX, dimensionY,mazeName = "A_Maze"):
        """
        
        """        
        if not isinstance(dimensionX, int) or not isinstance(dimensionY, int):      #Checking input errors
            raise self.__MazeError("Maze dimensions have to be an integer > 0",1)
                    
        if dimensionX < 1 or dimensionY < 1:
            raise self.__MazeError("Maze dimensions have to be an integer > 0",1)
                    
        if not isinstance(mazeName, str):
            raise self.__MazeError("The name of the Maze has to be a string",1)
            
        self.sizeX = dimensionX     #The size of the Maze in the X direction (from left to right)
        self.sizeY = dimensionY     #The size of the Maze in the Y direction (from up to down)
        
        self.name = mazeName    #The name of the Maze. Can be any string
        self.__mazeIsDone = False     #When this flag is False, no picture can be made. When this flag is True, the maze can not be changed
        
        self.mazeList = []          #A nested List of maze Tiles. The internal representation of the maze
        
        self.wallList = []          #A list of all lists that are walls (needed for certain algorithm)
        self.tileList = []          #A single list of all tiles (needed of certain algorithm)
        
        self.mazeString = ""        #A string describing the Maze in a pseudo graphical manner, gets generated everytime __str__() gets called
                
    def __str__(self): 
        """ 
        
        """        
        self.mazeString = ""        
        for row in self.mazeList:            
            for tile in row:                
                self.mazeString += "{:^20}".format(str(tile.connectTo))        
            self.mazeString += "\n"                
        return self.mazeString                    
        
    def __repr__(self): 
        """ 

        """                        
        return "This is a Maze with width of {} and height of {}".format(self.sizeX , self.sizeY)
    
    def __getNextTiles(self,X,Y): 
        """ 
            
        """        
        if X < 0 or Y < 0:  #Checks input error (this should never happen)            
            raise self.__MazeError("Inputs have to be an integer > 0",1)        
        templist = []        
        try:
            if Y == 0:
                pass
            else:
                templist.append(self.mazeList[Y-1][X])
        
        except(IndexError):
            pass

        try:
            templist.append(self.mazeList[Y+1][X])
        except(IndexError):
            pass
            
        try:
            if X == 0:
                pass
            else:
                templist.append(self.mazeList[Y][X-1])
        except(IndexError):
            pass
            
        try:
            templist.append(self.mazeList[Y][X+1])
        except(IndexError):
            pass
        
        return templist
        
    def __connectTiles(self, tileA, tileB):
        """   
        
        """
        X1 = tileA.coordinateX 
        Y1 = tileA.coordinateY
        
        X2 = tileB.coordinateX 
        Y2 = tileB.coordinateY
        
        if X1 == X2:            
            if Y1 < Y2:               
                tileA.connectTo.append("S")
                tileB.connectTo.append("N")
            
            elif Y1 > Y2:
                tileA.connectTo.append("N")
                tileB.connectTo.append("S")

        else:
            if X1 < X2:                
                tileA.connectTo.append("E")
                tileB.connectTo.append("W")
            
            else:
                tileA.connectTo.append("W")
                tileB.connectTo.append("E")
        
        return True
        
    def __connectTilesWithString(self,tile,direction):
        """
        
        """
        if direction == "N":
            try:
                if tile.coordinateY == 0:   #This prevents list[-1] situations and two holes in the border wall
                    raise IndexError
                    
                self.mazeList[tile.coordinateY -1][tile.coordinateX].connectTo.append("S")
                tile.connectTo.append("N")
                
            except(IndexError):
                raise self.__MazeError("This tile can not connect in this direction",2)
        
        elif direction == "S":
            try:
                self.mazeList[tile.coordinateY + 1][tile.coordinateX].connectTo.append("N")
                tile.connectTo.append("S")
                
            except(IndexError):
                raise self.__MazeError("This tile can not connect in this direction",2)     
               
        elif direction == "W":
            try:
                if tile.coordinateX == 0:
                    raise IndexError
                self.mazeList[tile.coordinateY][tile.coordinateX - 1].connectTo.append("E")
                tile.connectTo.append("W")   
                             
            except(IndexError):
                raise self.__MazeError("This tile can not connect in this direction",2)
                
        elif direction == "E":
            try:
                self.mazeList[tile.coordinateY][tile.coordinateX + 1].connectTo.append("W")
                tile.connectTo.append("E")
                
            except(IndexError):
                raise self.__MazeError("This tile can not connect in this direction",2)
                
        else:
            raise self.__MazeError("This was not a direction string",1)
            
        return True
    
    def __makeEntryandExit(self,random = False):
        """ 
        
        """
        if random:            
            tile = rnd.choice(self.mazeList[0])
            tile.connectTo.append("N")
                    
            tile = rnd.choice(self.mazeList[-1])
            tile.connectTo.append("S")
        else:
            self.mazeList[0][0].connectTo.append("N")
            self.mazeList[-1][-1].connectTo.append("S")
            
        return True
    
    def makeMazeSimple(self):
        """
        
        """        
        if self.__mazeIsDone:     #Can only run if the maze is not already formed
            raise self.__MazeError("Maze is already done",3)
            
        for indexY in range (0,self.sizeY):     #This loops generates the mazeList and populates it with new untouched floor tiles
            templist = []
            
            for indexX in range(0,self.sizeX):
                newTile = self.__MazeTile(indexX, indexY, isWall = False)
                templist.append(newTile)
                
            self.mazeList.append(templist)
        
        frontList = []          #A list of all untouched tiles that border a touched tile
        startingtile = rnd.choice(rnd.choice(self.mazeList))    #A randomly chosen tile that acts as starting tile
        
        startingtile.workedOn = True    #This flag always gets set when a tile has between worked on.
        frontList += self.__getNextTiles(startingtile.coordinateX, startingtile.coordinateY)  #populates the frontier
                                                                                                #list with the first 2-4 tiles 
        
        while len(frontList) > 0 : #When the frontier list is empty the maze is finished because all tiles have been connected
            newFrontTiles = []
            workedOnList = []
            
            rnd.shuffle(frontList)
            nextTile = frontList.pop()
            nextTile.workedOn = True
            
            tempList = self.__getNextTiles(nextTile.coordinateX,nextTile.coordinateY)

            for tile in tempList: #Finds all neighbours who are touched and all that are a untouched
                if tile.workedOn:                    
                    workedOnList.append(tile)                    
                else:                    
                    if not tile in frontList:
                        newFrontTiles.append(tile)                    
            frontList += newFrontTiles
            if len(workedOnList) > 1:   #Chooses the neighbor the tile should connect to
                connectTile = rnd.choice(workedOnList)
            
            else:
                connectTile = workedOnList[0]
            
            self.__connectTiles(nextTile,connectTile)
            
        self.__makeEntryandExit()     #Finally produces a Entry and an Exit
        self.__mazeIsDone = True
        return True

    def makeMazeGrowTree(self,weightHigh = 99,weightLow = 97):
        
        """
        
        """
        if self.__mazeIsDone: #This function only runs of the Maze is not already formed.
            raise self.__MazeError("Maze is already done",3)
            
        for indexY in range (0,self.sizeY):     #This loops generates the mazeList and populates it with new untouched floor tiles
            templist = []
            
            for indexX in range(0,self.sizeX):
                newTile = self.__MazeTile(indexX, indexY, isWall = False)
                templist.append(newTile)
                
            self.mazeList.append(templist)

        startingtile = rnd.choice(rnd.choice(self.mazeList))    #First tile is randomly chosen
        startingtile.workedOn = True
        
        choiceList = [startingtile] #The list of available tiles
        
        while len(choiceList) > 0:  #Runs until choiceList is empty     
            choice_ = rnd.random() * 100    #This random choice determines how the next tile is chosen     
            if choice_ <= weightLow:  
                nextTile = choiceList[-1]
            elif weightLow < choice_ < weightHigh:
                nextTile=rnd.choice(choiceList)
            else:
                nextTile = choiceList[0]
            
            neiList = []    #List of neighbours
            for tile in self.__getNextTiles(nextTile.coordinateX,nextTile.coordinateY):
                if not tile.workedOn:
                    neiList.append(tile)
            if len(neiList) == 0:   #either removing this tile or choosing a neighbour to interact with
                choiceList.remove(nextTile)
            else:
                connectTile = rnd.choice(neiList)
                connectTile.workedOn = True
                choiceList.append(connectTile)
                self.__connectTiles(nextTile,connectTile)

        self.__makeEntryandExit() #finally marking an Entry and an Exit
        self.__mazeIsDone = True
        return True
        
    def makeMazeBraided(self, weightBraid = -1):
        """
        
        """
        if not self.__mazeIsDone:
            raise self.__MazeError("Maze needs to be formed first",4)

        if not isinstance(weightBraid, int) or weightBraid <  -1 or weightBraid > 100:
            raise self.__MazeError("weightBraid has to be >= -1",1)
        
        elif weightBraid == -1:
            for row in self.mazeList:
                for tile in row:
                    if len(tile.connectTo) == 1: #All tiles that are only connected to one other tile are dead ends
    
                        directionList=["N","S","W","E"]
                        directionList.remove(tile.connectTo[0])
                        
                        rnd.shuffle(directionList) #Randomizing connections
                        for direction in directionList:
                            try:
                                self.__connectTilesWithString(tile,direction)
                                break
                                
                            except self.__MazeError as mazeExcept:
                                if mazeExcept.errorcode == 2:
                                    pass
                                    
                                else:
                                    raise
        else:
            for row in self.mazeList:
                for tile in row:
                    if weightBraid >= (rnd.random() * 100): #Weight decides if this tiles gets a addtional connection
                        
                        directionList=["N","S","W","E"]
                        for connection in tile.connectTo:
                            directionList.remove(connection)
                             
                        rnd.shuffle(directionList) #Randomizing connections
                        for direction in directionList:                            
                            try:
                                self.__connectTilesWithString(tile,direction)
                                break                                
                            except self.__MazeError as mazeExcept:
                                if mazeExcept.errorcode == 2:
                                    pass                                    
                                else:
                                    raise
        return True
        
    def makePP(self,mode = "1", colorWall = 0, colorFloor = 1, pixelSizeOfTile = 10, ):
        """
        
        """
        if not self.__mazeIsDone:
            raise self.__MazeError("There is no Maze yet",4)
            
        if mode == "1":                                                         #Checking for input errors
            if colorWall in (1,0) and colorFloor in (1,0):
                pass
            else:
                raise self.__MazeError("In mode \'1\' the color vaules have to be 0 for black or 1 for white",1)                
        elif mode == "RGB":            
            try:
                if isinstance(colorWall,str):
                    colorWall = ImageColor.getrgb(colorWall)                
                elif isinstance(colorWall,tuple) and len(colorWall) == 3:
                    for i in colorWall:
                        if not isinstance(i,int) or (i < 0 or i > 255):
                            raise self.__MazeError("RGB mode excepts only 8-bit integers",1)                
                else:
                    raise self.__MazeError("RGB Mode only excepts color strings or 3x8bit tulpels",1)                    
                    
                if isinstance(colorFloor,str):
                    colorFloor = ImageColor.getrgb(colorFloor)
                
                elif isinstance(colorFloor,tuple) and len(colorFloor) == 3:
                    for i in colorFloor:
                        if not isinstance(i,int) or (i < 0 or i > 255):
                            raise self.__MazeError("RGB mode excepts only 8-bit integers",1)
                
                else:
                    raise self.__MazeError("RGB Mode only excepts color strings or 3x8bit tulpels",1) 
                    
            except ValueError:
                raise self.__MazeError("RGB mode excepts 140 common html color strings. This was not one of them",1)
                
        else: raise self.__MazeError("The mode was not recognized. Only \'1\' or \'RGB\' are allowed",1)  
        
        if not isinstance(pixelSizeOfTile, int) or pixelSizeOfTile <= 0:
            raise self.__MazeError("the size of the tiles has to be an integer > 0",1) #Finished looking for input errors.                
        
        size = ( pixelSizeOfTile  * (self.sizeX * 2 + 1),  pixelSizeOfTile  * (self.sizeY * 2 + 1)) 
            # Determines the size of the picture. It does this by taking the number of tiles,
            # multiplying it with 2 to account for walls or connections and adds one for offset

        image = Image.new(mode,size,colorWall) #Generates a Pillow Image object
        drawImage = ImageDraw.Draw(image)        
        for row in self.mazeList: #Iterates over all tiles                
                for tile in row:
                    #There are floor tiles at postion 1,3,5..., at postion 0,2,4,6... are either wall tiles or connecting tiles.
                    x = ((tile.coordinateX  + 1) * 2 - 1) *  pixelSizeOfTile 
                    y = ((tile.coordinateY  + 1) * 2 - 1) *  pixelSizeOfTile 
                    drawImage.rectangle([x, y, 
                                         x +  pixelSizeOfTile  -1, 
                                         y +  pixelSizeOfTile  -1], 
                                         fill = colorFloor) 
                    if "N" in tile.connectTo:
                        drawImage.rectangle([x, y -  pixelSizeOfTile , 
                                             x +  pixelSizeOfTile  - 1,
                                               y - 1], fill = colorFloor)                        
                    if "S" in tile.connectTo:
                        drawImage.rectangle([x, y +  pixelSizeOfTile , 
                                             x +  pixelSizeOfTile  - 1, 
                                             y +  pixelSizeOfTile  +  pixelSizeOfTile  - 1], 
                                             fill = colorFloor)                        
                    if "W" in tile.connectTo:
                        drawImage.rectangle([x -  pixelSizeOfTile , y, 
                                             x - 1, y +  pixelSizeOfTile  - 1], 
                                             fill = colorFloor)        
                    if "E" in tile.connectTo:
                        drawImage.rectangle([x +  pixelSizeOfTile , y, 
                                             x +  pixelSizeOfTile  +  pixelSizeOfTile  - 1, 
                                             y +  pixelSizeOfTile  - 1], 
                                             fill = colorFloor)
        return image #returns an image object  
                        
    def saveImage(self, pixelSizeOfTile, image, name = None,format = None):
        """
        
        """
        if name == None:
            tempName = re.sub(r'[^a-zA-Z0-9_]', '', self.name)  # Regular expression to make name filename safe
            if len(tempName) > 120:                             # Limiting the length of the filename
                tempName = tempName[0:120]
            size = ( pixelSizeOfTile  * (self.sizeX * 2 + 1),  pixelSizeOfTile  * (self.sizeY * 2 + 1))
            name = tempName +"-"+ str(size[0]) + "_" + str(size[1]) + ".png"
        image.save(name,format)        
        return True