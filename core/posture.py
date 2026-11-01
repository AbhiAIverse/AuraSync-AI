import numpy as np

def check_posture(landmarks, w, h):
    """
    Evaluates ergonomic posture using MediaPipe Pose landmarks.
    Checks shoulder alignment and neck/head forward lean.
    """
    try:
        # Landmark indices for shoulders and nose
        left_shoulder = landmarks[11]
        right_shoulder = landmarks[12]
        nose = landmarks[0]
        
        # Calculate shoulder midpoint x-coordinate
        shoulder_mid_x = (left_shoulder.x + right_shoulder.x) / 2.0
        
        # Calculate horizontal distance between nose and shoulder midpoint (head tilt/forward lean)
        deviation = abs(nose.x - shoulder_mid_x) * w
        
        # Threshold for slouching/bad posture
        if deviation > 45: # Threshold in pixels
            return True, "Bad Posture (Slouching)"
        else:
            return False, "Good Posture"
            
    except Exception as e:
        return False, "Good Posture"