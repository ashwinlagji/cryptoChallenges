
def xor_two_ascii(s1,s2):
        return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))



def xor_two_buffers(a_hex_str,b_hex_str):
    import binascii
    x = binascii.unhexlify(a_hex_str)
    y = binascii.unhexlify(b_hex_str)
    
    if(len(x)==len(y)):
        output = xor_two_ascii(x,y)
        print output
        output = binascii.hexlify(output)
        print output
    else:   
        print "length mismatch"
    

def main(a,b):
    xor_two_buffers(a,b)
    
if __name__=="__main__":
    import sys
    main(sys.argv[1],sys.argv[2])