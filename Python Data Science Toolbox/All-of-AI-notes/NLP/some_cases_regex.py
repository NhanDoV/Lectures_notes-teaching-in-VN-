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