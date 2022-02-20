from mylibrary import myfunctions


def test_haversine():
    assert myfunctions.haversine(52.370216, 4.895168, 52.520008,
    13.404954) != 945793.4375088713

def test_haversine():
    assert myfunctions.haversine(52.370216, 4.895168, 52.520008,
    13.404954) == 946.3876221719836

def test_sum():
    assert myfunctions.sum(1, 2) == 3

def test_sum():
    assert myfunctions.sum(-1, 1) == 0