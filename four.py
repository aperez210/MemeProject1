def read(s:bytes):
    args = s.split(b'|',1)
    if keyAuth(args[1]):
        print("key authenticated.")
        try:
            if args[0] == b'query':
                return b'haha nice'
        except:
            return b'api call failed'
        

def keyAuth(k:bytes):
    if k == b'key':
        return True