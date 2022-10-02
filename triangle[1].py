from time import sleep                                     
rall = int(input("brp: "))                          
re = input("what: ")
res = ("∆")
for i in range(rall):
        print((res*(1+2*i)).center(1+2*25))
        sleep(0.5)