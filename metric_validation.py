
from phoneme_error_counter import count_phoneme_errors
from scli_calculator import calculate_scli

expected_text = "The cat is on the mat"

test_cases = [
    # 1. Perfect sentence
    ("The cat is on the mat", 1.2, 0),

    # 2. One missing phoneme/word
    ("The ca is on the mat", 1.8, 1),

    # 3. Repeated words
    ("The ca ca is on mat", 2.6, 2),

    # 4. Multiple missing sounds
    ("The th ca is on the ma", 3.4, 3),

    # 5. Missing first word
    ("cat is on the mat", 1.5, 0),

    # 6. Missing last word
    ("The cat is on the", 1.7, 0),

    # 7. Missing middle word
    ("The cat on the mat", 2.0, 0),

    # 8. Repeated first word
    ("The The cat is on the mat", 2.1, 1),

    # 9. Repeated last word
    ("The cat is on the mat mat", 2.3, 1),

    # 10. Several repeated words
    ("The cat cat is is on the mat", 2.8, 3),

    # 11. Substituted word
    ("The bat is on the mat", 2.0, 0),

    # 12. Multiple substituted words
    ("The dog is in the bag", 3.0, 0),

    # 13. Short response
    ("The cat", 2.5, 0),

    # 14. Longer response with extra words
    ("The cat is sitting on the mat", 3.2, 1),

    # 15. Very slow response with several errors
    ("The ca is mat", 4.5, 2),
]

sentence_length = len(expected_text.split())

print("Expected sentence:", expected_text)
print("-" * 70)

for i, (spoken_text, response_time, repetitions) in enumerate(
    test_cases, start=1
):
    errors, _ = count_phoneme_errors(
        expected_text, spoken_text
    )

    scli = calculate_scli(
        phoneme_errors=errors,
        response_time=response_time,
        repetitions=repetitions,
        sentence_length=sentence_length
    )

    print(
        f"Test {i:02d} | "
        f"Spoken: {spoken_text!r} | "
        f"Time: {response_time}s | "
        f"Repetitions: {repetitions} | "
        f"Errors: {errors} | "
        f"SCLI: {scli}"
    )
