with open('retrived-binary.txt') as f:
    retrived_string = f.read()
with open('binary.txt') as f:
    original_string = f.read()
ls=[]
for i,(s1,s2) in enumerate( zip(original_string,retrived_string)):
    if s1!=s2:
        ls.append(i)

print(len(retrived_string)-len(original_string))