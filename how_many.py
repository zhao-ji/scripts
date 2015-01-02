from itertools import permutations

arrange_of_ten = permutations('0123456789')

num = 0

for item in arrange_of_ten:
    will_be_div_by_11111 = int(''.join(item))
    if will_be_div_by_11111 % 11111 is 0:
        num += 1

print num
