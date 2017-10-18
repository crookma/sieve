# By: Magnus Crooke, File Name: unit6.py, last modified 10-18-17, This program gives you the prime numbers from a list.
def main():
    """
    This  function asks for a maximum number and finds all of the prime numbers from 2 to the maximum number that the
    user gave.
    :return:This function returns the prime numbers from a list.
    """
    random = []
    max_num = int(input("What is the maximum number you would like to deal with?:"))
    for x in range(2, max_num):
        random.append(x)
    prime_num = []
    while len(random) > 0:
        prime_num.append(random[0])
        divisur = random[0]

        for y in random:

            if y % divisur == 0:
                random.remove(y)
    print("The list of prime numbers is:")
    print(prime_num)

main()