def point_on_line(p1, p2, x):
	m = calculate_slope(p1, p2)
	b = calculate_y_intercept(p1, m)
	y = (m*x) + b
	return y

def calculate_slope(p1, p2):
	m = (p2[1]-p1[1]) / (p2[0]-p1[0])
	return m

def calculate_y_intercept(p1, m):
	b = p1[1] - (m*p1[0]) # b = y - mx
	return b

if __name__ == '__main__':
	print(point_on_line((1,1), (7,5), 4))
