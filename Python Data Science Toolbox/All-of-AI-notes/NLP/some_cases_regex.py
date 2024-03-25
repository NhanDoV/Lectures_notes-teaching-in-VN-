import re

#=======================================================================
def count_word(w, s):
    """
        Count all the word (w) in the given string (s)
        --------------
        Example
        >> count_word("hi", "hi how are you")
            1
        >> count_word("wow", "wow amazing and wow ")
            2
    """
    patt = rf"{w}\s"
    return len(re.findall(patt, s.lower()))
#=======================================================================
def count_programing_language(text):
    """
        Here we count the distinct programming languages
        Example
        >> count_programing_language("Python, Matlab and R are my favorite programming languages")
            Unique programming language(s) mentioned : {'r', 'matlab', 'python'}
            3
        >> count_programing_language("Python is better than R in ML but R is better than Python in statistics")
            Unique programming language(s) mentioned : {'r', 'python'}
            2
    """
    pattern = r'\b(cpp|c|java|python|perl|php|ruby|csharp|matlab|haskell|clojure|bash|scala|erlang|clisp|lua|brainfuck|javascript|go|d|ocaml|r|pascal|sbcl|dart|groovy|objectivec)\b'
    reg = re.compile(pattern)
    reg = reg.findall(text.lower())
    print('Unique programming language(s) mentioned :', set(reg))
    return len(set(list(reg)))
#=======================================================================
def any_check(string):
    """
        Nhập vào một đoạn dữ liệu, đếm số các
          - từ có cả số lẫn chữ
          - từ chỉ gồm toàn chữ cái
          - từ chỉ gồm toàn con số
          - từ có ít nhất 1 chữ viết thường
          - từ gồm toàn bộ các chữ cái là in hoa
          - số khoảng trắng
        ====================================================================
        Example
        >> string = "Hello XI 1234 is 1234"
            n_words is alpha-numeric                :    5     
            n_words is alphabet                     :    3     
            n_words is all-digits                   :    2     
            n_words has at-least lowercase          :    2     
            n_words has all-uppercase               :    1     
            n_space                                 :    4         
    """
    any_upper = len(re.findall(r'\b(?:[a-z]*[A-Z]){2}[a-zA-Z]*\b', string))
    any_lower = len(re.findall(r'[a-z]+', string))
    any_alnum = len(re.findall(r'[A-Za-z0-9]+', string))
    any_albet = len(re.findall(r'[A-Za-z]+', string))
    any_digit = len(re.findall(r'[0-9]+', string))
    any_space = len(re.findall(r'\s', string))

    print(f"{'n_words is alpha-numeric': <40}:{str(any_alnum): ^10}")
    print(f"{'n_words is alphabet': <40}:{str(any_albet): ^10}")
    print(f"{'n_words is all-digits': <40}:{str(any_digit): ^10}")
    print(f"{'n_words has at-least lowercase': <40}:{str(any_lower): ^10}")
    print(f"{'n_words has all-uppercase': <40}:{str(any_upper): ^10}")
    print(f"{'n_space': <40}:{str(any_space): ^10}")

#=======================================================================
def count_digit_vs_nondigit(string):
    """
        Examples:
        >> count_digit_vs_nondigit("12 + 13 = 25")
            n digits            :    3     (e.g. ['12', '13', '25'])
            n non-digits        :    2     (e.g. [' + ', ' = '])    
        >> count_digit_vs_nondigit("Today is 25 Mar 2024")
            n digits            :    2     (e.g. ['25', '2024'])
            n non-digits        :    2     (e.g. ['Today is ', ' Mar '])
    """
    n_digits = len(re.findall(r"\d{1,}", string))
    n_nondigits = len(re.findall(r"\D{1,}", string))
    print(f"{'n digits': <20}:{str(n_digits): ^10}")
    print(f"{'n non-digits': <20}:{str(n_nondigits): ^10}")

#=======================================================================
def count_whitespace_vs_nonwsp(string):
    """
        Example
        >> count_whitespace_vs_nonwsp("Hello World\tAre you ok")
           n white-space       :    4     (e.g. [' ', '\t', ' ', ' '] )
           n non-white-space   :    5     (e.g. ['Hello', 'World', 'Are', 'you', 'ok'])
    """
    n_wspace = len(re.findall(r"\s{1,}", string))
    n_nonwspace = len(re.findall(r"\S{1,}", string))
    print(f"{'n white-space': <20}:{str(n_wspace): ^10}")
    print(f"{'n non-white-space': <20}:{str(n_nonwspace): ^10}")