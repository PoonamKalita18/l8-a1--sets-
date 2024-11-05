S = {1,2,2,3,4,4,4,4}
print('set 1 :',S)

S.add(6)
print('updated set', S)

S1 = S
S2 = {2,3,3,4,5}

print('\n S1',S1)
print('Set 2', S2)
print('difference')
print(S1.difference(S2))
print("symmetric difference")
print(S1.symmetric_difference(S2))