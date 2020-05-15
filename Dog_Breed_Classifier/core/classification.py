import os
import time

import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


class Dog_Classifier:

    def __init__(self, image_model):
        self.image_model = image_model
        self.image = image_model.image
        self.model_path = 'Dog_Breed_Classifier/core/models/model.pb'
        self.input_layer_name = 'DecodeJpeg/contents:0'
        self.output_layer_name = 'final_result:0'
        self.num_top_predictions = 1
        self.labels_path = \
            'Dog_Breed_Classifier/core/models/dog_labels.txt'

    def load_image(self, image):
        return tf.io.gfile.GFile(image, 'rb').read()

    def load_labels(self):
        labels = [line.rstrip() for
                  line in tf.io.gfile.GFile(self.labels_path)]
        return labels

    def load_graph(self):
        with tf.io.gfile.GFile(self.model_path, 'rb') as f:
            graph_def = tf.compat.v1.GraphDef()
            graph_def.ParseFromString(f.read())
            tf.import_graph_def(graph_def, name='')

    def get_dog_category(self):
        start = time.time()
        # Set the path of the uploaded file
        image_path = os.path.abspath(self.image.url).replace("/media/",
                                                             "media/")
        # Init the graph
        tf.compat.v1.reset_default_graph()
        # load the graph
        self.load_graph()
        # Open a tf session
        config = tf.compat.v1.ConfigProto()
        config.gpu_options.allow_growth = True
        config.allow_soft_placement = True
        with tf.compat.v1.Session(config=config) as sess:
            # Load the image
            image_data = self.load_image(image_path)
            # Get the softmax tensor from the graph
            softmax_tensor = sess.graph.get_tensor_by_name(
                self.output_layer_name)
            # Get the probabilities of the different categories
            predictions, = sess.run(
                softmax_tensor,
                {self.input_layer_name: image_data})
            # Get the index of the highest probablity
            top_k = predictions.argsort()[-self.num_top_predictions:][::-1]
            # Load the labels/categories
            labels = self.load_labels()
            # Get the category that matches the highest probablity
            predicted_label = labels[top_k[0]]
            # To get the score of the prdicted label
            # score = predictions[node_id]
            # self.image_model.category = json.dumps(predicted_label,
            #                                        ensure_ascii=False)
            processing_time = round(time.time() - start, 2)
            self.image_model.category = predicted_label
            self.image_model.processed = True
            self.image_model.processing_time = \
                '{} secondes'.format(processing_time)
            self.image_model.save()
            # print('Processing time:', end_time - start_time)

            # return predicted_label
