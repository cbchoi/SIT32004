# calculate 10!

@profile
def factorial(num):
    if num == 1:
        return 1
    else:
        print("Calculating " + str(num) + "!")
        return factorial(num -1) * num

@profile
def profiling_factorial():
    value = 10
    result = factorial(value)
    print("10!= " + str(result))

if __name__ == "__main__":
    profiling_factorial()