def show_args(*args):
    for value in args:
        print(value)

def show_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

show_args(1, 2, 3)
show_kwargs(name="Saveliy", age=18)
