import moviepy.editor as mp
from scipy.signal import butter, lfilter
import librosa
import numpy as np
import io
import ffmpeg
from scipy.io import wavfile

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return b, a

def bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

def extract_audio_to_memory(video_path):
    """Extract audio from video and return as an in-memory bytes object."""
    out, _ = (
        ffmpeg
        .input(video_path)
        .output('pipe:1', format='wav')
        .run(capture_stdout=True, capture_stderr=True)
    )
    return io.BytesIO(out)

def calculate_excitedness(video_path, average_weight : float = 0.7, max_weight : float = 0.3):
    video = mp.VideoFileClip(video_path)
    audio_buffer = extract_audio_to_memory(video_path)
    
    y, sr = librosa.load(audio_buffer, sr=None)
    
    lowcut = 300
    highcut = 3000
    filtered_audio = bandpass_filter(y, lowcut, highcut, sr)

    hop_length = 512
    frame_length = 2048
    energy = librosa.feature.rms(y=filtered_audio, frame_length=frame_length, hop_length=hop_length)[0]

    pitches, magnitudes = librosa.core.piptrack(y=filtered_audio, sr=sr, hop_length=hop_length)

    pitch_max = []
    for t in range(pitches.shape[1]):
        pitch = pitches[:, t]
        pitch_max.append(pitch[pitch > 0].max() if len(pitch[pitch > 0]) > 0 else 0)
    
    pitch_max = np.array(pitch_max)

    excitedness = energy * pitch_max
    
    average_score = np.mean(excitedness)
    max_score = np.max(excitedness)

    print(f"Average Excitedness Score: {average_score:.2f}")
    print(f"Maximum Excitedness Score: {max_score:.2f}")
    
    return average_score * average_weight + max_score * max_weight


def calculate_video_sentiment(video_path):
    video = mp.VideoFileClip(video_path)
    audio_buffer = extract_audio_to_memory(video_path)
    
    y, sr = librosa.load(audio_buffer, sr=None)
    

    lowcut = 300
    highcut = 3000
    filtered_audio = bandpass_filter(y, lowcut, highcut, sr)
    
    filtered_audio_int16 = np.int16(filtered_audio / np.max(np.abs(filtered_audio)) * 32767)

    output_wav_path = "filtered_audio.wav"
    wavfile.write(output_wav_path, sr, filtered_audio_int16)
    
    return output_wav_path


# if __name__ == "__main__":
#     calculate_video_sentiment("temp.mp4")