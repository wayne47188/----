# 初始化錯誤計數器
error_counter = 0

# 初始化每個步驟的符合標準幀數和總幀數
step_frames = {'pose_detection': 0, 'ready_pose': 0, 'completed_pose': 0}
total_frames = {'pose_detection': 0, 'ready_pose': 0, 'completed_pose': 0}

# 定義每個步驟的得分閾值（這裡以85%為例）
score_threshold = 85

while video_is_running:
    # 捕捉一幀視頻數據並進行身體檢測
    frame = capture_frame()
    pose_result = pose_detection(frame)

    # 更新總幀數
    total_frames['pose_detection'] += 1

    # 檢查是否符合標準，可以根據需要進一步定義標準
    if pose_is_correct(pose_result):
        step_frames['pose_detection'] += 1

    # 檢查其他步驟的相似操作，進行紀錄，類似於上述步驟

    # 計算每個步驟的得分
    step_scores = {}
    for step in step_frames:
        step_scores[step] = (step_frames[step] / total_frames[step]) * 100

    # 檢查是否任何一個步驟的得分低於閾值
    for step, score in step_scores.items():
        if score < score_threshold:
            error_counter += 1

    # 如果錯誤計數器達到5，則觸發提醒
    if error_counter >= 5:
        show_error_message()
