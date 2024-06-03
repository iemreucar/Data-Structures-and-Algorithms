from queue_1 import stack
# geeks for geeks the celebrity problem soru cikabilir interviewlarda.

query="{[3232{123sad[asdb]}]}"
query1="/(&)%=54[]]]"

def checkparenthesis(query:str):
    st=stack()
    for letter in query:
        if letter == "(" or letter=="[" or letter=="{":
            st.push(letter)
        elif letter == ")":
            if not st.pop()=="(":
                return False
        elif letter == "]":
            if not st.pop()=="[":
                return False
        elif letter == "}":
            if not st.pop()=="{":
                return False
    if  not st.isEmpty():
        print("hata var")
        return False
    return True

print(checkparenthesis(query))