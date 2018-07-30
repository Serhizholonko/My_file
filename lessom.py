def hello(name, title=''):
    #name = "Peter"
    print("Hello %s %s!" % (title, name))

n = "Peter" 
hello(n, "Sir")
hello(name= "John", title="Mr.")
hello("world")
hello()
