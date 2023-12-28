import pandas

s_data_f = pandas.read_csv("abcd.csv")
list1 = {v.letter: v.code for (i, v) in s_data_f.iterrows()}
print(list1)


def setup():
    name = input("Enter a name: ")
    f = []

    try:
        f = [list1[i.upper()] for i in name]
    except KeyError as e:
        print("Only letters allowed!!")
        setup()
    else:
        print(f)
    finally:
        print("Enjoy the NATO lang!")

setup()
