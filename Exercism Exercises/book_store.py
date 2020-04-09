BOOK_PRICE = 800
DISCOUNT = {0: 1, 1: 1, 2: 0.95, 3: 0.9, 4: 0.8, 5: 0.75}


def total(books, start_price=0):
    u_books = set(books)
    n_books = len(u_books)
    n_price = BOOK_PRICE * n_books * DISCOUNT[n_books] + start_price

    num_books = len(books)

    if num_books % 8 == 0 and n_books == 5:
        n_price -= 5 * num_books

    if num_books == n_books:
        return n_price

    for b in u_books:
        books.remove(b)
    return total(books, n_price)