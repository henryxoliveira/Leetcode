from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []  # Stack to store indices
        
        for i in range(n):
            # While stack is not empty and current temperature is warmer
            # than the temperature at the index stored in stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index
            
            # Push current index to stack
            stack.append(i)
        
        return answer

