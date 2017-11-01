import os
import sys
import time
from hashlib import sha256, sha224, sha384, sha1, sha512

list_size = 1000000

def bloom3(dictfile, inputfile, outputfile, bitlist):
    #Use three hash functions
    print('Beginning Bloom check with 3 hashes:\n')
    start_time = time.time()
    returnlist = []
    f = open(dictfile, 'r')

    line = f.readline()
    while(line != ''):
        hash_browns = sha256(line).hexdigest()
        hash_browns1 = sha224(line).hexdigest()
        hash_browns2 = sha384(line).hexdigest()

        bit0 = int(hash_browns, 16) % list_size
        bit1 = int(hash_browns1, 16) % list_size
        bit2 = int(hash_browns2, 16) % list_size
        
        bitlist[bit0] = 1
        bitlist[bit1] = 1
        bitlist[bit2] = 1

        line = f.readline()

    f.close()
    f = open(inputfile, 'r')

    line = f.readline()
    line = f.readline()
    while(line != ''):
        hash_browns = sha256(line).hexdigest()
        hash_browns1 = sha224(line).hexdigest()
        hash_browns2 = sha384(line).hexdigest()

        bit0 = int(hash_browns, 16) % list_size
        bit1 = int(hash_browns1, 16) % list_size
        bit2 = int(hash_browns2, 16) % list_size
        
        if(bitlist[bit0] == 1 and bitlist[bit1] == 1 and bitlist[bit2] == 1):
            returnlist.append('maybe\n')
            print(line + ' maybe\n\n')
        if(bitlist[bit0] == 0 or bitlist[bit1] == 0 or bitlist[bit2] == 0):
            returnlist.append('no\n')
            print(line + ' not in list\n\n')

        line = f.readline()

    f.close()
    f = open(outputfile, 'w')

    for answer in returnlist:
        f.write(answer)

    f.close()
    print("\n--- %s seconds ---\n" % (time.time() - start_time))
    count = 0
    for bit in bitlist:
        if(bit == 1):
            count+=1
    print count
    print " bits set\n"

    #print bitlist

def bloom5(dictfile, inputfile, outputfile, bitlist):
    #Use three hash functions
    print('Beginning Bloom check with 5 hashes:\n')
    start_time = time.time()
    returnlist = []
    f = open(dictfile, 'r')

    line = f.readline()
    while(line != ''):
        hash_browns = sha256(line).hexdigest()
        hash_browns1 = sha224(line).hexdigest()
        hash_browns2 = sha384(line).hexdigest()
        hash_browns3 = sha1(line).hexdigest()
        hash_browns4 = sha512(line).hexdigest()

        bit0 = int(hash_browns, 16) % list_size
        bit1 = int(hash_browns1, 16) % list_size
        bit2 = int(hash_browns2, 16) % list_size
        bit3 = int(hash_browns3, 16) % list_size
        bit4 = int(hash_browns4, 16) % list_size
        
        bitlist[bit0] = 1
        bitlist[bit1] = 1
        bitlist[bit2] = 1
        bitlist[bit3] = 1
        bitlist[bit4] = 1

        line = f.readline()

    f.close()
    f = open(inputfile, 'r')

    line = f.readline()
    line = f.readline()
    while(line != ''):
        hash_browns = sha256(line).hexdigest()
        hash_browns1 = sha224(line).hexdigest()
        hash_browns2 = sha384(line).hexdigest()
        hash_browns3 = sha1(line).hexdigest()
        hash_browns4 = sha512(line).hexdigest()

        bit0 = int(hash_browns, 16) % list_size
        bit1 = int(hash_browns1, 16) % list_size
        bit2 = int(hash_browns2, 16) % list_size
        bit3 = int(hash_browns3, 16) % list_size
        bit4 = int(hash_browns4, 16) % list_size
        
        if(bitlist[bit0] == 1 and bitlist[bit1] == 1 and bitlist[bit2] == 1 and bitlist[bit3] == 1 and bitlist[bit4] == 1):
            returnlist.append('maybe\n')
            print(line + ' maybe\n\n')
        if(bitlist[bit0] == 0 or bitlist[bit1] == 0 or bitlist[bit2] == 0 or bitlist[bit3] == 0 or bitlist[bit4] == 0):
            returnlist.append('no\n')
            print(line + ' not in list\n\n')

        line = f.readline()

    f.close()
    f = open(outputfile, 'w')

    for answer in returnlist:
        f.write(answer)

    f.close()
    print("\n--- %s seconds ---\n" % (time.time() - start_time))
    count = 0
    for bit in bitlist:
        if(bit == 1):
            count+=1
    print count
    print " bits set\n"

    #print bitlist

def main():

    sys.argv[1:]
    dictfile = sys.argv[1]
    inputfile = sys.argv[2]
    output3 = sys.argv[3]
    output5 = sys.argv[4]
    bitlist = [0] * list_size
    wordlist = []

    #dictfile = "dictionary.txt"
    #inputfile = "sample_input.txt"
    #output3 = "output3.txt"
    #output5 = "output5.txt"
    
    
    bloom3(dictfile, inputfile, output3, bitlist)
    bitlist = [0] * list_size
    bloom5(dictfile, inputfile, output5, bitlist)

if __name__ == '__main__':
    main()

