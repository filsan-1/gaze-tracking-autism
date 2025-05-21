import cv2
import mediapipe as mp
from gaze import gaze
import time
from logger import get_fixation_stats

# Setup MediaPipe face mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    refine_landmarks=True
)

# Video stream and recording setup
cap = cv2.VideoCapture(0)
width, height = 640, 480
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('autism_gaze_session.avi', fourcc, 20.0, (width, height))

print("🟢 Starting autism screening session...\nPress 'q' to stop.")

start_time = time.time()

# Real-time stats
fixation_counter = {
    'eyes_left': 0,
    'eyes_right': 0,
    'mouth': 0,
    'nose': 0,
    'none': 0
}

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (width, height))
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:
        for landmarks in results.multi_face_landmarks:
            # Draw face mesh (optional)
            # mp.solutions.drawing_utils.draw_landmarks(frame, landmarks, mp_face_mesh.FACEMESH_CONTOURS)

            # Analyze gaze and draw red line
            target = gaze(frame, landmarks)
            fixation_counter[target] += 1

    # Write frame to video
    out.write(frame)

    # Show frame
    cv2.imshow("Autism Screening", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Stop everything
cap.release()
out.release()
cv2.destroyAllWindows()

# Analyze fixation behavior
total_duration = time.time() - start_time
risk_score, report = get_fixation_stats(fixation_counter, total_duration)

print("\n📊 Session Complete")
print(report)
