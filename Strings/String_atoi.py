class Solution:
    def myAtoi(self, s: str) -> int:
        maxl = pow(2, 31) - 1
        minl = -pow(2, 31)
        s = s.strip(" ")
        # s=s.lstrip(".")
        n = len(s)
        if (n == 0):
            return 0
        pos = True
        st = 0
        if (s[0] == '-'):
            pos = False
            st = 1
        elif (s[0] == '+'):
            pos = True
            st = 1
        i = st
        out = ""
        found = False
        while (i < n):
            if ((s[i] >= '0' and s[i] <= '9')):
                j = i
                found = True
                while (j < n and ((s[j] >= '0' and s[j] <= '9'))):
                    out += s[j]
                    j += 1
                i = j

            else:
                break
            if (found == True):
                break
        if (len(out) == 0):
            return 0
        # return 3
        out = int(out)
        if (pos == False):
            out = -(out)
        if (out > maxl):
            out = maxl
        elif (out < minl):
            out = minl
        return out
