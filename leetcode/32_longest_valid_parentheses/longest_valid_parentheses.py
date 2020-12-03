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
        
        open_paren_count = 0
        most_parens = 0
        current_matched_paren_count = 0

        for i in range(0,len(s)):
            cur_char = s[i]
            
            # open paren always add to open_paren_count
            if cur_char == "(":
                open_paren_count += 1
            
            else:
                if open_paren_count > 0:

                    #closed paren matches open paren
                    # decrement open_parent_count
                    #current_matched_paren_count +=2
                    # update most_parens
                    open_paren_count -= 1
                    current_matched_paren_count += 2

                    if current_matched_paren_count > most_parens:
                        most_parens = current_matched_paren_count

                else:
                    # closed paren doesn't match (no open parens)
                    #reset current_matched_paren_count
                    current_matched_paren_count = 0
        
        return most_parens
