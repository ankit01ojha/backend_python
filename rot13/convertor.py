def convert(n):
    new=""
    for i in range(0,len(n)):
        if(str.isupper(n[i])):
            if(90-(ord(n[i])))>=13:
                new += chr(ord(n[i]) + 13)
            else:
                new+=chr(64+ (13-(90-(ord(n[i])))))
        elif(str.islower(n[i])):
            if (122 - (ord(n[i]))) >= 13:
                new += chr(ord(n[i]) + 13)
            else:
                new += chr(96 + (13 - (122 - (ord(n[i])))))
        else:
            new+=n[i]

    return new

print convert('Ankit')

