from time import time
start = time()
print(start)

# Python program to create acronyms
word = "Artificial Intelligence DELL "
text = word.split()
print(text)

a = " "
for i in text:
    a = a+str(i[0]).upper()
print(a)

end = time()
print(end)

execution_time = end - start
print("Execution Time : ", execution_time)