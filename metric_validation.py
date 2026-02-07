from phoneme_error_counter import count_phoneme_errors
from scli_calculator import calculate_scli

expected_text = "The cat is on the mat"

test_cases = [
    ("The cat is on the mat", 1.2, 0),
    ("The ca is on the mat", 1.8, 1),
    ("The ca ca is on mat", 2.6, 2),
    ("The th ca is on the ma", 3.4, 3)
]

for spoken_text, response_time, repetitions in test_cases:
    errors, _ = count_phoneme_errors(expected_text, spoken_text)
    scli = calculate_scli(
        phoneme_errors=errors,
        response_time=response_time,
        repetitions=repetitions,
        sentence_length=len(expected_text.split())
    )
    print(spoken_text, "-> SCLI:", scli)
