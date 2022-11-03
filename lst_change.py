def change_numb(lst):
    print(lst)
    (lst[-1],lst[0])=(lst[0],lst[-1])
    return lst


print (change_numb([1,2,4,8,15]))
        