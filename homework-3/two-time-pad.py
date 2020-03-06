def xor(a, b):
    return "{:x}".format(int(a, 16) ^ int(b, 16))

hexes =     ['7f4d155f585c1f405e59531345525c115e4313425e174355554c4a5612151810'] 
hexes.append('5f555b4916555b5f52145f4715514d4517445b5842175f5e531951405e5d5754')
hexes.append('5451505c4519465c5214445646435d5243104459585458105f4a185746514d5e')
hexes.append('5c5b155c5f545b4017405913425b59451751135c50591053575718575c145643')
hexes.append('6b5b40105b4c414017565313415b5d115458525f56521049594c18445a475111')
hexes.append('665c5c4316504114561442564647185e511047595417755d534b5f565d574011')
hexes.append('665c5a4545585c50441459551550595f535c56421154515e165b5d5f5a535145')
hexes.append('7b524c5f43195e5b415116475d5c4b5417475b5e115b5f46531957475b514b42')

file = open('test.txt', 'w')

lookFor = 'This is a test of the Emergency '.encode().hex()

print(type(hexes[0]))
print(xor(hexes[0], hexes[1]))
value = xor(hexes[0], hexes[1])
print(value)
print(bytes.fromhex(value).decode('ascii'))

for i in range(0, len(hexes) - 1):
    for j in range(i + 1, len(hexes)):
        file.write(f'Hex: {i} xor {j}: ')
        m1XorM2 = xor(hexes[i], hexes[j])
        uniqueMessage = xor(m1XorM2, lookFor)
        file.write(bytes.fromhex(uniqueMessage).decode('ascii') + '\n')