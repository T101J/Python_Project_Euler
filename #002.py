#By conside,ring the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
def ProjectEuler2():
	Fibonacci_seq = [1,2]
	while(True):
		Fibonacci_next = Fibonacci_seq[-1] + Fibonacci_seq[-2]
		if Fibonacci_next > 4000000:
			break
		Fibonacci_seq.append(Fibonacci_next)
	
	total = 0

	for n in Fibonacci_seq:
		if n % 2 == 0:
			total += n
		print(total)

ProjectEuler2()




