from typing import List

class Solution:
    """
    Solves LeetCode Problem 20: Valid Parentheses
    """

    def __init__(self):
        self.open_parens = {"(": True, "{": True, "[": True}
        self.matched_parens = {"()": True, "{}": True, "[]": True}

    def isValid(self, s: str) -> bool:
        return self.isValidRecursive(s, [])

    def isValidRecursive(self, s: str, stack: List[str]) -> bool:
        """
        Recursively determines if the given string of parentheses s is valid
        given the stack of existing unmatched open parentheses

        :param s: Input string containing remaining parentheses that need to be traversed
        :param stack: Stack of unmatched open parentheses that need to be matched.
            The top of the stack needs to be matched first
        :type s: str
        :type stack: List[str]
        :returns: True if all remaining parentheses in s can be matched with stack
        :rtype: bool
        """

        if not s:
            # True when both s and stack are empty
            return len(stack) == 0
        else:
            # There exists at least one paren to process
            next_paren = s[0]

            if next_paren in self.open_parens:
                # always add open paren to stack and recurse
                return self.isValidRecursive(s[1:], stack + [next_paren])
            else:
                # closing paren must match top of stack (latested_open_paren)
                if not stack:
                    return False
                else:
                    latested_open_paren = stack[-1]
                    potential_matched_parens = latested_open_paren + next_paren
                    if (potential_matched_parens in self.matched_parens):
                        return self.isValidRecursive(s[1:], stack[0:-1])
                    else:
                        return False
