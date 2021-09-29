#         group members
# Habib Gemmechu section 1 UGR/4012/12
# Felmeta Muktar section 2 UGR/3555/12
# Usmael Abdurhaman section 2 UGR/6575/12 
# Yared Namssi section 3 UGR/1548/12

#p,q stands for the 2 prime numbers used for encryption, m is the totient function
def isprime(num): # function that check if p and q are prime
    for i in range(2, num//2):
        if(num%i==0):
            return False
        else:
            i+=1
        return True
def gcd(num1,num2): # function to calculate gcd
    if (num1%num2==0):
        return num2
    else:
        temp=num1%num2
        return gcd(num2,temp)
def value_of_e(p,q,m): # function to calculate e which is coprime to both n and m
    for i in range(2, m):
        if(i!=p and i!=q and gcd(m,i)==1):
            e=i
            return e
        else:
            i+=1
def value_of_d(m,e): # function to calculate value of d
    i=1
    while(i!=0):
        if((i*e)%m==1):
            d=i
            i=0
            return d
        else:
            i+=1
def encryption(e,n,value): # function to encrypt
    temp=value**e
    encrypt=temp%n
    return encrypt

def decryption(d,n,value2): # function to decrypt
    temp=value2**d
    decrypt=temp%n
    return decrypt
# main part of the code
p=int(input( "enter p: "))
q=int(input( "enter q: "))
while(isprime(p)==False or isprime(q)==False or p==q):
    if(isprime(p)==False):
        p=int(input( "p must be prime. Enter p: "))
    elif(isprime(q)==False):
        q=int(input( "q must be prime. Enter q: "))
    else:
        q=int(input( "p and q are equal.Please change q:"))
        
n=p*q
m=(p-1)*(q-1)
e=value_of_e(p,q,m)
d=value_of_d(m,e)
#public key=(e,n) and private key=(d,n)
h=22 # sample data to check
enc=encryption(e,n,h)
dec=decryption(d,n,enc)
print("encryption of h is: " enc)
print("decryption of h is: "dec)

