import time
import pyttsx3
import threading

class AICoach:
    def __init__(self):
        self.last_advice_time = 0
        self.cooldown_period = 25  # Cooldown in seconds to avoid spamming advice
        
        self.wellness_tips = [
            "Hey coder, sit straight and protect your spine!",
            "High fatigue detected. Take a quick break and drink some water.",
            "Remember the 20-20-20 rule. Look away from the screen.",
            "Roll your shoulders back and check your ergonomics."
        ]
        self.tip_index = 0

    def speak(self, text):
        # Run text-to-speech in a background thread to prevent OpenCV video lagging
        def _run_speech():
            try:
                engine = pyttsx3.init()
                engine.setProperty('rate', 160)  # Setting speech speed
                engine.say(text)
                engine.runAndWait()
            except Exception as e:
                print(f"[WARNING] TTS Error: {e}")

        threading.Thread(target=_run_speech, daemon=True).start()

    def get_advice(self, is_drowsy, is_bad_posture):
        current_time = time.time()
        
        # Trigger advice and voice alert only if drowsy or bad posture and cooldown has passed
        if (is_drowsy or is_bad_posture) and (current_time - self.last_advice_time > self.cooldown_period):
            self.last_advice_time = current_time
            
            advice = self.wellness_tips[self.tip_index]
            self.tip_index = (self.tip_index + 1) % len(self.wellness_tips)
            
            # Trigger audio speech
            self.speak(advice)
            return advice
            
        return None