import cv2
from core.detector import AuraSyncDetector
from core.analytics import SessionAnalytics

def main():
    cap = cv2.VideoCapture(0)
    detector = AuraSyncDetector()
    analytics = SessionAnalytics()
    
    print("[INFO] AuraSync AI Complete Vision, Ergonomic, Voice AI & Analytics Engine Initialized...")
    
    current_advice = "Stay focused! AI Coach is monitoring your wellness."
    
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            print("[WARNING] Ignoring empty camera frame.")
            break
            
        frame = cv2.flip(frame, 1)
        processed_frame, avg_ear, is_drowsy, posture_status, is_bad_posture, ai_advice = detector.process_frame(frame)
        
        # Update session analytics metrics
        analytics.update(is_drowsy, is_bad_posture)
        
        # Update advice if new advice is triggered by AI Coach
        if ai_advice:
            current_advice = ai_advice
        
        # Display professional HUD overlay text
        cv2.putText(processed_frame, "STATUS: SYSTEM ACTIVE [PRO]", (30, 40), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 128), 2, cv2.LINE_AA)
        
        # Display Eye Aspect Ratio (EAR) on screen
        ear_text = f"EAR (Fatigue Index): {avg_ear:.2f}"
        cv2.putText(processed_frame, ear_text, (30, 80), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2, cv2.LINE_AA)
        
        # Display Posture Status on screen
        posture_text = f"Posture: {posture_status}"
        posture_color = (0, 0, 255) if is_bad_posture else (0, 255, 0)
        cv2.putText(processed_frame, posture_text, (30, 120), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, posture_color, 2, cv2.LINE_AA)
        
        # Show warning alerts if drowsy or bad posture
        y_offset = 160
        if is_drowsy:
            cv2.putText(processed_frame, "ALERT: HIGH FATIGUE / DROWSINESS!", (30, y_offset), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2, cv2.LINE_AA)
            y_offset += 30
            
        if is_bad_posture:
            cv2.putText(processed_frame, "ALERT: BAD POSTURE / SLOUCHING!", (30, y_offset), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2, cv2.LINE_AA)
            y_offset += 30
            
        # Display AI Coach advice banner at the bottom of the screen
        h, w, _ = processed_frame.shape
        cv2.rectangle(processed_frame, (0, h - 50), (w, h), (20, 20, 20), -1)
        cv2.putText(processed_frame, f"AI Coach: {current_advice}", (20, h - 18), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2, cv2.LINE_AA)
        
        cv2.imshow("AuraSync AI - Professional Vision Engine", processed_frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    # Generate and save session report JSON upon exit
    analytics.generate_report()
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()