import tensorflow as tf
mat = tf.constant([[2, 3, 4], [5, 6, 7], [8, 9, 10]], dtype=tf.float32)
inv_mat = tf.matrix_inverse(mat)
with tf.Session() as sess:
    print(sess.run(inv_mat))
    print(sess.run(mat))
