import pytest

from morse_decoder import MorseDecoder


@pytest.fixture
def decoder():
    decoder = MorseDecoder()
    yield decoder


def test_decode_valid(decoder):
    for seq_list in decoder._seq_all:
        for seq in seq_list:
            assert decoder.decode(seq.seq) == seq.output


def test_decode_invalid(decoder):
    expected = MorseDecoder.OUTPUT_INVALID
    input_invalid = ['a', 'b', 12, 'c', 4.5]
    actual = decoder.decode(input_invalid)
    assert actual == expected
