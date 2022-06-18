st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word[0] == 's':
        print(word)

for num in range(0,11,2):
    print(num)

myls = [x for x in range(1,51) if x%3 ==0]
print(myls)

st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len (word)%2 == 0:
        print(word+' even!')

for num in range(1,101):
    if num %3 == 0 and num %5 == 0:
        print("FizzBuzz")
    elif num %3 ==0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

st = 'Create a list of the first letters of every word in this string'
for word in st.split():
    print(word[0])
