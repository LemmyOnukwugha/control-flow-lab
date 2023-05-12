fibo = [0,1]

for i in range (2,50):
    fibo.append (fibo [i-1] + fibo [i-2])

for i in range (0,50):
    print(f"term: {i} / number: {fibo[i]}")
