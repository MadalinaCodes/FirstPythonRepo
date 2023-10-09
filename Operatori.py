'''Operatori:
aritmetici: +, *, /, % (modulo - aflarea restului impartirii)
de comparare: < >, ==, !=, >=, <=
logici: and, or'''

a = 3
b = 5

print(a + b) # 3+5 => 8
print(a == b) # a este egal cu b? => False
print(a < b and a < 4) # True SI True => True
print(a < b or a < 2) # True SAU False => True

# cu mama sau tata sau (cu bunicul si bunica)
mama = True
tata = True
bunicul = True
bunica = True
print(mama or tata or (bunicul and bunica))


