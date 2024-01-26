class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

class Int:
    def __init__(self, i):
        self.i = i
    
    def __repr__(self):
        return str(self.i)

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)

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

class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p2, Int):
            return repr(self.p1) + " - " + repr(self.p2)
        return repr(self.p1) + " - ( " + repr(self.p2) + " )"

    def evaluate(self):
        return 0

# 4 = 3 + X + ( X * X + 1 )
poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print(poly)

## Additional examples
# x^2 + 2x - 1
poly1 = Sub( Add( Mul( X(), X()), Mul( Int(2), X())), Int(1))
print(poly1)

# (x^3) / 2 + 3x^2 - 2x + 1
poly2 = Add( Add( Div( Mul( X(), Mul( X(), X())), Int(2)), Mul( Int(3), Mul( X(), X()))), Sub( Mul( Int(2), X()), Int(1)))
print(poly2)

# (x^2 + 2x - 1) * (x^3 / 2 + 3x^2 - 2x + 1)
poly3 = Mul(poly1, poly2)
print(poly3)

# 32 - ((x^2 + 2x - 1) * (x^3 / 2 + 3x^2 - 2x + 1) + 42/(3*2))
poly4 = Sub( Int(32), Add( poly3, Div( Int(42), Mul( Int(3), Int(2) ) ) ) )
print(poly4)
