list1 = [1, 3, 4, 64, 44, 99, 45, 9]
list2 = [1, 3, 4, 64, 44, 99, 45]

def solution(x, y):
    shorter = x if len(x) < len(y) else y 
    longer = x if len(x) > len(y) else y
    for a in longer:
      if a not in shorter:
        return a

print(solution(list1, list2))