

def main():
    num = 1000
    count = 0

    while(num < 10000):
        aux = str(num)
        i = 0
        while(i<4):
            print(aux)
            if(aux[i]=="7"):
                count+=1
            elif(aux[i]=="0"):
                count=0
                break
            i+=1
        if(count >= 3):
            print(num)
        num+=1

main()