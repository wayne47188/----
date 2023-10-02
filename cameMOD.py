import cv2
import mediapipe as mp

# 初始化MediaPipe姿勢估計模型
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# 初始化MediaPipe視覺輔助庫
mp_drawing = mp.solutions.drawing_utils

# 初始化攝像頭
cap = cv2.VideoCapture(0)  # 使用第一個攝像頭

while cap.isOpened():
    # 讀取攝像頭畫面
    ret, frame = cap.read()
    if not ret:
        continue

    # 轉換BGR圖像為RGB格式
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    ##
    # 前處理步驟
    # 調整亮度和對比度
    alpha = 1.5  # 亮度增強因子
    beta = 10    # 對比度增強因子
    rgb_frame = cv2.convertScaleAbs(rgb_frame, alpha=alpha, beta=beta)

    # 使用MediaPipe姿勢估計模型進行身體檢測
    results = pose.process(rgb_frame)

    # 繪製姿勢估計結果
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    # 顯示結果
    cv2.imshow("Body Pose Detection", frame)

    # 按下 "q" 鍵退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 釋放攝像頭資源並關閉視窗
cap.release()
cv2.destroyAllWindows()