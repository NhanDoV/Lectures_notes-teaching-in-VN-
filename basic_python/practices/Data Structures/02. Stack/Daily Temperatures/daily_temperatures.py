class dailyTemperatures:
    def brute_force(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        result = []

        for i in range(n):
            count = 1               # number of days checked ahead
            j = i + 1               # pointer to scan forward

            while j < n:
                if temperatures[j] > temperatures[i]:
                    break           # found a warmer temperature
                j += 1
                count += 1

            # If j reaches the end, no warmer day exists
            count = 0 if j == n else count
            result.append(count)

        return result 
    
    def using_stack(self, temperatures: list[int]) -> list[int]:
        result = [0] * len(temperatures)
        my_stack = []              # stack of (temperature, index)

        for i, t in enumerate(temperatures):
            # While the current temp is warmer than the last stacked temp
            while my_stack and t > my_stack[-1][0]:
                stackT, stackInd = my_stack.pop()
                result[stackInd] = i - stackInd   # days waited

            # Push current temperature and index for later comparison
            my_stack.append((t, i))

        return result