import pyttsx3
import threading
import time

class AICoach:
    def __init__(self, mode="Active - Deep Work"):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 160)  # Speaking speed
        self.engine.setProperty('volume', 1.0) # Volume level
        
        self.last_spoken_time = 0
        self.set_mode(mode)
        
    def set_mode(self, mode):
        self.mode = mode
        if mode == "Strict Focus":
            self.cooldown = 10  # Alerts more frequently
            self.drowsy_threshold = 0.22
            self.posture_threshold = 15
        elif mode == "Casual Mode":
            self.cooldown = 30  # Relaxed alerts
            self.drowsy_threshold = 0.18
            self.posture_threshold = 25
        else: # Default Active - Deep Work
            self.cooldown = 20
            self.drowsy_threshold = 0.20
            self.posture_threshold = 20

    def speak(self, text):
        current_time = time.time()
        # Check if cooldown has passed to avoid overlapping repetitive speech
        if current_time - self.last_spoken_time > self.cooldown:
            self.last_spoken_time = current_time
            # Run text-to-speech in a background thread to prevent UI lag
            threading.Thread(target=self._speak_async, args=(text,), daemon=True).start()

    def _speak_async(self, text):
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            print(f"[VOICE ERROR] {e}")