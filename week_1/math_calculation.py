from queue_1 import stack
"(3+5*7)-4"
exp="357*+4-"
"-+*5734"

def postfixcalc(expression:str):
    st=stack()
    for letter in expression:
        if not letter in ["+","-","*","/"]:
            st.push(letter)
        else:
            op2=int(st.pop())
            op1=int(st.pop())
            if letter =="+":
                st.push(str(op1+op2))
            elif letter =="-":
                st.push(str(op1-op2))
            elif letter =="*":
                st.push(str(op1*op2))
            elif letter =="/":
                st.push(str(op1/op2))
    return st.pop()
res= postfixcalc(exp)
print(res)
