# pickle模块演示
import shelve
import pickle

# write it
print("pickling lists\n")
va = ["sweet", "hot", "dill"]
wa = ["whole", "spear", "chip"]
ya = ["I", "love", "you", "baby"]
f = open("1.bat", "wb")

pickle.dump(va, f)
pickle.dump(wa, f)
pickle.dump(ya, f)
f.close()

# read it
f = open("1.bat", "rb")

v = pickle.load(f)
w = pickle.load(f)
y = pickle.load(f)
print("first", v)
print("second", w)
print("thrid", y)
f.close()
#
# print("try\n")
# try:
#     a = int(input("please input a number\n"))
#     print("\n", a)
# except:
#     print("Error\n")
#
# input("\n\n input enter key to continue\n")
