from app import say_hello

def test_say_hello():
    assert say_hello() == "Hello, World!"
    assert say_hello("Alice") == "Hello, Alice!"