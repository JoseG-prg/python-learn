list = [1, 4, 7, 8, 10, 12, 15]
winner = 10

i = (len(list)/2)
i = int(i)
print (i)

while list[i] != int(winner):
  if winner < list[i]:
    i = i - (i/2)
    i = int(i)
  elif winner > list[i]:
    i = i + (i/2)
    i = int(i)

if list[i] == winner:
 print("winner!")