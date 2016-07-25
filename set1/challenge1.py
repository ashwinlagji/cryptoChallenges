
def to_base64(hex_string):
    import base64
    import binascii
    
    x = binascii.unhexlify(hex_string)
    print "plain text :",x
    base64_str = base64.b64encode(x)
    print "base64 encoded :",base64_str
    
def main(abc):
    to_base64(abc)
    
if __name__=="__main__":
    import sys
    main(sys.argv[1])

