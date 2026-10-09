
list = [("a", 1), ("b", 2)]


print(list[[tag == "a" for tag, weight in list].index(True)])