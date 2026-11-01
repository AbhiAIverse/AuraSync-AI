import numpy as np
from scipy.spatial import distance

def calculate_ear(landmarks, w, h):
    # MediaPipe Face Mesh landmark indices for Left eye
    LEFT_EYE_INDICES = [362, 385, 387, 263, 373, 380]
    
    try:
        # Extracting coordinates for left eye
        eye_landmarks = np.array([[landmarks[i].x * w, landmarks[i].y * h] for i in LEFT_EYE_INDICES])
        
        # Euclidean distances between vertical eye landmarks
        A = distance.euclidean(eye_landmarks[1], eye_landmarks[5])
        B = distance.euclidean(eye_indexes[2] if 'eye_indexes' in locals() else eye_landmarks[2], eye_landmarks[4]) # or simple indexing
        
        # Euclidean distance between horizontal eye landmarks
        C = distance.euclidean(eye_landmarks[0], eye_landmarks[3])

        # Eye Aspect Ratio formula
        ear = (A + B) / (2.0 * C)
        return ear
    except Exception as e:
        return 0.25