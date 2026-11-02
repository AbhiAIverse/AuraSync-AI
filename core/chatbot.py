import random

class WellnessChatbot:
    def __init__(self):
        self.responses = [
            "Based on your telemetry, you've been working intensely. Try the 20-20-20 rule: look at something 20 feet away for 20 seconds to relieve eye strain!",
            "It looks like your shoulder posture dropped recently. Sit up straight, roll your shoulders back, and take three deep breaths.",
            "Great focus today! However, a 5-minute stretch break right now will boost your cognitive efficiency for the next hour.",
            "To prevent burnout, ensure your monitor is at eye level and keep your wrists neutral while typing."
        ]
        
    def get_response(self, user_query):
        """Generates contextual wellness and ergonomic advice based on user queries."""
        query_lower = user_query.lower()
        if "posture" in query_lower or "back" in query_lower or "slouch" in query_lower:
            return "🪑 **Posture Tip:** Keep your feet flat on the floor, adjust your monitor to eye level, and ensure your lower back is fully supported against your chair."
        elif "eye" in query_lower or "strain" in query_lower or "vision" in query_lower:
            return "👁️ **Eye Strain Relief:** Remember the 20-20-20 rule! Every 20 minutes, look at an object 20 feet away for at least 20 seconds to relax your eye muscles."
        elif "break" in query_lower or "tired" in query_lower or "fatigue" in query_lower:
            return "⚡ **Energy Boost:** Take a 5-minute break right now. Stand up, stretch your arms upward, roll your shoulders, and drink a glass of water."
        elif "burnout" in query_lower or "stress" in query_lower:
            return "🧠 **Burnout Prevention:** Break your tasks into 25-minute Pomodoro intervals with 5-minute pauses. Check your dashboard's ML Burnout Risk meter to gauge your fatigue levels!"
        else:
            return random.choice(self.responses)