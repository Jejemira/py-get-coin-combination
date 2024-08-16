from app.main import get_coin_combination

import pytest


@pytest.mark.parametrize(
    "amount_to_convert,extend_value",
    [
        pytest.param(
            0,
            [0, 0, 0, 0],
            id=""
        ),
        pytest.param(
            4,
            [4, 0, 0, 0],
            id=""
        ),
        pytest.param(
            5,
            [0, 1, 0, 0],
            id=""
        ),
        pytest.param(
            9,
            [4, 1, 0, 0],
            id=""
        ),
        pytest.param(
            10,
            [0, 0, 1, 0],
            id=""
        ),
        pytest.param(
            24,
            [4, 0, 2, 0],
            id=""
        ),
        pytest.param(
            25,
            [0, 0, 0, 1],
            id=""
        )
    ]
)
def test_coim(amount_to_convert: int, extend_value: list) -> None:
    assert get_coin_combination(amount_to_convert) == extend_value
