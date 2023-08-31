


import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import cv2

# Initialize speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def listen():
    """Listens to user's voice command"""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)  # Use Google Speech Recognition API
        print(f"User: {command}")
        process_command(command.lower())
    except sr.UnknownValueError:
        print("Unable to recognize speech.")
    except sr.RequestError:
        print("Speech recognition service is unavailable.")

def speak(text):
    """Speaks the given text"""
    engine.say(text)
    engine.runAndWait()

def open_camera():
    """Opens the camera and displays the video stream"""
    cap = cv2.VideoCapture(0)  # Open the default camera (index 0)

    while True:
        ret, frame = cap.read()  # Read a frame from the camera

        cv2.imshow("Camera", frame)  # Display the frame

        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and close all windows
    cap.release()
    cv2.destroyAllWindows()

def greet():
    """Greets the user"""
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am Tracy . How can I assist you today?")

def search_wikipedia(query):
    """Searches and speaks a summary from Wikipedia"""
    try:
        result = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia:")
        speak(result)
    except wikipedia.exceptions.PageError:
        speak("Sorry, I couldn't find any relevant information.")
    except wikipedia.exceptions.DisambiguationError:
        speak("Multiple results found. Please provide more specific query.")
def speak(text):
    """Speaks the given text and prints it"""
    print("Jarvis:", text)  # Print the text to console
    engine.say(text)  # Speak the text
    engine.runAndWait()

def open_website(url):
    """Opens a website in the default web browser"""
    webbrowser.open(url)

def play_music():
    """Plays a random music track from a designated directory"""
    music_dir = "path/to/music/directory"
    music_files = os.listdir(music_dir)
    if music_files:
        random_music = os.path.join(music_dir, random.choice(music_files))
        os.startfile(random_music)
    else:
        speak("No music files found.")

def process_command(command):
    """Processes the user's command and provides a response"""
    if "hello" in command:
        greet()
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}.")
    elif "search" in command:
        query = command.replace("search", "").strip()
        search_wikipedia(query)
    elif "website" in command:
        website = command.replace("website", "").strip()
        open_website("https://www." + website + ".com")
    elif "open camera" in command:
        speak("Opening the camera.")
        open_camera()
    elif "music" in command:
        play_music()
    elif "exit" in command or "bye" in command:
        speak("Goodbye! ")
        exit()
    else:
        speak("I'm sorry, I couldn't understand your command.")

# Main loop
if __name__ == "__main__":
    greet()

    while True:
        listen()
