import day_14.puzzle_02.solution as s

PROVIDED_TEST_INPUT_ONE = ["498,4 -> 498,6 -> 496,6", "503,4 -> 502,4 -> 502,9 -> 494,9"]


def test_basic_happy_path():
    assert s.process_list(PROVIDED_TEST_INPUT_ONE, 1000) == 93


def test_parse_rock_formation():
    assert s.parse_rock_formation(PROVIDED_TEST_INPUT_ONE[0]) == ["498,4", "498,6", "496,6"]
    assert s.parse_rock_formation(PROVIDED_TEST_INPUT_ONE[1]) == ["503,4", "502,4", "502,9", "494,9"]


def test_get_line_points():
    cave_map = [["."] * 5 for _ in range(5)]
    print(cave_map)
    s.draw_line_between_points("2,4", "2,2", cave_map)
    assert cave_map == [
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."],
        [".", ".", "#", ".", "."],
        [".", ".", "#", ".", "."],
        [".", ".", "#", ".", "."],
    ]

if __name__ == "__main__":
    test_basic_happy_path()
