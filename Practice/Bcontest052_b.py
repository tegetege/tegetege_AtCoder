N = int(input())
S = list(input())
x = 0
x_list = [0]
for i in range(N):
	if S[i] == 'I':
		x+=1
	else:
		x-=1
	x_list.append(x)

print(max(x_list))