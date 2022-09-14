try:
    arr1 = ['A','B', 'C', 'D']
    print(arr1[6])
    numC = 6 / 0
except ArithmeticError as e:
    print("Arithmetic Error Exception caught", e)
except IndexError as e:
    print ("index is out of Range ", e)
except Exception as e:
    print("exception caught ", e)