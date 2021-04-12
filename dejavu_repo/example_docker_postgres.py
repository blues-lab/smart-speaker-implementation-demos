import json
import sys
from dejavu import Dejavu
from dejavu.logic.recognizer.file_recognizer import FileRecognizer
from dejavu.logic.recognizer.microphone_recognizer import MicrophoneRecognizer

# load config from a JSON file (or anything outputting a python dictionary)
config = {
    "database": {
        "host": "db",
        "user": "postgres",
        "password": "password",
        "database": "dejavu"
    },
    "database_type": "postgres"
}

if __name__ == '__main__':

    # create a Dejavu instance
    djv = Dejavu(config)

    # Fingerprint all the mp3's in the directory we give it
    # djv.fingerprint_directory("test2", [".wav"])
    #djv.fingerprint_file(file_path="test_fingerprint_full.wav", song_name="Field of Hopes and Dreams")
    # Recognize audio from a file
    #results = djv.recognize(FileRecognizer, "mp3/Josh-Woodward--I-Want-To-Destroy-Something-Beautiful.mp3")
    #print(f"From file we recognized: {results}\n")

    # Or use a recognizer without the shortcut, in anyway you would like
    recognizer = FileRecognizer(djv)
    file_name = sys.argv[1]
    print(f"Checking fingerprint for file {file_name}")
    results = recognizer.recognize_file(file_name)
    print(f"No shortcut, we recognized: {results}\n")
