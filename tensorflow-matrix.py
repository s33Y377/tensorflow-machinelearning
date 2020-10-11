# convert matrices to tensor objects
import numpy as np
import tensorflow as tf
# create a 2x2 matrix in various forms
matrix1 = [[1.0, 2.0], [3.0, 40]]
matrix2 = np.array([[1.0, 2.0], [3.0, 40]], dtype=np.float32)
matrix3 = tf.constant([[1.0, 2.0], [3.0, 40]])
print(matrix1)
print(matrix2)
print(matrix3)

tensorForM1 = tf.convert_to_tensor(matrix1, dtype=tf.float32)
tensorForM2 = tf.convert_to_tensor(matrix2, dtype=tf.float32)
tensorForM3 = tf.convert_to_tensor(matrix3, dtype=tf.float32)
with tf.Session() as sess:
    print("Tensorlfow")
    print(sess.run(tensorForM1))
    print(sess.run(tensorForM2))
    print(sess.run(tensorForM3))
