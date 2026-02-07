from phoneme_error_counter import count_phoneme_errors
from scli_calculator import calculate_scli
from difficulty_level_classifier import classify_difficulty

expected_text = "The rabbit ran through the road"

simulated_cases = [
    ("The wabbit wan through the woad", 3.0, 1),
    ("The wabbit wabbit ran through", 3.8, 2),
    ("The ra ra rabbit ran th through the road", 4.5, 3)
]

for spoken_text, response_time, repetitions in simulated_cases:
    errors, _ = count_phoneme_errors(expected_text, spoken_text)
    scli = calculate_scli(
        errors,
        response_time,
        repetitions,
        len(expected_text.split())
    )
    difficulty = classify_difficulty(scli)
    print(spoken_text)
    print("SCLI:", scli, "Difficulty:", difficulty)
