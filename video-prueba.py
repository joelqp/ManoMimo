import picamera

camera=picamera.PiCamera()
camera.resolution = (640, 360)
camera.framerate=20


camera.start_recording('video.h264')

camera.wait_recording(10)

camera.stop_recording()

camera.close()