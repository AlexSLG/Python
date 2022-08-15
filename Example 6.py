def hanoi (disc,Torre1=1,Torre2=2,Torre3=3):
    if disc==1:
        print (Torre1,"a",Torre3)
    else:
        hanoi(disc-1,Torre1,Torre3,Torre2)
        print(Torre1,"a",Torre3)
        hanoi (disc-1,Torre2,Torre1,Torre3)
    return
n=int(input("Ingrese la cantidad de discos: "))
hanoi(n)