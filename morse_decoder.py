from enum import Enum
from typing import Sequence

class MorseEvent(Enum):
    DOT = 1
    DASH = 2

class MorseSequence:
    def __init__(self, seq: Sequence[MorseEvent], output: str):
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

    def __init__(self):
        e = MorseSequence([MorseEvent.DOT], 'e')
        t = MorseSequence([MorseEvent.DASH], 't')
        seq_len_1 = [e, t]

        i = MorseSequence([MorseEvent.DOT, MorseEvent.DOT], 'i')
        a = MorseSequence([MorseEvent.DOT, MorseEvent.DASH], 'a')
        n = MorseSequence([MorseEvent.DASH, MorseEvent.DOT], 'n')
        m = MorseSequence([MorseEvent.DASH, MorseEvent.DASH], 'm')
        seq_len_2 = [i, a, n, m]
        
        s = MorseSequence([MorseEvent.DOT, MorseEvent.DOT, MorseEvent.DOT], 's')
        u = MorseSequence([MorseEvent.DOT, MorseEvent.DOT, MorseEvent.DASH], 'u')
        r = MorseSequence([MorseEvent.DOT, MorseEvent.DASH, MorseEvent.DOT], 'r')
        w = MorseSequence([MorseEvent.DOT, MorseEvent.DASH, MorseEvent.DASH], 'w')
        d = MorseSequence([MorseEvent.DASH, MorseEvent.DOT, MorseEvent.DOT], 'd')
        k = MorseSequence([MorseEvent.DASH, MorseEvent.DOT, MorseEvent.DASH], 'k')
        g = MorseSequence([MorseEvent.DASH, MorseEvent.DASH, MorseEvent.DOT], 'g')
        o = MorseSequence([MorseEvent.DASH, MorseEvent.DASH, MorseEvent.DASH], 'o')
        seq_len_3 = [s, u, r, w, d, k, g, o]
        
        h = MorseSequence([MorseEvent.DOT, MorseEvent.DOT, MorseEvent.DOT, MorseEvent.DOT], 'h')
        v = MorseSequence([MorseEvent.DOT, MorseEvent.DOT, MorseEvent.DOT, MorseEvent.DASH], 'v')
        f = MorseSequence([MorseEvent.DOT, MorseEvent.DOT, MorseEvent.DASH, MorseEvent.DOT], 'f')
        space = MorseSequence([MorseEvent.DOT, MorseEvent.DOT, MorseEvent.DASH, MorseEvent.DASH], ' ')
        l = MorseSequence([MorseEvent.DOT, MorseEvent.DASH, MorseEvent.DOT, MorseEvent.DOT], 'l')
        # unused MorseSequence([MorseEvent.DOT, MorseEvent.DASH, MorseEvent.DOT, MorseEvent.DASH], '')
        p = MorseSequence([MorseEvent.DOT, MorseEvent.DASH, MorseEvent.DASH, MorseEvent.DOT], 'p')
        j = MorseSequence([MorseEvent.DOT, MorseEvent.DASH, MorseEvent.DASH, MorseEvent.DASH], 'j')
        b = MorseSequence([MorseEvent.DASH, MorseEvent.DOT, MorseEvent.DOT, MorseEvent.DOT], 'b')
        x = MorseSequence([MorseEvent.DASH, MorseEvent.DOT, MorseEvent.DOT, MorseEvent.DASH], 'x')
        c = MorseSequence([MorseEvent.DASH, MorseEvent.DOT, MorseEvent.DASH, MorseEvent.DOT], 'c')
        y = MorseSequence([MorseEvent.DASH, MorseEvent.DOT, MorseEvent.DASH, MorseEvent.DASH], 'y')
        z = MorseSequence([MorseEvent.DASH, MorseEvent.DASH, MorseEvent.DOT, MorseEvent.DOT], 'z')
        # unused MorseSequence([MorseEvent.DASH, MorseEvent.DASH, MorseEvent.DASH, MorseEvent.DOT], '')
        back = MorseSequence([MorseEvent.DASH, MorseEvent.DASH, MorseEvent.DASH, MorseEvent.DASH], '\b')
        seq_len_4 = [h, v, f, space, l, p, j, b, x, c, y, z, back]

        digit_0 = MorseSequence([MorseEvent.DASH, MorseEvent.DASH, MorseEvent.DASH, MorseEvent.DASH, MorseEvent.DASH], '0')
        digit_1 = MorseSequence([MorseEvent.DOT, MorseEvent.DASH, MorseEvent.DASH, MorseEvent.DASH, MorseEvent.DASH], '1')
        digit_2 = MorseSequence([MorseEvent.DOT, MorseEvent.DOT, MorseEvent.DASH, MorseEvent.DASH, MorseEvent.DASH], '2')
        digit_3 = MorseSequence([MorseEvent.DOT, MorseEvent.DOT, MorseEvent.DOT, MorseEvent.DASH, MorseEvent.DASH], '3')
        digit_4 = MorseSequence([MorseEvent.DOT, MorseEvent.DOT, MorseEvent.DOT, MorseEvent.DOT, MorseEvent.DASH], '4')
        digit_5 = MorseSequence([MorseEvent.DOT, MorseEvent.DOT, MorseEvent.DOT, MorseEvent.DOT, MorseEvent.DOT], '5')
        digit_6 = MorseSequence([MorseEvent.DASH, MorseEvent.DOT, MorseEvent.DOT, MorseEvent.DOT, MorseEvent.DOT], '6')
        digit_7 = MorseSequence([MorseEvent.DASH, MorseEvent.DASH, MorseEvent.DOT, MorseEvent.DOT, MorseEvent.DOT], '7')
        digit_8 = MorseSequence([MorseEvent.DASH, MorseEvent.DASH, MorseEvent.DASH, MorseEvent.DOT, MorseEvent.DOT], '8')
        digit_9 = MorseSequence([MorseEvent.DASH, MorseEvent.DASH, MorseEvent.DASH, MorseEvent.DASH, MorseEvent.DOT], '9')
        seq_len_5 = [digit_0, digit_1, digit_2, digit_3, digit_4, digit_5, digit_6, digit_7, digit_8, digit_9]

        self._seq_all = [seq_len_1, seq_len_2, seq_len_3, seq_len_4, seq_len_5]

    def decode(self, seq: Sequence[MorseEvent]) -> str:
        out = MorseDecoder.OUTPUT_INVALID
        seq = seq[:MorseDecoder.LEN_MAX]
        for cand in self._seq_all[len(seq) - 1]:
            if cand.seq == seq:
                out = cand.output
                break
        return out



    