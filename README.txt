run in the windows command prompt with: python Assignment1.py dictionary.txt sample_input.txt output3.txt output5.txt

Questions:
a) I used the sha family of hash functions for this assignment. I used them because 
of the fact that they are cryptographic and thus much less easily broken. The only
downside to this is that they take more time to run. I used sha1 output = 160 bits, sha224
output = 224 bits, sha256 output = 256 bits, sha384 output = 384 bits, and sha512 which has
output = 512 bits. In both the 3 and 5 hash functions, my bit array/list size is 1 million.
This was to ensure that their would be enough 0 bits left that some of the passwords not in the 
list would return a no, while not dragging out the times too much. In the 3 hash case, using the
 supplied dictionary file, 845979 bits are set to 1. In the 5 hash scenario, that number swelled to 
 955524 bits being set as 1. I used the hashlib library in my code to get the sha functions.
 
b) In the 3 hash bloom filter, one password takes --- 4.38100004196 seconds --- to check, including
the time needed to set the array. In the 5 hash bloom filter, it takes --- 7.05499982834 seconds ---.
The former performs better because cryptographic hash functions are time intensive, and the latter performs
more of them. If I had used non-cryptographic hash functions, these times would have been faster, but 
the hashes would have been less secure.

c)  False negatives, aka reporting that an element is not in the dictionary when it is, are not
 possible. This is because, if a password was in the dictionary, then its bit pattern has to already
be set as ones. This bit pattern would be the same when the password in question is later hashed, and set bits
 cannot be reset by the bloom filter mid run. False positives on the other hand are possible in a bloom
filter. This is because it could just happen that hashing unmatching dictionary words end up setting all
 of the bits that the password input checks. The probability is = (1 - e^(-kB/N))^k where B = number of 
 bad words, k = number of hash functions and N = the size of the bit array.
 In the dictionary we have, B = 623518 since there are that many words in the dictionary.txt.
 
 So, I will do this calculation for for the 5 hash bloom filter, where k = 5
 P = (1 - e^(-5 * 623518/1000000))^5 = 79.7% false positive rate
 and where k = 3 
  P = (1 - e^(-3 * 623518/1000000))^3 = 60.5% false positive rate
 
sha1 has an output range of 160