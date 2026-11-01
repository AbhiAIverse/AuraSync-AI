import cv2
import mediapipe as mp
import numpy as np
from core.metrics import FatigueMetrics
from core.posture import PostureAnalyzer
from core.ai_coach import AICoach

class AuraSyncDetector:
    def __init__(self):
        self.mp_face_mesh = mp.solutions.face_mesh
        self.mp_pose = mp.solutions.pose
        
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            max_num_faces=1,
            min_detection_confidence=0.6,
            min_tracking_confidence=0.6
        )
        self.pose = self.mp_pose.Pose(
            min_detection_confidence=0.6,
            min_tracking_confidence=0.6
        )
        
        self.fatigue_monitor = FatigueMetrics()
        self.posture_analyzer = PostureAnalyzer()
        self.ai_coach = AICoach()
        
    def process_frame(self, frame):
        h, w, c = frame.shape
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image_rgb.flags.writeable = False
        
        face_results = self.face_mesh.process(image_rgb)
        pose_results = self.pose.process(image_rgb)
        
        image_rgb.flags.writeable = True
        annotated_frame = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)
        
        avg_ear = 0.0
        is_drowsy = False
        posture_status = "UNKNOWN"
        is_bad_posture = False
        
        # Evaluate fatigue if face landmarks are detected
        if face_results.multi_face_landmarks:
            for face_landmarks in face_results.multi_face_landmarks:
                avg_ear, is_drowsy = self.fatigue_monitor.evaluate_fatigue(face_landmarks, w, h)
                
        # Evaluate posture if pose landmarks are detected
        if pose_results.pose_landmarks:
            posture_status, is_bad_posture = self.posture_analyzer.evaluate_posture(pose_results.pose_landmarks, w, h)
            
            mp.solutions.drawing_utils.draw_landmarks(
                annotated_frame, pose_results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS,
                mp.solutions.drawing_utils.DrawingSpec(color=(0,255,0), thickness=2, circle_radius=2),
                mp.solutions.drawing_utils.DrawingSpec(color=(0,0,255), thickness=2, circle_radius=2)
            )
            
        # Get AI Coach advice if needed
        ai_advice = self.ai_coach.get_advice(is_drowsy, is_bad_posture)
                
        return annotated_frame, avg_ear, is_drowsy, posture_status, is_bad_posture, ai_advice