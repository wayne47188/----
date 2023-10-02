import cv2
import mediapipe as mp
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


# 數據標籤
labels = ["high_quality", "low_quality"]

# 使用Mediapipe Pose提取特徵，以座標為特徵數據

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

def extract_features_from_image(image_path):
    # 讀取圖像
    image = cv2.imread(image_path)
    
    # 轉換為rgb
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # 提取關鍵點
    with mp_pose.Pose() as pose:
        results = pose.process(image_rgb)
        keypoints = results.pose_landmarks.landmark
    
    # 提取關鍵點座標
    feature_vector = []
    for keypoint in keypoints:
        feature_vector.extend([keypoint.x, keypoint.y, keypoint.z])
    
    return feature_vector

# 假設有一個含有圖像路徑和數據的列表
data = [
    {"image_path": "path_to_image1.jpg", "label": "high_quality"},
    {"image_path": "path_to_image2.jpg", "label": "low_quality"},
    # 添加更多數據
]

# 提取特徵標籤
features = []
labels = []
for item in data:
    image_path = item["image_path"]
    label = item["label"]
    
    feature_vector = extract_features_from_image(image_path)
    
    features.append(feature_vector)
    labels.append(label)

# 劃分測試集合訓練集
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# 初始化svm分類器
svm_classifier = SVC(kernel='linear', C=1)

# 訓練模型
svm_classifier.fit(X_train, y_train)

# 預測測試集
y_pred = svm_classifier.predict(X_test)

# 計算準確度
accuracy = accuracy_score(y_test, y_pred)
print("模型準確度：", accuracy)
