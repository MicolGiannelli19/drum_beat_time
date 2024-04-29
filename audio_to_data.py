import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# Load the audio file
audio_path = "audio/Performance.wav"
metronome_path = "audio/Metronomo.wav"
y, sr = librosa.load(audio_path, duration=10)
y_metronome, sr_metronome = librosa.load(metronome_path, duration=10)

# sanity check
print(
    librosa.get_duration(y=y, sr=sr),
    librosa.get_duration(y=y_metronome, sr=sr_metronome),
)

print(y.shape, y_metronome.shape)

print(y[:10], y_metronome[:10])

onset_env = librosa.onset.onset_strength(y=y, sr=sr, aggregate=np.median)

tempo, beats = librosa.beat.beat_track(onset_envelope=onset_env, sr=sr)

# import aubio
# import pandas as pd


# def detect_drum_beats(audio_file):
#     # Open audio file
#     samplerate, audio = aubio.source(audio_file)

#     # Create tempo and beat tracker
#     tempo_detector = aubio.tempo("default", audio.samplerate)
#     beat_detector = aubio.beat("default", audio.samplerate)

#     # Initialize beat times list
#     beat_times = []

#     # Process audio frames and detect beats
#     total_frames = 0
#     while True:
#         samples, read = audio()
#         if read < audio.hop_size:
#             break
#         total_frames += read

#         # Detect tempo
#         tempo = tempo_detector(samples)

#         # Detect beats
#         if beat_detector(samples):
#             beat_times.append(total_frames / float(samplerate))

#     # Create DataFrame with beat number and time
#     beat_df = pd.DataFrame(
#         {"Beat": range(1, len(beat_times) + 1), "Time (s)": beat_times}
#     )

#     return beat_df


# beat_dataframe = detect_drum_beats(audio_path)
# print(beat_dataframe)
