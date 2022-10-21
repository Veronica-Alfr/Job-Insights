from src.counter import count_ocurrences


def test_counter():
    # 16.., 1..
    path = "src/jobs.csv"
    assert count_ocurrences(path, "Javascript") == 32
    assert  count_ocurrences(path, "Python") == 1570
