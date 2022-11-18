# %%
a = [1, 9, 4, 25, 16]
i = a.__iter__()
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())

# %%
f = open('../Data/camion.csv')
f.__iter__()    # Notar que esto apunta al método...
                    # ...que accede al archivo mismo.
#%%
next(f)

# %%
