def foo():
    return 5

def test_func(my_eval_string):
    res = eval(my_eval_string)
    return res

print(test_func("foo()"))