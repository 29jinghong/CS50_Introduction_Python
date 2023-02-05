def test(num, output):
    try:
        assert(num == output)
        print("True")
    except AssertionError:
        print("False")

test(2,3)
test(2,2)