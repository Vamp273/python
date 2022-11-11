N = int(input("Fibonacci Series : "))

#initialize the list with starting elements: 0, 1
fib = [0,1]

if N>2:
	for i in range(2, N):
		#next elment in series = sum of its previous two numbers
		nextElement = fib[i-1] + fib[i-2]
		#append the element to the series
		fib.append(nextElement)

print(fib)