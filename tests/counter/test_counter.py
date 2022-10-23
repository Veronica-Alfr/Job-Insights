from src.counter import count_ocurrences


def test_counter():
    path = "src/jobs.csv"
    assert count_ocurrences(path, "Javascript") == 122
    assert count_ocurrences(path, "Python") == 1639
