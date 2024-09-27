
class Oddeven:
    def odd(self,a):
        if a%2==0:
            print("Even",a)
        else:
            print("odd",a)

class Input:
       def input(self):
            a=int(input("Enter num: "))
            c=Oddeven()
            c.odd(a)

    #    def create(self):
    #         self.input()

b=Input()
b.input()




