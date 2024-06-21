import numpy as np
from pydub import AudioSegment


def load_audio(file_path):
    try:
        audio = AudioSegment.from_file(file_path)
        # Convert audio to numpy array (16-bit signed PCM format)
        audio_data = np.array(audio.get_array_of_samples(), dtype=np.int16)
        return audio_data
    except Exception as e:
        print(f"Error: {e}")
        return None


def check_lsb_steganography(audio_data):
    try:
        # Extract the least significant bits
        lsb_array = np.bitwise_and(audio_data, 1)

        # Calculate the percentage of 1s in the LSB array
        lsb_ratio = np.mean(lsb_array)
        print(f"LSB Ratio: {lsb_ratio:.4f}")

        # Heuristic: If the ratio is significantly different from 0.5, it might indicate hidden data
        if abs(lsb_ratio - 0.5) > 0.1:  # Threshold can be adjusted
            print("Potential steganography detected based on LSB analysis.")
        else:
            print("No steganography detected based on LSB analysis.")
    except Exception as e:
        print(f"Error during LSB analysis: {e}")


def main():
    file_path = input("Enter the audio file path (WAV or MP3): ")
    audio_data = load_audio(file_path)
    if audio_data is not None:
        check_lsb_steganography(audio_data)
    else:
        print("Failed to load and process the audio file.")


if __name__ == "__main__":
    main()
