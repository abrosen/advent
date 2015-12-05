import hashlib 

ans = 1
secret = "ckczppom"

while True: 
    test =  secret + str(ans)
    m = hashlib.md5()

    m.update(test.encode("utf-8"))
    s = m.hexdigest()
    if s[:6] == '000000':
        print(s)
        print(ans)
        break
    ans  += 1
        
