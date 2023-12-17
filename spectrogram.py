import librosa
import librosa.display
import matplotlib.pyplot as plt

# 讀取音訊檔案
file_path = 'path_to_your_audio_file.wav'  # 請換成你的音訊檔案路徑
audio_data, sample_rate = librosa.load(file_path)

# 計算音訊的短時傅立葉變換 (STFT)
stft = librosa.stft(audio_data)

# 將幅度轉換為分貝 (dB)
spectrogram = librosa.amplitude_to_db(abs(stft))

# 顯示頻譜圖
plt.figure(figsize=(10, 5))
librosa.display.specshow(spectrogram, sr=sample_rate, x_axis='time', y_axis='hz')
plt.colorbar(format='%+2.0f dB')
plt.title('Spectrogram')
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.tight_layout()

# 顯示頻譜圖
plt.show()
