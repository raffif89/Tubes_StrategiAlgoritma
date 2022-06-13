import time

def main():
    # Kunci yang akan dicocokkan
    angka = [(0,0,1,0,0)]

    peluang = []
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    for m in range(10):
                        dataMasuk = i,j,k,l,m
                        peluang.append(dataMasuk)

    hasil = False
    for kunci in angka:
        for i in peluang:
            print(i)
            if (i == kunci):
                hasil = True
        print("\nThe key",kunci, "matches")
        print()

# Running
start_time = time.time()
main()
print("Time : %s seconds" % (time.time() - start_time))
print()