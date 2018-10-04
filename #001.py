#Find the sum of all the multiples of 3 or 5 below 1000.
def ProjectEuler1():
    total = 0
    number_to_sum_to = 1000
    for n in range(number_to_sum_to):
        if n % 3 == 0 or n % 5 == 0:
            total += n
    print(total)
ProjectEuler1()

#After running script, answer printed was 233168