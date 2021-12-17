from example import reverse


def test_reverse():
    assert reverse('Hello') == 'olleH'


def test_reverse_empty():
    assert reverse('') == ''


def test_failed():
    assert reverse('12') == '12'
