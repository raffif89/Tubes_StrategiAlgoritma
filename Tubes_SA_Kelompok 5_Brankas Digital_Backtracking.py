import time

def findKey(kunci):
    mustBreak = False
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    for m in range(10):
                        data = (i,j,k,l,m)
                        print(data)
                        if kunci == data:
                            print("\nThe key",kunci, "matches")
                            print()
                            mustBreak = True
                            break
                        
                    if mustBreak: break
                if mustBreak: break
            if mustBreak: break
        if mustBreak: break

# Kunci yang akan dicocokkan
angka = [(0,0,1,0,0)]

# Running
start_time = time.time()
for kunci in angka:
    findKey(kunci)
print("Time : %s seconds" % (time.time() - start_time))
print()