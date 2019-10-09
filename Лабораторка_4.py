
import math

def frange(start, stop = None, step = None):
    if stop == None:
        stop = start + 0.0
        start = 0.0
    if step == None:
        step = 1.0
    while True:
        if step > 0 and start >= stop:
            break
        elif step < 0 and start <= stop:
            break
        yield (start) # return float number
        start = start + step

def e(x):
    result = 0.0
    for i in range(0, 171):
        result += math.pow(x, i) / math.factorial(i)
    return result

def output(x, y, r = 6):
    print(x, '\t', round(y, r), '\t', round(e(x), r), '\t', round(e(x) - y, r))

def main():
    print('=================================================\n', 'X\t Y\t standart\t error\n', '================================================')
    y = None
    xn = -2
    step = 0.5
    xs = 3
    for x in frange(xn, xs + step, step):
        if (-1 <= x and x <= 0):
            try: 
                y = math.cos(x)*math.cos(x)
            except ValueError:
                print(x, '\t', 'not define')
            else:
                y = math.cos(x)*math.cos(x)
                output(x, y)
        elif (0 <= x and x <= 2):
            try: 
                y = math.cos(x/2)/math.cos(x+0.5)
            except ValueError:
                print(x, '\t', 'not define')
            else:
                output(x, y)

if __name__ == "__main__":
    main()