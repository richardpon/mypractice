class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self.generate_recursive(n, 0)
        
    def generate_recursive(self, n: int, num_open: int, indent:str="") -> List[str]:
        print(indent+f"{n=} {num_open=}")
        """
        in each iteration, add an open or closed paren (do both then combine with results

        7, (

        6  ()
           ((
        """
        if n == 0 and num_open ==0:
            return [""]

        # open
        results = set()
        if n > 0:
            results.update({"(" + suffix for suffix in self.generate_recursive(n - 1, num_open + 1,indent+"-")})
        
        # optionally close

        if num_open > 0:
            results.update({")" + suffix for suffix in self.generate_recursive(n, num_open - 1,indent+"_")})    

        return list(results)


