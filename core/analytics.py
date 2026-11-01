import json
import time
from datetime import datetime

class SessionAnalytics:
    def __init__(self):
        self.start_time = time.time()
        self.drowsy_count = 0
        self.bad_posture_count = 0
        self.total_frames = 0
        
    def update(self, is_drowsy, is_bad_posture):
        self.total_frames += 1
        if is_drowsy:
            self.drowsy_count += 1
        if is_bad_posture:
            self.bad_posture_count += 1
            
    def generate_report(self):
        end_time = time.time()
        duration_seconds = round(end_time - self.start_time, 2)
        
        report_data = {
            "session_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "duration_seconds": duration_seconds,
            "total_frames_monitored": self.total_frames,
            "fatigue_events_detected": self.drowsy_count,
            "bad_posture_events_detected": self.bad_posture_count,
            "status": "Completed Successfully"
        }
        
        # Save report to a JSON file in root directory
        file_name = "session_report.json"
        with open(file_name, "w") as f:
            json.dump(report_data, f, indent=4)
            
        print(f"[INFO] Session analytics saved successfully to {file_name}")
        return report_data