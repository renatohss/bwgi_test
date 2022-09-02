import pytest

from last_line import last_line


class TestLastLines:

    def test_should_print_lines_in_reversed_order(self):
        txt_list = ["'Line 1\\n'", "'Line 2\\n'", "'Line 3\\n'"]
        idx = -1
        for line in last_line("tests/test_txt.txt"):
            assert line == txt_list[idx]
            idx -= 1

    def test_should_raise_exception_on_empty_file(self):
        with pytest.raises(Exception):
            for _ in last_line("tests/empty_txt.txt"):
                pass
