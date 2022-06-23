liczby = [5,10,15,20,25,30]
liczby.append(35)
print(len(liczby))
print(liczby[1:4])
print(liczby[:-1])

liczby.reverse()
print(liczby)
liczby.pop(4)
print(liczby)
print(max(liczby))
print(sum(liczby))
print(sum(liczby)/len(liczby))
