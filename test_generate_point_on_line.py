import pytest

@pytest.mark.parametrize("(x1, y1), (x2, y2), x, expected", 
[((1,1), (7,5), 4, 3)
 ]) 
def test_point_on_line((x1, y1), (x2, y2), x, expected):
	from generate_point_on_line import point_on_line
	answer = point_on_line((x1, y1), (x2, y2), x)
	assert answer == expected