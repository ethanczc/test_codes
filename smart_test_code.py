'''
converting an input decimal to binary outputs
'''

num = 12
S0 = 0
S1 = 0
S2 = 0
S3 = 0

if (num % 2) == 1:
	S0 = 1
if (num / 2) % 2 == 1:
	S1 = 1
if (num / 4 ) == 1 or (num / 4) == 3:
	S2 = 1
if (num /2) > 3:
	S3 = 1

print('{} {} {} {}'.format(S3,S2,S1,S0))
