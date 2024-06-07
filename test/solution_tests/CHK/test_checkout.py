from lib.solutions.CHK import checkout_solution
import pytest


class TestCheckout():
    @pytest.mark.parametrize(
        "test_string, expected_result", [
            ("A, A, A, A, A, A, B, C, D", 325),
            ("A, B, B, B, C, D", 160),
            ("D, D, D, D, D", 75),
            ("", -1),
            ("a", 50),
            ("-", -1),
            ("+", -1),
            (190, -1),
            ("abcd", 115),
            ("AxA", 115),
        ]
    )
    def test_checkout(self, test_string, expected_result):
        assert checkout_solution.checkout(skus=test_string) == expected_result





