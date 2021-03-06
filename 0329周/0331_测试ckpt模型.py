import tensorflow as tf
with tf.Session() as sess:
    saver = tf.train.import_meta_graph('./Model/model-1000.meta')
    saver.restore(sess, tf.train.latest_checkpoint('Model/'))
    graph = tf.get_default_graph()
    x_input = graph.get_tensor_by_name("x_input:0")
    predict = graph.get_tensor_by_name("predict:0")
    print(sess.run([predict],feed_dict={x_input:[[1,2]]}))