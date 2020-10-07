# string counter

string = input('Enter the string : ')
string = string.lower()
vowels = {'a':0,'e':0,'i':0,'o':0,'u':0}
for x in string:
  if x=='a':
    vowels['a']+=1
  if x=='e':
    vowels['e']+=1
  if x=='i':
    vowels['i']+=1
  if x=='o':
    vowels['o']+=1
  if x=='u':
    vowels['u']+=1
for x, y in vowels.items():
  print(x,'-',y)
