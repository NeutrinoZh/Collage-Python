def make_decorator(text, ch):
    def myDecorator(func):
        def decorator(*args):
            print(ch * (len(text) + 4))
            print(f'{ch} {text} {ch}')
            print(ch * (len(text) + 4))

            func(*args)
        
        return decorator
    return myDecorator


@make_decorator('My name is Zhenya!', '=')
def foo(text):
    print('Hello, World!', text)

foo('This is func')