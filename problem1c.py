from monkeys import (compute_freq_tab, simulate_freq_tab, 
                     relative_word_yield)

corpus = (
    ('books/christmas_carol.txt', 168925),
    ('books/wuthering_heights.txt', 662869),
    ('books/agnes_grey.txt', 384300),
    ('books/jane_eyre.txt', 1051336),
    ('books/tarzan_of_the_apes.txt', 492783),
    ('books/king_solomons_mines.txt', 454437),
    ('books/fanny_hill.txt', 474725),
    ('books/alices_adventures_in_wonderland.txt', 148580),
    ('books/legend_of_sleepy_hollow.txt', 69164),
    ('books/the_adventures_of_sherlock_holmes.txt', 575574),
    ('books/adventures_of_huckleberry_finn.txt', 578345),
    ('books/the_prince.txt', 286854),
    ('books/war_of_the_worlds.txt', 346458),
    ('books/metamorphosis.txt', 122139),
    ('books/the_jungle_book.txt', 279771)
)

bronte_books = (
    'books/wuthering_heights.txt', 
    'books/agnes_grey.txt', 
    'books/jane_eyre.txt'
)

for order in (2, 3):
    freq_tab = compute_freq_tab(order, *bronte_books)
    for book_path, book_chars in corpus:
        simulate_freq_tab(freq_tab, 10 * book_chars, 'tmp.txt')
        word_yield = relative_word_yield('tmp.txt', book_path)
        print '%s,%s,%s' % (book_path, order, word_yield)
