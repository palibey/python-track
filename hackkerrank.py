# else if 

if __name__ == '__main__':
    n = int(raw_input().strip())
    if n % 2 == 1:
        print("Weird")
    elif 2 <= n <= 5 or n > 20:
        print("Not Weird")    
    elif 6 <= n <= 20:
        print("Weird")
        
# arithmetic

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print(a + b)
    print(a - b)
    print(a * b)

# division

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print(a // b)
    print(a / b)
    
# loops

if __name__ == '__main__':
    n = int(raw_input())
    for x in range(n):
        print(x * x)
        
# write a function

def is_leap(year):
    leap = False
    
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
    return leap

year = int(raw_input())
print is_leap(year)
        
# Nested List

if __name__ == '__main__':
    size = int(raw_input())
    names = []
    scores = []
    scoresOrg = []
    for _ in range(size):
        name = raw_input()
        score = float(raw_input())
        scores.append(score)
        scoresOrg.append(score)
        names.append(name)
    scores.sort() 
    secondMin = scores[1]
    while scores[0] == scores[1]:
        scores.pop(0)
    secondMin = scores[1]
    index = []
    count = scores.count(secondMin)
    while count >= 1:
        index.append(scoresOrg.index(secondMin))
        scores.remove(secondMin)
        count = scores.count(secondMin)
    namesToSort = []
    while len(index) > 0:
        namesToSort.append(names.pop(index[0]))
        index.pop(0)
    namesToSort.sort()
    while len(namesToSort) > 0:
        print(namesToSort[0])
        namesToSort.pop(0)    
    
