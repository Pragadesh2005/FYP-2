from phoneme_error_counter import count_phoneme_errors
from scli_calculator import calculate_scli
from difficulty_level_classifier import classify_difficulty

expected_text = "The rabbit ran through the road"


simulated_cases = [
    # Existing cases
    ("The wabbit wan through the woad", 3.0, 1),
    ("The wabbit wabbit ran through", 3.8, 2),
    ("The ra ra rabbit ran th through the road", 4.5, 3),

    # Additional simulated cases
    ("The rabbit ran through the road", 2.0, 0),
    ("The wabbit ran through the woad", 2.8, 0),
    ("The rabbit wan through the road", 3.1, 1),
    ("The rabbit ran fwough the road", 3.2, 1),
    ("The rabbit ran through the woad road", 3.5, 2),
    ("The wa wa rabbit ran through the road", 3.9, 2),
    ("The rabbit rabbit ran through the road", 3.6, 2),
    ("The ra rabbit ran through the road", 3.4, 1),
    ("The rabbit wan wan through the woad", 4.0, 2),
    ("The wabbit wan fwough the woad", 4.2, 2),
    ("The ra ra wabbit ran th th through the road", 4.6, 3),
    ("The rabbit ran through", 3.7, 1),
    ("The wa wabbit wan through the woad road", 4.8, 3),
    ("The rabbit ran ran through the the road", 4.4, 3),
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
