import tensorflow as tf
mat = tf.constant([
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
], dtype=tf.float32)
# get diagonal of the matrix
diag_mat = tf.diag_part(mat)
x = tf.map_fn(lambda x: x*2, diag_mat)
print(x)
# create matrix with given diagonal
mat = tf.diag([1, 2, 3, 4])
with tf.Session() as sess:
    print(sess.run(x))
    print(sess.run(diag_mat))
    print(sess.run(mat))
