n = int(input()) 
number = input()

st=[] 
count = 0
for num in number[::-1]:
    st.append(num)
    count+=1
    if count == 3:
        st.append(',')
        count = 0
    
print("".join(st[::-1]).strip(',')) 