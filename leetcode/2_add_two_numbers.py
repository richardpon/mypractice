class SubString:
    def __init__(self):
        self.length = 0
        self.map = {}
        self.done = False

    def add_char_to_substr(self, char):

        # already done
        if self.done:
            return

        # dupe char
        elif char in self.map:
            self.done = True
        
        # new char
        else:
            self.length += 1
            self.map[char] = True

    def __repr__(self):
        s = "===\n"
        s += "length={}".format(self.length) + "\n"
        s += "map={}".format(self.map) + "\n"
        s += "done={}".format(self.done) + "\n"
        s += "---\n"
        return s


class SlowSolution:
    def __init__(self):
        self.done_substrings = []
        self.building_substrings = []
        self.longest_substring = None

    def add_char(self, char):
        self.building_substrings.append(SubString())

        index_to_move = None
        for i,l in enumerate(self.building_substrings):
            l.add_char_to_substr(char)
            
            # substring is done, move to done
            if l.done:
                index_to_move = i

            # found new longest substring
            if self.longest_substring is None or l.length > self.longest_substring.length:
                self.longest_substring = l

        if index_to_move is not None:
            self.done_substrings.append(self.building_substrings[index_to_move])
            self.building_substrings.pop(index_to_move)

    def lengthOfLongestSubstring(self, s):
        for char in s:
            self.add_char(char)

        if self.longest_substring is None:
            return 0
        else:
            return self.longest_substring.length

    def __repr__(self):
        s = "done===\n" 
        for done in self.done_substrings:
            s += repr(done) + "\n"

        s += "progress===\n"
        for subbstr in self.building_substrings:
            s += repr(subbstr)  + "\n"

        s += "longest="
        s += repr(self.longest_substring)  + "\n"

        return s

        
        



class Solution:
    def __init__(self):
        self.cur_string = []
        self.max_sub_string = 0
        self.char_map = {}

    def add_char(self, char):
        # remove any existance of char (and other leading characters)
        if char in self.char_map:
            index_to_remove_up_to = self.cur_string.index(char)

            self.remove_first_n_chars(index_to_remove_up_to + 1)
            # remove chars from beginning of self.cur_string until and including char

        # add char back in
        self.cur_string.append(char)
        self.char_map[char] = True

        # update max len if needed
        if len(self.char_map) > self.max_sub_string:
            self.max_sub_string = len(self.char_map)


    # todo: Consider making this a pure function and not modify internal state
    def remove_first_n_chars(self, num):
        for i in range(0, num):
            # always pop head. (don't modify list while iterating)
            cur_char = self.cur_string.pop(0)
            del self.char_map[cur_char]

    def lengthOfLongestSubstring(self, s):
        for char in s:
            self.add_char(char)
        return self.max_sub_string


str = "abcabcbb"
s = Solution()
len = s.lengthOfLongestSubstring(str)
print(len)