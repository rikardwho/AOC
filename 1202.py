import csv

def add(a, b):
    return a + b

def mult(a, b):
    return a * b

def run(p, i):
    if int(p[(i * 4)]) == 1:
        p[int(p[(i * 4) + 3])] = add(int(p[int(p[(i * 4) + 1])]), int(p[int(p[(i * 4) + 2])]))

    if int(p[(i * 4)]) == 2:
        p[int(p[(i * 4) + 3])] = mult((int(p[int(p[(i * 4) + 1])])), int(p[int(p[(i * 4) + 2])]))

    if int(p[(i * 4)]) == 99:
        print(p)
        return

    run(p, i+1)

def main():
    with open("program.csv") as program:
        p = list(csv.reader(program))
    p = p[0]

    run(p, 0)
 

if __name__ == "__main__":
    main()
