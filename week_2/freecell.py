from data_st import Stack

class Card:
    def __init__(self,suit,value) -> None:
        self.value=value
        self.suit=suit
        pass




s1=Stack()
s2=Stack()


s1.push(Card(suit="C",value=8))
s1.push(Card(suit="D", value=3))
s1.push(Card(suit="S", value="K"))

c=s1.pop()

s2.push(c)
s2.push(s1.pop())

s1.push(Card(suit="H",value="A"))
s2.push(Card(suit="S",value="K"))

