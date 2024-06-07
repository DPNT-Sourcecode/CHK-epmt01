from lib.solutions.CHK import checkout_solution
import pytest


class TestCheckout():
    @pytest.mark.parametrize(
        "test_string, expected_result", [
            ("A, A, A, A, A, A, B, C, D", 355),
            ("A, B, B, B, C, D", 355),
            ("D, D, D, D, D", 355),
            ("", 0),
        ]
    )
    def test_checkout(self, test_string, expected_result):
        assert checkout_solution.checkout(skus=test_string) == expected_result

