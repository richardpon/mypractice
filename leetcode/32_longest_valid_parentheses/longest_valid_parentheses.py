from typing import List

class Solution:
    """
    Problem: Identify which parentheses in the string
    are valid?

    Valid paren: Has matching paren
    In left to right traversal:
    1) encounter open paren - Don't know if this is valid
    until traverse remainder of string
    2) encounter closed paren - immediately know if this
    matches a previous open paren

    intermediate output is a List[Boolean] indicate
    which indexes in string are valid


    """
    def longestValidParentheses(self, s: str) -> int:
        
        # Keep track of which character in s belongs to a matching paren
        # initialize to all false, as we don't know if any match or not
        matching_paren_tracker: List[bool] = []
        for i in range(0, len(s)):
            matching_paren_tracker.append(False)

        # stack of index of open paren
        open_paren_indexes: List[int] = []

        for i in range(0, len(s)):
            if s[i] == "(":
                # add open paren to stack as we don't know if it is matching yet
                open_paren_indexes.append(i)
            else:
                # see if closing paren matches top open paren of stack
                if len(open_paren_indexes) > 0:
                    # There is an open paren that will match this closing paren

                    # mark indexes of both parens as matching
                    # mark open paren as matching
                    matching_paren_tracker[open_paren_indexes[-1]] = True

                    # mark closed paren as matching
                    matching_paren_tracker[i] = True 

                    # pop open paren from stack (delete it)
                    del open_paren_indexes[-1]

                else:
                    # There is no open paren, so this closing paren is unmatched
                    matching_paren_tracker[i] = False

        # Count longest sequential matched parens
        max_longest = 0
        longest_so_far = 0
        for i in range(0, len(matching_paren_tracker)):
            if (matching_paren_tracker[i]):
                # found another matching paren
                longest_so_far += 1
                if longest_so_far > max_longest:
                    max_longest = longest_so_far
            else:
                # found an unmatched paren, reset counters
                longest_so_far = 0
        
        return max_longest
