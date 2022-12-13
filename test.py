def rev_str(s):
   if n == 1:
      return 1
   return n + rec_sum(n-1)

print(rev_str('qwerty'))