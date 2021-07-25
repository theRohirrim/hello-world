#Play the 99 bottles song#

#>Play 99 bottles song
#>>'set counter to 99'
#>>> ' IF counter is 0'
#        'no more bottles and terminate'
#>>>'ELIF counter is 1'
#        'change to singular bottle and decrement counter'
#>>>'ELSE lyrics as usual and decrement counter
#>>'return strings of the lyrics with counter'

counter = 99
while counter > 0:
    if counter == 1:
        print(counter,'bottle of beer on the wall,',counter,'bottle of beer.')
        print('Take one down and pass it around, no more bottles of beer on the wall.')
        print('')
        counter = counter - 1
    else:
        print(counter,'bottles of beer on the wall,',counter,'bottles of beer.')
        counter = counter - 1
        print('Take one down and pass it around,', counter, 'bottles of beer on the wall.')
        print('')
else:
    print('No more bottles of beer on the wall, no more bottles of beer.')
    print('Go to the store and buy some more, 99 bottles of beer on the wall.')
    print('')

