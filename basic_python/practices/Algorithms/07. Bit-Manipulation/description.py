def bitwise_description():
    a = [0, 0, 1, 1]
    b = [0, 1, 0, 1]

    # Header
    print("*" + "-"*82 + "*")
    print(f"| {'a':^7} | {'b':^7} | {'OR (a | b)':^17} | {'AND (a & b)':^20} | {'XOR (a ^ b)':^17} |")
    print("*" + "-"*82 + "*")

    # Rows
    for i in range(len(a)):
        or_result = a[i] | b[i]
        and_result = a[i] & b[i]
        xor_result = a[i] ^ b[i]
        print(f"| {a[i]:^7} | {b[i]:^7} | {or_result:^17} | {and_result:^20} | {xor_result:^17} |")

    print("*" + "-"*82 + "*")