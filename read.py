data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('读取完成, 共', len(data), '笔资料')

s = 0
for i in data:
	s = s + len(i)
	avg = s / len(data)
print('avg=', avg)
