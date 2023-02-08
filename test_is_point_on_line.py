import pytest

@pytest.mark.parametrize("p1, p2, p3, expected", 
[((-3,-1), (-1,0), (1,1), True),
 ((-3,-1), (-1,0), (1,8), False),
 ((2,4), (4,6), (6,8), True),
 ((2,4), (4,6), (6,1), False),
 ((2,3), (4,0), (6,-3), True),
 ((2,3), (4,0), (6,-9), False)
 ])
def test_determine_collinearity(p1, p2, p3, expected):
	from is_point_on_line import determine_collinearity
	answer = determine_collinearity(p1, p2, p3)
	assert answer == expected