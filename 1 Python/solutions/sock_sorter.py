import random
from collections import Counter

sock_types = ['ankle', 'crew', 'calf', 'thigh']
socks = {}

for i in range(100):
    sock = random.choice(sock_types)
    if sock in socks.keys():
        socks[sock] += 1
    else:
        socks[sock] = 1

print(socks)
for sock, count in socks.items():
    print(sock, "has", count//2, "pairs and", count%2, "loners")
