import random
from collections import Counter

sock_types = ['ankle', 'crew', 'calf', 'thigh']
sock_colors = ['black', 'white', 'blue']

if __name__ == '__main__':
	socks = []
	for i in range(100):
		socks.append((random.choice(sock_types), random.choice(sock_colors)))

	socks = Counter(socks)
	loners = filter(lambda x: socks[x]%2, socks)
	for sock in socks:
		print(str(sock) +': '+ str(socks[sock]))
	print('Loners: ')
	print(loners)	

