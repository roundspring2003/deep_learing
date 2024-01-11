import os
import librosa
import soundfile as sf
import noisereduce as nr
DIR_WAV = "Dataset_wav\\"

def remove_noise(input_path, output_path):
    audio_data, sample_rate = librosa.load(input_path, sr=None)
    reduced_noise = nr.reduce_noise(y=audio_data, sr=sample_rate)
    sf.write(output_path, reduced_noise, sample_rate)
    print(input_path+": OK")

all_WAV_Names = [file for file in os.listdir(DIR_WAV) if file.endswith(".wav")]
for name in all_WAV_Names:
    remove_noise(DIR_WAV+name, DIR_WAV+name)