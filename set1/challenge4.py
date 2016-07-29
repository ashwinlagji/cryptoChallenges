import binascii

from challenge3 import breakSingleByteXOR,freqs


def score(s):
    #    print s
    score = 0
    for i in s:
        c = i.lower()
        if c in freqs:
            score += freqs[c]
            #    print score
    return score


def challenge4(fileName):
    def key(p):
        return score(p)
    
    fh=open(fileName,'r')
    lines=[]
    for line in fh:
        t=binascii.unhexlify(line.strip())
        lines.append(breakSingleByteXOR(t)[1])
    print max([(line) for line in lines],key=key)
    
    
if __name__=="__main__":
    import sys
    challenge4(sys.argv[1])