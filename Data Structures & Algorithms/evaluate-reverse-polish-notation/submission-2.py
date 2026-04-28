class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for ch in tokens:
            if ch not in "+-*/":
                st.append(int(ch))
            else:
                b = st.pop()
                a = st.pop()
                if ch == "+":
                    res = a + b
                elif ch =="-":
                    res = a - b
                elif ch =="*":
                    res = a * b
                elif ch =="/":
                    res = int(a / b)
                st.append(res)
        return int(st[-1])