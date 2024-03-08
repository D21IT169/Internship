def hetero(stri):
    stri = stri.lower()
    
    B = set()

    for i in stri:
        if i in B:
            return False
        else:
            B.add(i)
    return True

stri = "hetvi"
result = hetero(stri)

if result:
    print("yes, every char is unique")
else:
    print("no")

    
        