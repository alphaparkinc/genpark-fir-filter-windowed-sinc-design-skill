"""Windowed-Sinc Linear-Phase FIR Filter Designer.
100% Python Standard Library.
"""

import math

class FIRFilterDesign:
    @staticmethod
    def design_lowpass(num_taps, cutoff_ratio):
        assert num_taps % 2 == 1, "Taps must be odd for symmetric linear phase"
        m = (num_taps - 1) // 2
        coeffs = []
        fc = cutoff_ratio / 2.0
        for i in range(num_taps):
            n = i - m
            if n == 0:
                h = 2.0 * math.pi * fc
            else:
                h = math.sin(2.0 * math.pi * fc * n) / n
            w = 0.54 - 0.46 * math.cos(2.0 * math.pi * i / (num_taps - 1))
            coeffs.append(h * w)
        total = sum(coeffs)
        return [round(c / total, 6) for c in coeffs]
