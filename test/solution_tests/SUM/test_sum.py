from lib.solutions.SUM import sum_solution
import pytest


class TestSum():
    @pytest.mark.parametrize("int_1, int_2, expected_result", [
  (2, 3, 5),
  (99, 98, 197),
  (1, 1, 2)
])
    def test_sum(self, int_1, int_2, expected_result):
        assert sum_solution.compute(int_1, int_2) == expected_result


