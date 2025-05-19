import speech_recognition as sr
import moviepy.editor as mp

def extract_audio_text(filepath):
    try:
        if filepath.endswith(('.mp4', '.mkv', '.mov')):
            clip = mp.VideoFileClip(filepath)
            audio_path = filepath.rsplit('.', 1)[0] + ".wav"
            clip.audio.write_audiofile(audio_path)
        else:
            audio_path = filepath

        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_path) as source:
            audio = recognizer.record(source)
            return recognizer.recognize_google(audio)

    except Exception as e:
        return f"Error during transcription: {str(e)}"
