import time
from stt_whisper import speech_to_text
from phoneme_error_counter import count_phoneme_errors
from scli_calculator import calculate_scli
from difficulty_level_classifier import classify_difficulty
from error_pattern_profiler import build_error_profile, update_cumulative_profile
from phoneme_error_counter import get_phoneme_sequences

expected_text = "The cat is on the mat"
audio_path = r"C:\Users\praga\OneDrive\Desktop\PLANS\sem8\FYP\inpyt.wav"

start_time = time.time()
spoken_text = speech_to_text(audio_path)

expected_ph, spoken_ph = get_phoneme_sequences(expected_text, spoken_text)

session_profile = build_error_profile(expected_ph, spoken_ph)

cumulative_profile = {}
cumulative_profile = update_cumulative_profile(cumulative_profile, session_profile)

print("Session Error Profile:", session_profile)
print("Cumulative Error Profile:", cumulative_profile)

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