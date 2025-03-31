r, c = map(int, input().split())

words = []
flag = 0

for _ in range(r):
    word = input()
  

    dots = c -len(word)
    if dots % 2 == 1:
        if flag == 0:
            word += '.'
        else:
            word = '.' + word
        flag ^= 1
    
    #word += '.'

    n = dots // 2
    word = '.' * n + word + '.' * n

    print(word)
