e = input('Write an equasion: ')
e1 = e.split(' ')
answer = 0
action = len(e1)


for i in e1:
    action -= 1
    if e1[action] == '+':
        answer += int(e1[0]) + int(e1[1])
    elif e1[action] == '-':
        answer += int(e1[0]) - int(e1[1])
    elif e1[action] == '*':
        answer += int(e1[0]) * int(e1[1])
    elif e1[action] == '/':
        answer +=int(e1[0]) / int(e1[1])
print(answer)
    #if e1[action] == '+':
     #   answer += int(e1[2])
    #elif e1[action] == '-':
     #   answer += int(e1[2])
    #elif e1[action] == '*':
     #   answer += int(e1[2])
    #elif e1[action] == '/':
     #   answer += int(e1[2])
    #print(answer)

#if e1[-1] == '+':
 #   print(int(a) + int(e1[-1]))
#elif e1[-1] == '-':
 #   print(int(a) + int(e1[-1]))
#elif e1[-1] == '*':
  #  print(int(a) + int(e1[-1]))
#elif e1[-1] == '/':
 #   print(int(a) + int(e1[-1]))