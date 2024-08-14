def test_function():
    def inner_function():
        print("I am in the scope of the test_function.")
    inner_function()

test_function()

# inner_function() - не работает, так как она не глобальная