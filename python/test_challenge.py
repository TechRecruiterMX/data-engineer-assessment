from challenge import *


def test_clean_records():
    data = [
        {
            "id":1,
            "timestamp":"2025-01-01",
            "value":100
        },
        {
            "id":2,
            "timestamp":None,
            "value":50
        }
    ]

    assert len(clean_records(data)) == 1



def test_deduplicate():

    data = [
        {
            "id":1,
            "timestamp":"2025-01-01",
            "value":100
        },
        {
            "id":1,
            "timestamp":"2025-01-02",
            "value":200
        }
    ]

    result = deduplicate_records(data)

    assert result[0]["value"] == 200



def test_batches():

    result = list(
        batched([1,2,3,4,5],2)
    )

    assert result == [
        [1,2],
        [3,4],
        [5]
    ]
