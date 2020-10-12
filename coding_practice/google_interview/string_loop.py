"""
Google interview question

We are trying to construct string A from string B. The rules are, we can only move left to right in string B, when
reaching the end of string B, we move back to the beginning. At any point, we are allowed to append the character we
are pointing to to our string under construction, but we are only allowed to append the character once. We want to know
the minimum number of times we need to iterate through string B in order to construct string A.

For example, if string A is "DACA" and string B is "ABCD", then:
1. In the first iteration through string B, we append "D"
2. In the second iteration through string B append "A" and then "C"
3. In the third iteration through string B, we append "A" to complete string A

So the answer is three.
"""