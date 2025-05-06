### Write a function that computes the volume of a sphere given its radius
import math

def vol(x):
    vsphere = (4/3)*math.pi*x**3
    return vsphere
print(vol(2))

### Write a function that checks whether a number is in a given range (inclusive of high and low)
def check(n,low,high):
    if n in range(low,high+1):
        return f'{n} is in the range between {low} and {high}'
    else:
        return f'Is not in the range between'
print(check(5,2,7))


### Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
def uplow(s, i=0, low=0, upp=0):

    # Base case: If we've reached the end of the string, return the counts
    if i >= len(s):
        return upp, low
    
    # Get the current character
    current_char = s[i]

    if current_char.isupper():
        upp += 1
    elif current_char.islower():
        low += 1
    
    # call the next character
    return uplow(s, i+1, low, upp)

inp ='Hello Mr. Rogers, how are you this fine Tuesday?'
ucount, lcount = uplow(inp)
print(f'Uppercase: {ucount}')
print(f'Lowercase: {lcount}')

### Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unq(lst):
    return set(lst)

unique_list = list(unq([1,1,1,1,2,2,3,3,3,3,4,5]))
print(unique_list)

### Write a Python function to multiply all the numbers in a list.
def times(ls):
    res = 1
    for i in ls:
        res *= i
    return res
print(times([1,2,3,-4]))    

### Write a Python function that checks whether a word or phrase is palindrome or not.
def palindrome(word):
    p = word.lower().replace(' ', '')
    return p == p[::-1]
print(palindrome('Oso'))

### Write a Python function to check whether a string is pangram or not. 
### (Assume the string passed in does not have any punctuation)
import string

def ispangram(word, alphabet=string.ascii_lowercase):
    alph = set(alphabet)
    phrase = word.replace(' ','').lower()
    return alph == set(phrase)
print(ispangram("The quick brown fox jumps over the lazy dog"))
