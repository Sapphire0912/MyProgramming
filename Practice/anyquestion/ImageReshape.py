import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_sample_image
bg = load_sample_image("background.jpg")
# print(bg.shape) # (1080, 1920, 3)

data = bg / 255.0
data = data.reshape(1080 * 1920, 3)

from sklearn.cluster import MiniBatchKMeans
model = MiniBatchKMeans(16)
model.fit(data)
new_color = model.cluster_centers_[model.predict(data)]
new_color = new_color.reshape(bg.shape)
plt.imshow(new_color)
plt.title('Myself Image')
plt.show()