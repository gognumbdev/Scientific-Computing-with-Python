# encryption inspired by AES (Advanced Encryption Standard)
# Prabhas Chongstitvatana

key = "ABCDEFGHIJKLMNOP"
plaintext = "I LOVE PYTHON101"

def encrypt(key,text):
    t1 = oneround(key,text)
    t2 = oneround(key,t1)
    return t2

def oneround(key,text):
    t1 = addkey(key,text)
    t2 = subbyte(t1)
    t3 = shiftrow(t2)
    t4 = mixcolumn(t3)
    return t4

# xor key with text, keep it in printable range
def addkey(k,t):
    s= ""
    for i in range(len(k)):
        s += doxor(k[i],t[i])
    return s

# doxor xor ascii code of two characters c1, c2
def doxor(c1,c2):
    c3 = ord(c1) ^ ord(c2)
    c4 = makeprintable(c3)
    return c4

def makeprintable(c):
    c1 = ((c % 90) + 32 % 90)
    return chr(c1)

# substitute characters in t with pattern in subinput and suboutput
def subbyte(t):
    s = ""
    for i in range(len(t)):
        s += findreplace(t[i])
    return s

# findreplace use subinput and suboutput

def findreplace(c):
    c2 = suboutput[subinput.find(c)]
    return c2

# these two functions use "for", which we will learn later, just use
# it now
def createsubinput():
    s = ""
    for i in range(32,91):
        s += chr(i)
    return s

def createsuboutput():
    s = ""
    for i in range(33,91):
        s += chr(i)
    s += chr(32)
    return s

subinput = createsubinput()
suboutput = createsuboutput()

# rotate string one character to the right
def shiftonce(t):
    # when we shift right once that is the last character will move to be the first character of the plaintext 
    # and the rest( index 0 to index len(t)-2 ) of character will append to the last character which is now the first character of plaintext.
    #We can access the last character of plaintext with index -1 and rest of the plaintext except the last one with [:len(t)-1].
    t1 = t[-1]+t[:len(t)-1]
    return t1

def shiftrow(t):
    t1 = shiftonce(t)
    t2 = shiftonce(t1)
    return t2

# coefficients use in multiply with fix polynomial in mixcolumn
# fixpoly = "2311123111233112"
# we just hardcode it into the function
def mixcolumn(t):
    s = mulc(t[0], "2")
    s += mulc(t[1], "3")
    s += mulc(t[2], "1")
    s += mulc(t[3], "1")
    s += mulc(t[4], "1")
    s += mulc(t[5], "2")
    s += mulc(t[6], "3")
    s += mulc(t[7], "1")
    s += mulc(t[8], "1")
    s += mulc(t[9], "1")
    s += mulc(t[10], "2")
    s += mulc(t[11], "3")
    s += mulc(t[12], "3")
    s += mulc(t[13], "1")
    s += mulc(t[14], "1")
    s += mulc(t[15], "2")
    return s

def mulc(c1,c2):
    # Just find ascii value of c1 and ascii value of c2 with ord(character) after that multiplied them.
    c3 = ord(c1) * ord(c2)
    c4 = makeprintable(c3)
    return c4

def test():
    s = ""
    s += "1"
    s += "2"
    print(s)
    txt = "WHATEVER01234567"
    txt2 = subbyte(txt)
    print(plaintext)
    txt4 = oneround(key,plaintext)
    print(txt4)
    txt5 = encrypt(key,plaintext)
    print(txt5)

def main():
    key = input("Enter key : ")
    plaintext = input("Enter plaintext : ")
    ciphertext = encrypt(key, plaintext)
    print(ciphertext)
    
main()

#### End ######