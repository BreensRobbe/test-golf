import cv2
import mediapipe as mp
import time
import pandas as pd

mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture("vids/positives.mp4")

col_names = ["frame_id", "golfer_id", "swingphase_id", 
            "nose_x", "nose_y", "left_eye_inner_x", "left_eye_inner_y", "left_eye_x", "left_eye_y" 
            , "left_eye_outer_x" , "left_eye_outer_y" , "right_eye_inner_x" , "right_eye_inner_y"
            , "right_eye_x", "right_eye_y" , "right_eye_outer_x" , "right_eye_outer_y"
            , "left_ear_x" , "left_ear_y" , "right_ear_x" , "right_ear_y" , "mouth_left_x", "mouth_left_y"
            , "mouth_right_x" , "mouth_right_y", "left_shoulder_x", "left_shoulder_y", "right_shoulder_x", 
            "right_shoulder_y", "left_elbow_x", "left_elbow_y", "right_elbow_x", "right_elbow_y",
            "left_wrist_x", "left_wrist_y" , "right_wrist_x" , "right_wrist_y", "left_pinky_x", "left_pink_y", 
            "right_pinky_x", "right_pinky_y", "left_index_x", "left_index_y", "right_index_x", "right_index_y",
            "left_thumb_x", "left_thumb_y", "right_thumb_x", "right_thumb_y", "left_hip_x", "left_hip_y",
            "right_hip_x", "right_hip_y", "left_knee_x", "left_knee_y", "right_knee_x", "right_knee_y",
            "left_ankle_x", "left_ankle_y", "right_ankle_x", "right_ankle_y", "left_heel_x", "left_heel_y", 
            "right_heel_x", "right_heel_y", "left_foot_index_x", "left_foot_index_y", "right_foot_index_x", "right_foot_index_y",]

#df = pd.Dataframe(columns=col_names)


prevTime = 0
count = 0
while True:
    succes, img = cap.read()
    count += 1

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            if id == 14:
                print(count, id, lm.x, lm.y)
                #df.append(pd.DataFrame({""}))
            cx, cy = int(lm.x * w), int(lm.y * h)
            cv2.circle(img, (cx,cy), 5, (255,0,0), cv2.FILLED)

            

    currentTime = time.time()
    fps = 1 / (currentTime - prevTime)
    prevTime = currentTime

    cv2.putText(img, str(int(fps)), (70,50), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 3)
    cv2.imshow("image", img)
    cv2.waitKey(10)