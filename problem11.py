import time

def get_grid():
	"""
	Returns grid defined in problem statement as a list of lists
	"""
	filename = "problem11-data.txt"
	text_file = open(filename, "r")
	lines = text_file.readlines()
	text_file.close()
	L = []
	for i in range(len(lines)):
		L.append(map(int, lines[i].split()))
	return L
	
def find_max_product():
	L = get_grid()
	n = len(L)
	maxproduct = 0; P1 = 0; P2 = 0; P3 = 0; P4 = 0
	#sweep down/right from top-left corner
	for i in range(n):
		for j in range(n):
			if i <= n-4:
				P4 = L[i][j]*L[i+1][j]*L[i+2][j]*L[i+3][j] #vertical downward
				if j <= n-4:
					P3 = L[i][j]*L[i+1][j+1]*L[i+2][j+2]*L[i+3][j+3] #diagonal down/right
			if j <= n-4:
				P2 = L[i][j]*L[i][j+1]*L[i][j+2]*L[i][j+3] #horizontal to right
				if i >= 3:
					P1 = L[i][j]*L[i-1][j+1]*L[i-2][j+2]*L[i-3][j+3] #diagonal up/right
			maxproduct = max(P1,P2,P3,P4,maxproduct)
	return maxproduct	
	
if __name__ == "__main__":
	start = time.time()
	print(find_max_product())
	end = time.time()
	print(end-start)
