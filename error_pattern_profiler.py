def build_error_profile(expected_phonemes, spoken_phonemes):
    error_profile = {}
    for e, s in zip(expected_phonemes, spoken_phonemes):
        if e != s:
            if e not in error_profile:
                error_profile[e] = 1
            else:
                error_profile[e] += 1
    return error_profile

def update_cumulative_profile(cumulative_profile, session_profile):
    for phoneme, count in session_profile.items():
        if phoneme not in cumulative_profile:
            cumulative_profile[phoneme] = count
        else:
            cumulative_profile[phoneme] += count
    return cumulative_profile
