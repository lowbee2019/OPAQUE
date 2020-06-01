from Crypto.Util import number
import random

def str2hex(s):
    return ''.join([hex(ord(c)).replace('0x','') for c in s])

def init():
    n = number.getPrime(128)
    g = random.randint(2,n-1)
    return (n,g)

def init_user(s,g,n):
    x = int(str2hex(s),16)
    IDU = random.randint(2,n-1)
    PrivU = random.randint(2,n-1)
    PubU = pow(g,PrivU,n) %n
    gx = pow(g,x,n) %n
    return (gx,x,IDU,PubU,PrivU)

def init_server(g,n):
    y = random.randint(2,n-1)
    IDS = random.randint(2,n-1)
    PrivS = random.randint(2,n-1)
    PubS = pow(g,PrivS,n) %n
    gy = pow(g,y,n) %n
    return (gy,y,IDS,PubS,PrivS)

def Exchange(gx,IDU,PubU,gy,IDS,PubS):
     d = hash(gx+IDS)
     e = hash(gy+IDU)
     return (d,e)

def Calc_Key(gy,PubS,e,d,PrivU,x,n):
    key = hash(pow(gy*pow(PubS,e,n)%n,d*PrivU+x %n,n)%n)
    return key

if __name__ =="__main__":
    s = "lowbee"
    n,g = init()
    gx, x, IDU, PubU, PrivU = init_user(s,g,n)
    gy, y, IDS, PubS, PrivS = init_server(g,n)
    d,e = Exchange(gx,IDU,PubU,gy,IDS,PubS)
    UK = Calc_Key(gy,PubS,e,d,PrivU,x,n)
    SK = Calc_Key(gx,PubU,d,e,PrivS,y,n)
    if UK == SK:
        print("Suceess!The key is:",UK)
    else:
        print("Failed!")


