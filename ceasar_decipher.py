letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x',
'y','z']
inpt = input('>>>')

shift = int(input("Enter Shift: "))
outpt = []
for i in inpt:
    if i == ' ':
        outpt.append(' ')
    else:
        if i in letters:
            index = letters.index(i)
            final_index = index-shift
            if final_index<0:
                final_index=final_index+26
            outpt.append(letters[final_index])
print(outpt)
