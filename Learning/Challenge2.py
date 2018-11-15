ip= input("Whats your ip adress? ")
segment=1
length=-1
if ip == '':
    print('you didnt entered anything, please try again')
else:
    for i in range(len(ip)):
        length +=1
        if ip[i] in '.':
            print("The segment {0}, have {1} numbers".format(segment, length))
            segment += 1
            length = -1
    if ip[i]!='.':
        length += 1
        print("The segment {0}, have {1} numbers".format(segment, length))