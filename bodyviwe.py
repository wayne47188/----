import cv2
import mediapipe as mp

# 初始化Mediapipe的Blazepose模組
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# 初始化攝像頭
cap = cv2.VideoCapture(0)

# 創建Blazepose模組實例
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            continue

        # 將影像轉換成RGB格式
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # 進行身體姿勢檢測
        results = pose.process(frame_rgb)

        # 如果檢測成功，可繪製關鍵點和連線
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        cv2.imshow('Body Pose Detection', frame)

        # 按下'q'鍵退出應用
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

