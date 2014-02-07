
LETTERS = {l:l for l in 'abcdefghijklmnopqrstuvwxyz'}
DIGITS = {d:'#' for d in '0123456789'}
PUNCT_MARKS = {p:p for p in ' ,.;:?!()-\'"'}
CHAR_MAP = dict(LETTERS.items() + DIGITS.items() + PUNCT_MARKS.items())
del LETTERS, DIGITS, PUNCT_MARKS

VALID_CHARS = ''.join(sorted(set(CHAR_MAP.values() + ['@'])))
NUM_VALID_CHARS = len(VALID_CHARS)
AT_INDEX = VALID_CHARS.index('@')

# char2index uses CHAR_MAP to map any input char into the typewriter chars
# (if a char is not found in CHAR_MAP it is mapped to @).
char2index = lambda c: CHAR_MAP.get(c.lower(), AT_INDEX)

# index2char assigns consecutive integers to every typewriter char (ASCII order).
index2char = lambda i: VALID_CHARS[i]


def compute_freq_tab(order, *corpus_files):
    pass


def write_freq_tab(order, freq_tab, output_file):
    pass


def read_freq_tab(input_file):
    pass


def most_probable_digraph(freq_tab, initial_char):
    pass


def simulate(order, freq_tab, resolution, num_chars, output_file):
    pass


def relative_word_yield(sim_file, corpus_file):
    pass


def create_profile(order, freq_tab, profile_len):
    pass


def profile_dissimilarity(profile1, profile2):
    pass
