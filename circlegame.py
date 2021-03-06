from itertools import tee, islice

def trianglenumbers(k=0):
	total = 0
	while True:
		total += k
		k += 1
		yield total
			
def circlegame(n):
	values = []
	for j in islice(trianglenumbers(), n):
		values.append(j%n)
	if len(set(values)) == n: return True
	else: return False
	
def main():
	for j in range(1000):
		if circlegame(j):
			print(j)
		
if __name__ == "__main__":
	main()
