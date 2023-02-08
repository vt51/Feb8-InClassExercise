from generate_point_on_line import * 

def determine_collinearity(p1, p2, p3):
	expected_y = point_on_line(p1, p2, p3[0])
	if expected_y == p3[1]:
		return True
	else:
		return False

if __name__ == '__main__':
	print(determine_collinearity((-3,-1), (-1,0), (1,9)))