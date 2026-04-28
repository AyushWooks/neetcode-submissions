class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in s:
            if i in "([{":
                st.append(i)
            else:
                if not st:
                    return False
                top = st.pop()
                if (top == '(' and i != ')') or (top == '{' and i != '}') or (top == '[' and i != ']'):
                    return False
        return len(st) == 0