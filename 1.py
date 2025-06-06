from PIL import Image

# Список для хранения кадров.
frames = []

for frame_number in range(1, 13):
    # Открываем изображение каждого кадра.
    frame = Image.open(f'FastAPI/{frame_number}.png')
    # Добавляем кадр в список с кадрами.
    frames.append(frame)

# Берем первый кадр и в него добавляем оставшееся кадры.
frames[0].save(
    'FastAPI.gif',
    save_all=True,
    append_images=frames[1:],  # Срез который игнорирует первый кадр.
    optimize=True,
    duration=100,
    loop=0
)