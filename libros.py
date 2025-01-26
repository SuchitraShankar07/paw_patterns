import librosa
import main2
import main
import numpy as np
from moviepy.editor import VideoFileClip

def libro(video_file):
    def extract_audio_from_video(video_path, output_audio_path='temp_audio.wav'):
        video = VideoFileClip(video_path)
        audio = video.audio
        audio.write_audiofile(output_audio_path, codec='pcm_s16le')
        video.close()

    def analyze_frequencies_per_second(audio_path, sr=22050):
        y, sr = librosa.load(audio_path, sr=sr)
        frequency_map = {}
        duration_in_seconds = int(librosa.get_duration(y=y, sr=sr))
        for i in range(duration_in_seconds):
            start_sample = i * sr
            end_sample = start_sample + sr
            y_segment = y[start_sample:end_sample]
            D = np.abs(librosa.stft(y_segment))
            summed_spectrum = np.sum(D, axis=1)
            peak_freq_index = np.argmax(summed_spectrum)
            peak_freq = librosa.fft_frequencies(sr=sr)[peak_freq_index]
            frequency_map[i] = peak_freq
        return frequency_map

    temp_audio_path = 'temp_audio.wav'
    extract_audio_from_video(video_file, temp_audio_path)
    frequencies_per_second = analyze_frequencies_per_second(temp_audio_path)

    a = []
    n = 0

    for second, freq in frequencies_per_second.items():
        a1 = [0, 0]
        sound = 0
        if 750 > freq > 170:
            if freq > 450:
                sound = 4
                print(f"Second {second}: Dominant frequency {freq:.2f} Hz")
            else:
                sound = 1
                a1 = main2.doggo(video_file, second)
                print(f"{second} : HOWLING ZONE")
        else:
            print("NORMAL")
        print("a : ", (a1))
        a.append([sound, a1[1]])

    sets = []
    sad = 0
    Happy = 0
    Relaxed = 0
    Angry = 0
    for x in range(len(a)):
        if a[x] == [1, 0]:
            print("SAD")
            sad += 1
        elif a[x] == [0, 1]:
            print("Happy")
            Happy += 1
        elif a[x] == [0, 0]:
            print("Relaxed")
            Relaxed += 1
        elif a[x] == [4, 0]:
            print("Angry")
            Angry += 1
    sets.append(sad)
    sets.append(Happy)
    sets.append(Relaxed)
    sets.append(Angry)

    main.chart(sets)

libro('/home/Suchitra/Desktop/code./hack/videoplayback.mp4')