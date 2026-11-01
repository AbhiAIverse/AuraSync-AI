import cv2
from core.detector import AuraSyncDetector
from core.analytics import SessionAnalytics

def main():
    print("[INFO] Initializing AuraSync AI Camera & Voice Coach...")
    detector = AuraSyncDetector(mode="Active - Deep Work")
    analytics = SessionAnalytics()
    
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("[ERROR] Could not open webcam.")
        return

    print("[INFO] AuraSync AI is running. Press 'q' to exit the session.")
    
    try:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                print("[WARNING] Failed to grab frame.")
                break
                
            # Process frame through vision pipeline
            processed_frame, avg_ear, is_drowsy, posture_status, is_bad_posture, ai_advice = detector.process_frame(frame)
            
            # Log metrics for analytics report
            analytics.log_frame(is_drowsy, is_bad_posture)
            
            # Display real-time UI overlay on video feed
            cv2.putText(processed_frame, f"EAR: {avg_ear:.2f}", (30, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(processed_frame, f"Posture: {posture_status}", (30, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
            if ai_advice:
                cv2.putText(processed_frame, f"AI: {ai_advice}", (30, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 100, 100), 2)
                
            cv2.imshow("AuraSync AI - Posture & Wellness Monitor", processed_frame)
            
            # Press 'q' to quit session
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        # Clean up and export session report telemetry
        cap.release()
        cv2.destroyAllWindows()
        analytics.export_report()
        print("[INFO] Session ended. Analytics report generated successfully!")

if __name__ == "__main__":
    main()