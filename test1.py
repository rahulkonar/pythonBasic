import sys

# Gather our code in a main() function
def func1(n):
    print(n)
def main():
    func1(sys.argv[1])
    print("1")
if __name__=="__main__":
    main()
#print('Hello there', sys.argv[1])