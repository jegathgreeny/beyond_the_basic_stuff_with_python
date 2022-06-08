import wizcoin

# The ints are passed to __init__().
purse = wizcoin.WizCoin(10, 15, 7)
print(purse)

print(f"G: {purse.galleons}, S: {purse.sickles}, K: {purse.knuts}")
print(f"Total value: {purse.value()}")
print(f"Weight: {purse.weight()} g")


change = wizcoin.WizCoin(23, 4, 7)
print(change.sickles)
change.sickles +=  12
print(change.sickles)