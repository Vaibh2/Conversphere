from flask import Flask, render_template, Response, request
import cv2

application = Flask(__name__)
camera = cv2.VideoCapture(0)
name = ""


def gen_frames():
    global name

    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            detector = cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')
            faces = detector.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=15)

            if len(faces) == 1:
                x, y, w, h = faces[0]

                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

                roi_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                roi_color = frame[y:y + h, x:x + w]

                cv2.putText(frame, name, (x, y + h + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()

                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            elif len(faces) > 1:
                exit(0)
            else:
                pass
@application.route('/', methods=['GET', 'POST'])
def index():
    global name

    if request.method == 'POST':
        name = request.form['name']

    return render_template('output1.html')


@application.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    application.run(debug=True)