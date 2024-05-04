import sys

# Gather our co
# de in a main() function
def func1(x):
    numList = []
    n = 5
    i = 0
    while i < n:
        numList.append(input())
        i = i + 1
    sum = 0
    for num in numList:
        sum += int(num)    
    print(str(numList)+" = "+str(sum))
   # print(sum)

def main():
    func1(5)
if __name__== "__main__":
    main()
#print('Hello there', sys.argv[1])