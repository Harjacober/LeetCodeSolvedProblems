from collections import deque
def isValid(s):
    left,right,ast = deque(),deque(),deque()
    for i in range(len(s)):
        if s[i] == "(": left.append(i)
        elif s[i]==")":
            if left: left.pop()
            else: right.append(i)
        else:
            ast.append(i)

    if left and ast:
        while left and ast and left[-1] < ast[-1]:
            left.pop(); ast.pop()
    if right and ast:
        while right and ast and right[0] > ast[0]:
            right.popleft(); ast.popleft()

    return not(right or left)

string = "*)()()()((*)"
print(isValid(string))
            
