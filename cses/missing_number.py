import sys

def solution():
    line1 = sys.stdin.readline()
    if not line1:
        return
    n = int(line1.strip())

    line2 = sys.stdin.readline()
    if not line2:
        return
    arr = list(map(int, line2.split()))
    arr.sort()
    missing = 0
    for i in reversed(range(n)):
        
        target = i+1
        if arr[i] != target:
            missing = target
            break
    
    print(missing)

solution()