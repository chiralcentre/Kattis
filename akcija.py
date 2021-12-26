'''
def promo(books):
    sort_books = sorted(books,reverse = True)
    minimal_price = 0
    while sort_books:
        if len(sort_books) >= 3:
            minimal_price += sum(sort_books[0:2])
            sort_books = sort_books[3:]
        else:
            minimal_price += sum(sort_books)
            sort_books = []
    return minimal_price
'''
# list slicing will affect runtime
def promo(books):
    sort_books = sorted(books,reverse = True)
    minimal_price = 0
    for i in range(len(sort_books)):
        if (i+1)%3:
            minimal_price += sort_books[i]
    return minimal_price

num = int(input())
prices = [int(input()) for n in range(num)]
print(promo(prices))
