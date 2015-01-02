from itertools import permutations

num_5 = permutations('123456789',5)

if __name__ == "__main__":
    for item in num_5:
        value_5 = int(''.join(item))
        num_5_of_3 = permutations(''.join(item), 3)
        sum_value_3 = 0
        for n in num_5_of_3:
            sum_value_3 += int(''.join(n))
        if value_5 == sum_value_3:
            print value_5
        sum_value_3 = 0
