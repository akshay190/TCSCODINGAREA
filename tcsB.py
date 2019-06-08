def num2word(num):
    n20=[' ',' '," Twenty "," Thirty "," Fourty "," Fifty "," Sixty "," Seventy "," Eighty "," Ninety "]
    n19=[" Zero "," One "," Two "," Three "," Four "," Five "," Six "," Seven "," Eight "," Nine "," Ten ",
         " Eleven "," Twelve "," Thirteen "," Fourteen "," Fifteen "," Sixteen "," Seventeen ",
         " Eighteen "," Nineteen "]
    if(num<20):
        return(n19[num])
    elif(num==20):
        return(" Twenty ")
    elif(num<100):
        if(num%10==0):
            return(n20[num//10])
        else:
            return(n20[num//10]+n19[num%10])
    else:
        if(num==100):
            return(" Hundred ")
        elif(num<1000):
            if(num%100==0):
                return(num2word(int(num/100))+" Hundred ")
            else:
                return(num2word(int(num/100))+" Hundred "+num2word(int(num%100)))
        elif(num==1000):
            return("Thousand")
        elif(num==99999):
            return("Ninety Nine Thousand Ninety Nine Hundred Nine")
        else:
            return(num2word(int(num/1000))+" Thousand "+num2word(num%1000))

x,y=input().split()
x=int(x)
y=int(y)
i=1
while(1):
    if(x>90000):
        print("Out of bounds")
        break
    elif(y>90000):
        print("Out of bounds")
        break
    elif(x==y):
        print(x)
        break
    else:
        c1=num2word(x)
        c2=num2word(y)
        if([c1,c2]==sorted([c1,c2])):
            x=x*2
            y=y*2
        else:
            t1=x
            t2=y
            x=t1+t2
            y=t1+t2
            print(x)
            break
            

