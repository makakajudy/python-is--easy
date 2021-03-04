mylist = []
fizz = []
buzz = []
fizz_buzz = []
prime = []
even = []
n = 100


def prime_test(n):

    # for d in range(1, n + 1):  # d->iterator, n+1 ->last digit in the  range
    if n == 1:  # this statement eliminates 1 since it not a prime number
        return False
    for i in range(2, n):  # i iterator/the loop start at 2 to n which will exclude the last number/digit being
        # tested
        if n % i == 0:  # if n is divisible(no reminder) by any value of i then it not a prime
            break # return not prime

        else:
            #prime.append(n)
            return "prime"  # if there is a remind for any n divide by i then n is a prime

    return n


for number in range(1, n + 1):
    prime.append(prime_test(number))
    mylist.append(prime_test(number))

    if number % 3 == 0 and number % 5 == 0:
        fizz_buzz.append(number)
        mylist.append('fizzbuzz')

    elif number % 5 == 0:

        buzz.append(number)
        mylist.append('buzz')
    elif number % 3 == 0:

        fizz.append(number)
        mylist.append('fizz')
    else:
        mylist.append("neither")
print()

print(f'numbers divisible by 3:{fizz}')
print(f'numbers divisible by 5:{buzz}')
print(f'numbers divisible by 3 and 5:{fizz_buzz}')

print(f'Final List with prime/not prime:{prime}')
'''print both if its divisibility either fizz/buzz/fizzbuzz
 And if its prime or not eg 3 is fizz and prime while 5 is buzz and prime'''
print(f'Final list fizz,buzz,fizzbuzz and prime{mylist}')