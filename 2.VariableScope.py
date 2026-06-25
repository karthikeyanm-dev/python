# L -> E -> G -> B
# L -> Local ; E -> Enclosing; G -> Global; B -> Build-in

# Local Variable a variable which declared inside the function

def sayHello():
    a = "hello" # a -> is accessible in this region only

# print(a) -> a is not accessible in this scope

#  Enclosing
def function1():
    name = "Gopal"

    def function2():
        print("Hello ", name)
    function2()
function1()

# Global Variable

a = 10

def function3():
    print("Printing from function3 ", a)
    def function4():
        print("Printing from function4 ", a)
    function4()


def function5():
    print("Printing from function5 ", a)
    function3()

function5()

# Build-in variables
print(__file__)

# Use case  using swiggy

delivery_partner = "swiggy"

def hotel():
    item = "pizza"

    def orderNow():
        quantity = 2
        print(f"Ordering {quantity} numbers of {item} from {delivery_partner}")
    orderNow()

hotel()

