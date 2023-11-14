*import cv2
cap = cv2.VideoCapture("C:/Users/susri/Downloads/istockphoto-1255754954-640_adpp_is.mp4")  

if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()
fps = int (cap.get(cv2.CAP_PROP_FPS))
slow_motion_writer = cv2.VideoWriter('slow_motion_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (640, 480))  # Adjust the resolution as needed
fast_motion_writer = cv2.VideoWriter('fast_motion_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (640, 480))  # Adjust the resolution as needed

while True:
    ret, frame = cap.read()
    if not ret:
        break
    slow_motion_writer.write(frame)
    slow_motion_writer.write(frame)
    
    if cv2.waitKey(1) & 0xFF == ord('f'):
        fast_motion_writer.write(frame)
        
    cv2.imshow('Video', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
slow_motion_writer.release()
fast_motion_writer.release()
cv2.destroyAllWindows()
