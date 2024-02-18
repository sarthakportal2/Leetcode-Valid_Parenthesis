class Solution:
    def isValid(self, s: str) -> bool:
        #new_approach(97/97 testcases passed)* min. runtime and memory compile (27 ms,16.61 mb)*
        st = []#stack list initalize
        for c in s:#iterating each character value in stack
            if c == '(':st.append(')')#appending '(' in stack  to ')'
            elif c == '{':st.append('}')#appending '{' in stack  to '}'
            elif c == '[':st.append(']')#appending '[' in stack  to ']'
            elif not st or st.pop() != c:return False#printing false to different char val is determined
        return not st#printing true  val to same deterministic char

        #old_approach(62/97 Testcases Passed)
        #mp={")":"(","[":"]","}":"{"}#set declaration for every character val
        #st=[]#stack initalize 

        #for p in s:#iterating every stack in string 
         #   if p in mp:#checking matched character pair type
          #      if not st or mp[p]!=st[-1]:return False#printing false for the non matched string  type 
           #     elif st or mp[p]!=st[-1]:return True   #printing true to determistic matched char combination
            #    else:st.pop()#poping out the topmost element from  fully filled stack
           # else:st.append(p)#appending the character to stack at last of it 
       # return st==[]#printing vacant stack
