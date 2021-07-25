##>Count the number of coins + value by weight
#>For each coin:
#   >>Ask how much they weigh
#    >>Calculate how many coins by this weight
#    >>Update total value
#>Print the total by quantity + total by value

coins = ['1p', '2p', '5p', '10p', '20p', '50p', '£1', '£2']
weight_list = []
for coin in coins:
    print('What is the weight of your' ,coin, 'pieces in GRAMS?')
    weight = input()
    weight_list.append(weight)
    
onep = int(weight_list[0]) % 3.56
print('you have', round(onep), '1p pieces')
total = round(onep) * 1
twop = int(weight_list[1]) % 7.12
print('you have', round(twop), '2p pieces')
total = total + (round(twop) * 2)
fivep = int(weight_list[2]) % 3.25
print('you have', round(fivep), '5p pieces')
total = total + (round(fivep) * 5)
tenp = int(weight_list[3]) % 6.5
print('you have', round(tenp), '10p pieces')
total = total + (round(tenp) * 10)
twentyp = int(weight_list[4]) % 5.0
print('you have', round(twentyp), '20p pieces')
total = total + (round(twentyp) * 20)
fiftyp = int(weight_list[5]) % 8
print('you have', round(fiftyp), '50p pieces')
total = total + (round(fiftyp) * 50)
onepound = int(weight_list[6]) % 9.5
print('you have', round(onepound), '£1 pieces')
total = total + (round(onepound) * 100)
twopound = int(weight_list[7]) % 12
print('you have', round(twopound), '£2 pieces')
total = total + (round(twopound) * 200)
print('You have', total, 'pence total.')

