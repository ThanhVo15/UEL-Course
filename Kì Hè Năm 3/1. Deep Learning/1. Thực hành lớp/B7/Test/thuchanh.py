# Load model mà ta đã train được từ bước trước
model = load_model('model.h5')
# Góc lái hiện tại của ô tô
steering_angle = float(data["steering_angle"])
# Tốc độ hiện tại của ô tô
speed = float(data["speed"])
# Ảnh từ camera giữa
image = Image.open(BytesIO(base64.b64decode(data["image"])))
try:
# Tiền xử lý ảnh, cắt, reshape
image = np.asarray(image)
image = utils.preprocess(image)
image = np.array([image])
print('*****************************************************')
steering_angle = float(model.predict(image, batch_size=1))
# Tốc độ ta để trong khoảng từ 10 đến 25
global speed_limit
if speed > speed_limit:
speed_limit = MIN_SPEED # giảm tốc độ
else:
speed_limit = MAX_SPEED
throttle = 1.0 - steering_angle**2 - (speed/speed_limit)**2
print('{} {} {}'.format(steering_angle, throttle, speed))
# Gửi lại dữ liệu về góc lái, tốc độ cho phần mềm để ô tô tự lái
send_control(steering_angle, throttle)