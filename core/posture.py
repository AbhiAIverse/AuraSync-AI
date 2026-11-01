import numpy as np

class PostureAnalyzer:
    def __init__(self):
        # Threshold for slouching detection based on shoulder and nose alignment
        self.SLOUCH_THRESHOLD = 30.0

    def evaluate_posture(self, pose_landmarks, frame_width, frame_height):
        if not pose_landmarks:
            return "UNKNOWN", False

        # Extracting shoulder and nose coordinates
        left_shoulder = pose_landmarks.landmark[11]
        right_shoulder = pose_landmarks.landmark[12]
        nose = pose_landmarks.landmark[0]

        # Convert normalized coordinates to pixel values
        ls_y = left_shoulder.y * frame_height
        rs_y = right_shoulder.y * frame_height
        nose_y = nose.y * frame_height

        # Calculate average shoulder height
        avg_shoulder_y = (ls_y + rs_y) / 2.0

        # Simple heuristic: if nose drops too close to shoulder level or shoulders tilt drastically
        posture_status = "GOOD"
        is_bad_posture = False

        # Difference between nose and shoulder vertical position
        vertical_diff = avg_shoulder_y - nose_y

        if vertical_diff < 100.0:  # Threshold for slouching/leaning forward
            posture_status = "SLOUCHING / BAD POSTURE"
            is_bad_posture = True

        return posture_status, is_bad_posture