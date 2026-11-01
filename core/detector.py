import cv2
import mediapipe as mp
from core.metrics import calculate_ear
from core.posture import check_posture
from core.ai_coach import AICoach

class AuraSyncDetector:
    def __init__(self, mode="Active - Deep Work"):
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)
        
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
        
        # MediaPipe drawing utilities for facial mesh and skeleton lines
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        
        self.coach = AICoach(mode=mode)
        
    def set_detector_mode(self, mode):
        self.coach.set_mode(mode)

    def process_frame(self, frame):
        h, w, _ = frame.shape
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        face_results = self.face_mesh.process(rgb_frame)
        pose_results = self.pose.process(rgb_frame)
        
        avg_ear = 0.25
        is_drowsy = False
        posture_status = "Good Posture"
        is_bad_posture = False
        ai_advice = None
        
        # Draw Face Mesh & Process Fatigue (EAR)
        if face_results.multi_face_landmarks:
            for face_landmarks in face_results.multi_face_landmarks:
                # Draw facial mesh tessellation lines on the video frame
                self.mp_drawing.draw_landmarks(
                    image=frame,
                    landmark_list=face_landmarks,
                    connections=self.mp_face_mesh.FACEMESH_TESSELATION,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=self.mp_drawing_styles.get_default_face_mesh_tesselation_style()
                )
                
                avg_ear = calculate_ear(face_landmarks.landmark, w, h)
                if avg_ear < self.coach.drowsy_threshold:
                    is_drowsy = True
                    ai_advice = "High fatigue detected! Take a quick blink break."
                    self.coach.speak("Attention! High fatigue detected. Please take a deep breath.")
                    
        # Draw Pose Skeleton & Process Ergonomic Posture
        if pose_results.pose_landmarks:
            # Draw body posture skeleton lines on the video frame
            self.mp_drawing.draw_landmarks(
                frame,
                pose_results.pose_landmarks,
                self.mp_pose.POSE_CONNECTIONS,
                landmark_drawing_spec=self.mp_drawing_styles.get_default_pose_landmarks_style()
            )
            
            landmarks = pose_results.pose_landmarks.landmark
            is_bad_posture, posture_status = check_posture(landmarks, w, h)
            if is_bad_posture:
                ai_advice = "Slouching detected! Sit up straight."
                self.coach.speak("Ergonomic warning. Please correct your posture.")
                
        if not is_drowsy and not is_bad_posture:
            ai_advice = "Posture and focus levels are optimal. Keep going!"
            
        return frame, avg_ear, is_drowsy, posture_status, is_bad_posture, ai_advice