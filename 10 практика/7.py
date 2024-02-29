c = 2
def som(a):
    if a == 1:
        exit()
    else:
        global c
        if a % c == 0:
            a /= c
            print(c)
        else:
            if c > 9:
                print("нет простых множителей")
                exit()
            c += 1
        som(a)
som(378)