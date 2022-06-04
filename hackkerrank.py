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
    

    # percentage
    if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    currScore = student_marks[query_name]
    sumStud = 0;
    for x in range(len(currScore)):
        sumStud += currScore[x]
    print("{:.2f}".format(sumStud/len(currScore)))    
    
    
    #LIST
    
    if __name__ == '__main__':
    N = int(raw_input())
    newList = []
    for x in range(N):
        command = str(raw_input())
        inputList = command.split(" ")
        if inputList[0] == "insert":
            newList.insert(int(inputList[1]) ,int(inputList[2]))
        elif inputList[0] == "print":
            print(newList)
        elif inputList[0] == "remove":
            newList.remove(int(inputList[1]))
        elif inputList[0] == "append":
            newList.append(int(inputList[1]))
        elif inputList[0] == "sort":
            newList.sort()
        elif inputList[0] == "pop":
            newList.pop()
        elif inputList[0] == "reverse":
            newList.reverse()
            
            
    #Tuple
    if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    t = tuple(integer_list)
    print(hash(t))
    
    
    #Swap Case
def swap_case(s):
    s = s.swapcase()
    return s

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result

    
    
    
    #SPLIT
    def split_and_join(line):
   spl = line.split(" ")
   spl = "-".join(spl)
   return spl
if __name__ == '__main__':
    line = raw_input()
    result = split_and_join(line)
    print result
    
    
    #NAME
    def print_full_name(first, last):
    print("Hello " + first + " " + last + "! You just delved into python.")

if __name__ == '__main__':
    first_name = raw_input()
    last_name = raw_input()
    print_full_name(first_name, last_name)
    
    
    #ADD CHAR
    def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    toReturn = ""
    return toReturn.join(l)

if __name__ == '__main__':
    s = raw_input()
    i, c = raw_input().split()
    s_new = mutate_string(s, int(i), c)
    print s_new
    
    #COUNT SUB
    def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string) - len(sub_string) + 1):
        if string[i] == sub_string[0]:
            flag = True
            for x in range(0, len(sub_string)):
                if string[i + x] != sub_string[x]:
                    flag = False
            if flag:
                count = count + 1
    return count

if __name__ == '__main__':

    
    
    
    #SETS
    if __name__ == '__main__':
    set1Length = raw_input()
    line = raw_input()
    line = line.split(" ")
    set1 = set(line)
    set2Length = raw_input()
    line = raw_input()
    line = line.split(" ")
    set2 = set(line)
    l1 =list(set1.difference(set2))
    l2 =list(set2.difference(set1)) 
    l2 = l1 + l2
    l2.sort(key=int)
    for x in l2:
        print(x)
