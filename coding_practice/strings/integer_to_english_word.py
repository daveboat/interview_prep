"""
LC273 - Integer to English Words

Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"

Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
"""


class Solution(object):
    def __init__(self):
        self.ones = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six',
                     'Seven', 'Eight', 'Nine']
        self.teens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']

        self.tens = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

        self.orders_of_magnitude = ['', ' Thousand', ' Million', ' Billion', ' Trillion']

    def two_num_to_words(self, num):
        # return the correct english words for a num with two or less digits
        if num < 10:
            return self.ones[num]
        elif num < 20:
            return self.teens[num - 10]
        else:
            if num % 10 == 0:
                return self.tens[num // 10]
            else:
                return self.tens[num // 10] + ' ' + self.ones[num % 10]

    def three_num_to_words(self, num):
        # return the correct english words for a num with three or less digits
        if num < 100:
            return self.two_num_to_words(num)
        else:
            if num % 100 == 0:
                return self.ones[num // 100] + ' Hundred'
            else:
                return self.ones[num // 100] + ' Hundred ' + self.two_num_to_words(num % 100)

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """

        # the zero case isn't covered by the other stuff because of how english numbers work, so make a special
        # provision for it here
        if num == 0:
            return 'Zero'
        else:
            # add numbers in three at a time with the appropriate order of magnitude appended
            num_list = []
            magnitude_index = 0
            while num:
                if num % 1000 != 0:
                    num_list.append(self.three_num_to_words(num % 1000) + self.orders_of_magnitude[magnitude_index])
                magnitude_index += 1
                num = num // 1000

        return ' '.join(num_list[::-1])


if __name__ == '__main__':
    S = Solution()
    print(S.numberToWords(17))
    print(S.numberToWords(12345))
    print(S.three_num_to_words(100))
    print(S.numberToWords(1000))
