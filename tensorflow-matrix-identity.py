import tensorflow as tf
identity = tf.eye(3, 3)
squares = tf.map_fn(lambda x: x * x+1, identity)

with tf.Session() as sess:
    print(sess.run(identity))
    print(sess.run(squares))
