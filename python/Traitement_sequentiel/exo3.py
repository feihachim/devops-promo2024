a = input("Donner un caractère\n")
b = input("Donner un caractère\n")
print("Avant permutation,a={0} et b={1}".format(a, b))
"""
temp = a
a = b
b = temp
"""
a, b = b, a
print("Après permutation,a={0} et b={1}".format(a, b))
