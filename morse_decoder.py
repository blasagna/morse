from enum import Enum
from typing import Sequence


class MorseEvent(Enum):
    DOT = 1
    DASH = 2
    INVALID = 3


Dot = MorseEvent.DOT
Dash = MorseEvent.DASH


class MorseSequence:
    def __init__(self, seq: Sequence[MorseEvent], output: str) -> None:
        self._output = output
        self._seq = seq

    @property
    def output(self):
        return self._output

    @property
    def seq(self):
        return self._seq


class MorseDecoder:
    LEN_MAX = 5
    OUTPUT_INVALID = '\0'

    def __init__(self) -> None:
        e = MorseSequence([Dot], 'e')
        t = MorseSequence([Dash], 't')
        seq_len_1 = [e, t]

        i = MorseSequence([Dot, Dot], 'i')
        a = MorseSequence([Dot, Dash], 'a')
        n = MorseSequence([Dash, Dot], 'n')
        m = MorseSequence([Dash, Dash], 'm')
        seq_len_2 = [i, a, n, m]

        s = MorseSequence([Dot, Dot, Dot], 's')
        u = MorseSequence([Dot, Dot, Dash], 'u')
        r = MorseSequence([Dot, Dash, Dot], 'r')
        w = MorseSequence([Dot, Dash, Dash], 'w')
        d = MorseSequence([Dash, Dot, Dot], 'd')
        k = MorseSequence([Dash, Dot, Dash], 'k')
        g = MorseSequence([Dash, Dash, Dot], 'g')
        o = MorseSequence([Dash, Dash, Dash], 'o')
        seq_len_3 = [s, u, r, w, d, k, g, o]

        h = MorseSequence([Dot, Dot, Dot, Dot], 'h')
        v = MorseSequence([Dot, Dot, Dot, Dash], 'v')
        f = MorseSequence([Dot, Dot, Dash, Dot], 'f')
        space = MorseSequence([Dot, Dot, Dash, Dash], ' ')
        l = MorseSequence([Dot, Dash, Dot, Dot], 'l')
        '''unused = MorseSequence([Dot, Dash, Dot, Dash], '')'''
        p = MorseSequence([Dot, Dash, Dash, Dot], 'p')
        j = MorseSequence([Dot, Dash, Dash, Dash], 'j')
        b = MorseSequence([Dash, Dot, Dot, Dot], 'b')
        x = MorseSequence([Dash, Dot, Dot, Dash], 'x')
        c = MorseSequence([Dash, Dot, Dash, Dot], 'c')
        y = MorseSequence([Dash, Dot, Dash, Dash], 'y')
        z = MorseSequence([Dash, Dash, Dot, Dot], 'z')
        '''unused = MorseSequence([Dash, Dash, Dash, Dot], '')'''
        back = MorseSequence([Dash, Dash, Dash, Dash], '\b')
        seq_len_4 = [h, v, f, space, l, p, j, b, x, c, y, z, back]

        digit_0 = MorseSequence([Dash, Dash, Dash, Dash, Dash], '0')
        digit_1 = MorseSequence([Dot, Dash, Dash, Dash, Dash], '1')
        digit_2 = MorseSequence([Dot, Dot, Dash, Dash, Dash], '2')
        digit_3 = MorseSequence([Dot, Dot, Dot, Dash, Dash], '3')
        digit_4 = MorseSequence([Dot, Dot, Dot, Dot, Dash], '4')
        digit_5 = MorseSequence([Dot, Dot, Dot, Dot, Dot], '5')
        digit_6 = MorseSequence([Dash, Dot, Dot, Dot, Dot], '6')
        digit_7 = MorseSequence([Dash, Dash, Dot, Dot, Dot], '7')
        digit_8 = MorseSequence([Dash, Dash, Dash, Dot, Dot], '8')
        digit_9 = MorseSequence([Dash, Dash, Dash, Dash, Dot], '9')
        seq_len_5 = [
            digit_0, digit_1, digit_2, digit_3, digit_4, digit_5, digit_6,
            digit_7, digit_8, digit_9
        ]

        self._seq_all = [seq_len_1, seq_len_2, seq_len_3, seq_len_4, seq_len_5]

    def decode(self, seq: Sequence[MorseEvent]) -> str:
        out = MorseDecoder.OUTPUT_INVALID
        seq = seq[:MorseDecoder.LEN_MAX]
        for cand in self._seq_all[len(seq) - 1]:
            if cand.seq == seq:
                out = cand.output
                break
        return out
