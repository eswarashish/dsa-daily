import sys

def solution():
    line = sys.stdin.readline()
    if not line:
        return
    
    n = int(line.strip())

    results = []
    
    while n!=1:
        results.append(str(n))
        if n%2 != 0: 
            n = n*3 + 1
            
        else:
            n = int(n/2)
        
    results.append("1")
    print(" ".join(results))

solution()