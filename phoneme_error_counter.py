import pronouncing

def text_to_phonemes(text):
    phonemes = []
    words = text.lower().split()
    for word in words:
        phones = pronouncing.phones_for_word(word)
        if phones:
            phonemes.extend(phones[0].split())
    return phonemes

def count_phoneme_errors(expected_text, spoken_text):
    expected_ph = text_to_phonemes(expected_text)
    spoken_ph = text_to_phonemes(spoken_text)
    mismatches = abs(len(expected_ph) - len(spoken_ph))
    for e, s in zip(expected_ph, spoken_ph):
        if e != s:
            mismatches += 1
    return mismatches, len(expected_ph)

def get_phoneme_sequences(expected_text, spoken_text):
    expected_ph = text_to_phonemes(expected_text)
    spoken_ph = text_to_phonemes(spoken_text)
    return expected_ph, spoken_ph
