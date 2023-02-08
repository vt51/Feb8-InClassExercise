import pytest

@pytest.mark.parametrize("p1, p2, x, expected", 
[((-3,-1), (-1,0), 1, 1),
 ((2,4), (4,6), 6, 8),
 ((2,3), (4,0), 6, -3)
 ]) 
def test_point_on_line(p1, p2, x, expected):
	from generate_point_on_line import point_on_line
	answer = point_on_line(p1, p2, x)
	assert answer == expected

@pytest.mark.parametrize("p1, p2, expected", 
[((-3,-1), (-1,0), 1/2),
 ((2,4), (4,6), 1),
 ((2,3), (4,0), -3/2)
 ]) 
def test_calculate_slope(p1, p2, expected):
	from generate_point_on_line import calculate_slope
	answer = calculate_slope(p1, p2)
	assert answer == expected

@pytest.mark.parametrize("p1, m, expected", 
[((-3,-1), 1/2, 1/2),
 ((2,4), 1, 2),
 ((2,3), -3/2, 6)
 ]) 
def test_calculate_y_intercept(p1, m, expected):
	from generate_point_on_line import calculate_y_intercept
	answer = calculate_y_intercept(p1, m)
	assert answer == expected