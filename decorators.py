import time

def timing(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args,**kwargs)
        end = time.time()
        print(f.__name__ +" took " + str((end-start)*1000) + " mil sec")
        return result
    return wrapper

@timing
def calcSquare(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result

@timing
def calcCube(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result

# main method
if __name__ == '__main__':
    array = range(1,100000)
    sq = calcSquare(array)
    cube = calcCube(array)
