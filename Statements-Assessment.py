#1
st = 'Print only the words that start with s in this sentence' 
for s in st.split(): 
    if s[0] == 's':
        print(s)

#2
even = [x for x in range(0,11) if x%2==0]
print(even)
#list(range(0,11,2)) ALTERNATIVE SOLUTION

#3
thirds = [p for p in range(1,51) if p%3==0]
print(thirds)

#4 
st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word)%2==0:
        print(word,'<-- has an even lenght!')

#5
for num in range(1,101):
    if num%3==0 and num%5==0:
        print('OK')
    elif num%3==0:
        print('K')
    elif num%5==0:
        print('O')
    else:
        print(num)

st = 'Create a list of the first letter of every word in this string'
st = [word[0] for word in st.split()]