def calculate_scli(phoneme_errors,
                   response_time,
                   repetitions,
                   sentence_length,
                   alpha=0.4,
                   beta=0.3,
                   gamma=0.2,
                   delta=0.1):
    scli = (alpha * phoneme_errors) + \
           (beta * response_time) + \
           (gamma * repetitions) + \
           (delta * sentence_length)
    return round(scli, 2)
