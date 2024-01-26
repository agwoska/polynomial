

class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"
    
    def evaluate(self, n):
        return n

class Int:
    def __init__(self, i):
        self.i = i
    
    def __repr__(self):
        return str(self.i)
    
    def evaluate(self, n):
        return self.i

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)
    
    def evaluate(self, n):
        return self.p1.evaluate(n) + self.p2.evaluate(n)

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        if isinstance(self.p1, Add):
            if isinstance(self.p2, Add):
                 return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, Add):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        return repr(self.p1) + " * " + repr(self.p2)
    
    def evaluate(self, n):
        return self.p1.evaluate(n) * self.p2.evaluate(n)

class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p1, Int):
            if isinstance(self.p2, Int):
                return repr(self.p1) + " / " + repr(self.p2)
            return repr(self.p1) + " / ( " + repr(self.p2) + " )"
        if isinstance(self.p2, Int):
            return "( " + repr(self.p1) + " ) / " + repr(self.p2)
        return "( " + repr(self.p1) + " ) / ( " + repr(self.p2) + " )"
    
    def evaluate(self, n):
        return self.p1.evaluate(n) / self.p2.evaluate(n)

class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p2, Int):
            return repr(self.p1) + " - " + repr(self.p2)
        return repr(self.p1) + " - ( " + repr(self.p2) + " )"

    def evaluate(self, n):
        return self.p1.evaluate(n) - self.p2.evaluate(n)

# 4 + 3 + X + ( X * X + 1 )
poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print("poly(X): ", poly)
print("poly(-1): ", poly.evaluate(-1)) # 4 + 3 + (-1) + ((-1) * (-1) + 1) = 4 + 3 - 1 + 2 = 8

## Additional examples
# x^2 + 2x - 1
poly1 = Sub( Add( Mul( X(), X()), Mul( Int(2), X())), Int(1))
print("poly1(X): ", poly1)
print("poly1(2): ", poly1.evaluate(2)) # 2*2 + 2*2 - 1 = 16 + 4 - 1 = 7

# (x^3) / 2 + 3x^2 + 2x - 1
poly2 = Add( Add( Div( Mul( X(), Mul( X(), X())), Int(2)), Mul( Int(3), Mul( X(), X()))), Sub( Mul( Int(2), X()), Int(1)))
print("poly2(X): ", poly2)
print("poly2(2): ", poly2.evaluate(2)) # (8/2) + 3*4 + 4 - 1 = 4 + 12 + 4 - 1 = 19

# (x^2 + 2x - 1) * (x^3 / 2 + 3x^2 - 2x + 1)
poly3 = Mul(poly1, poly2)
print("poly3(X): ", poly3)
print("poly3(2): ", poly3.evaluate(2)) # 7 * 19 = 133

# 300 - ((x^2 + 2x - 1) * (x^3 / 2 + 3x^2 - 2x + 1) + 42/(3*2))
poly4 = Sub( Int(300), Add( poly3, Div( Int(42), Mul( Int(3), Int(2) ) ) ) )
print("poly4(X): ", poly4)
print("poly4(2): ", poly4.evaluate(2)) # 300 - (133 + 7) = 300 - 140 = 160

# X - 2
poly5 = Sub( X(), Int(2) )
print("poly5(X): ", poly5)
print("poly5(2): ", poly5.evaluate(2)) # 2 - 2 = 0

# -1
poly6 = Int(-1)
print("poly6(X): ", poly6)
print("poly6(42): ", poly6.evaluate(42)) # -1