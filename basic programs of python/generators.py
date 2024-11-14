
def generator_func():
  for i in range(5):
    yield i


y=generator_func()

print(next(y))
print(next(y))    # it will give only one iteration at a time and you need to call next for each itr
print(next(y))
print(next(y))
print(next(y))

