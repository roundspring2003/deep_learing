import librosa
import librosa.display
import matplotlib.pyplot as plt

# Ū�����T�ɮ�
file_path = 'path_to_your_audio_file.wav'  # �д����A�����T�ɮ׸��|
audio_data, sample_rate = librosa.load(file_path)

# �p�⭵�T���u�ɳť߸��ܴ� (STFT)
stft = librosa.stft(audio_data)

# �N�T���ഫ������ (dB)
spectrogram = librosa.amplitude_to_db(abs(stft))

# ����W�й�
plt.figure(figsize=(10, 5))
librosa.display.specshow(spectrogram, sr=sample_rate, x_axis='time', y_axis='hz')
plt.colorbar(format='%+2.0f dB')
plt.title('Spectrogram')
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.tight_layout()

# ����W�й�
plt.show()
