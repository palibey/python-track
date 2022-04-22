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
        
