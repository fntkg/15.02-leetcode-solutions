ROMAN_NUMERAL_MAP = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        previous_value = 0

        for numeral in s:
            current_value = ROMAN_NUMERAL_MAP[numeral]
            # If the previous numeral is smaller, adjust the total for subtraction.
            if previous_value < current_value:
                total += current_value - 2 * previous_value
            else:
                total += current_value
            previous_value = current_value

        return total


if __name__ == "__main__":
    s = Solution()
    assert s.romanToInt("III") == 3
    assert s.romanToInt("LVIII") == 58
    assert s.romanToInt("MCMXCIV") == 1994
