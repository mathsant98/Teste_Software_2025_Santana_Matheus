# tmp.py

def test_good():
    for i in range(1000):
        print(i)

def test_bad():
    print('this should fail!')
    assert False
