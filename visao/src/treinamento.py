import dlib

opcoes = dlib.simple_object_detector_training_options()
opcoes.add_left_right_image_flips = True
opcoes.C = 3

dir_xml = '../resources/xmls/trainX.xml'
dir_svm = '../resources/svms/svmX.svm'

dlib.train_simple_object_detector(dir_xml,
                                  dir_svm,
                                  opcoes)
