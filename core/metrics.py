import numpy as np
from scipy.spatial import distance

class FatigueMetrics:
    def __init__(self):
        # MediaPipe Face Mesh landmark indices for Left and Right eyes
        self.LEFT_EYE_INDICES = [362, 385, 387, 263, 373, 380]
        self.RIGHT_EYE_INDICES = [33, 160, 158, 133, 153, 144]
        
        # Threshold for detecting a blink or fatigue
        self.EAR_THRESHOLD = 0.22
        self.consecutive_frames = 0
        self.fatigue_alert_count = 0

    def calculate_ear(self, eye_landmarks):
        # Euclidean distances between vertical eye landmarks
        A = distance.euclidean(eye_landmarks[1], eye_landmarks[5])
        B = distance.euclidean(eye_landmarks[2], eye_landmarks[4])

        # Euclidean distance between horizontal eye landmarks
        C = distance.euclidean(eye_landmarks[0], eye_landmarks[3])

        # Eye Aspect Ratio formula
        ear = (A + B) / (2.0 * C)
        return ear

    def evaluate_fatigue(self, face_landmarks, frame_width, frame_height):
        if not face_landmarks:
            return 0.0, False

        # Extracting coordinates for left and right eyes
        left_eye = np.array([[face_landmarks.landmark[i].x * frame_width, 
                              face_landmarks.landmark[i].y * frame_height] for i in self.LEFT_EYE_INDICES])
        right_eye = np.array([[face_landmarks.landmark[i].x * frame_width, 
                               face_landmarks.landmark[i].y * frame_height] for i in self.RIGHT_EYE_INDICES])

        left_ear = self.calculate_ear(left_eye)
        right_ear = self.calculate_ear(right_eye)

        # Average EAR for both eyes
        avg_ear = (left_ear + right_ear) / 2.0

        is_drowsy = False
        if avg_ear < self.EAR_THRESHOLD:
            self.consecutive_frames += 1
            if self.consecutive_frames >= 15:  # If eyes closed for consecutive frames
                is_drowsy = True
        else:
            self.consecutive_frames = 0

        return avg_ear, is_drowsy