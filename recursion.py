def recursion(k):
    if(k>0):
        res=k+recursion(k-1)
        print(res)
    else:
        res=0
    return res
print("\n\nRecursion examples")
recursion(6)
#You enter the next recursion depth as tri_recursion(5) which because 5 > 0 calls 5 + tri_recursion(5 -1)

#Brings us to the next depth level as tri_recursion(4) -> 4 + tri_recursion(4-1)

#Next level: 3 + tri_recursion(3 - 1) -> 3 + tri_recursion(2)

#Next: 2 + tri_recursion(2 - 1) -> tri_recursion(1)

#Next: 1 + tri_recursion(1 - 1) -> tri_recursion(0)

#For tri_recursion(0)´ the conditionk > 0is no longer satisfied and thus theelsebranch is executed which executesreturn(0)`

#With this return we move one level back in the recursion to result = 1 + tri_recursion(1 - 1) -> we have the return value from the tri_recursion(1 - 1) call, which is 0 -> so it becomes result = 1 + 0 -> result = 1

#The next executed line in the code is print(result) -> which prints the 1

#The else´ branch is skipped and the next executed line isreturn resultwhich brings us one level back up to2 + tri_recursion(2 - 1)- the return value from before is1, so it becomes2 + 1->3` which is what is printed.

#And this goes on until you are back out of all levels. That is what recursion is.
