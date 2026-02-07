import time
from stt_whisper import speech_to_text
from phoneme_error_counter import count_phoneme_errors
from scli_calculator import calculate_scli
from difficulty_level_classifier import classify_difficulty

expected_text = "The cat is on the mat"
audio_path = "input.wav"

start_time = time.time()
spoken_text = speech_to_text(audio_path)
end_time = time.time()

response_time = round(end_time - start_time, 2)
repetitions = 1
sentence_length = len(expected_text.split())

errors, _ = count_phoneme_errors(expected_text, spoken_text)

scli = calculate_scli(
    phoneme_errors=errors,
    response_time=response_time,
    repetitions=repetitions,
    sentence_length=sentence_length
)

difficulty = classify_difficulty(scli)

print("Expected Text:", expected_text)
print("Spoken Text:", spoken_text)
print("Response Time:", response_time)
print("Phoneme Errors:", errors)
print("SCLI:", scli)
print("Difficulty Level:", difficulty)
