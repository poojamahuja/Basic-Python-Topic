def out(text):
    msg = text    
    def inner():
        print(msg)
    return inner

if __name__ == '__main__':
    func = out('hello')
    func()