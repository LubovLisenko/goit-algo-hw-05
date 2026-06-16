def caching_fibonacci():
     #Створити  порожній словник cache
    dict_cache = {}
    def fibonacci(n):
        if n <= 0:
         return 0
        if n == 1:
            return 1
        if n in dict_cache:
            return dict_cache[n]

        dict_cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return dict_cache[n]

    return fibonacci
#КІНЕЦЬ ФУНКЦІЇ caching_fibonacci

fib = caching_fibonacci()
print(fib(10))
print(fib(15))
