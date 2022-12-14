import day_04.puzzle_01.solution as s

def test_contains_overlap():
    assert s.is_sub_set("1-3", "1-4") is True
    assert s.is_sub_set("2-3", "1-4") is True
    assert s.is_sub_set("1-3", "2-4") is False
    assert s.is_sub_set("1-7", "6-9") is False
    assert s.is_sub_set("6-6", "4-6") is True
    assert s.is_sub_set("2-8", "4-8") is True
    assert s.is_sub_set("14-90", "13-89") is False
    assert s.is_sub_set("7-35", "49-54") is False
