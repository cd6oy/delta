def tokenizer(input: str, start):
    p = start
    while p != len(input):
        if(input[p] in ['(', ')', ' '] and p == start):
            return p+1
        elif(input[p] in ['(', ')', ' '] and p != start):
            print(p)
            return p
        else:
            p += 1