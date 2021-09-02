# Embedded deep learning for autonomous vehicles

<!-- ABOUT THE PROJECT -->
## About The Project

This project focuses on the implementation of optimized Linear and DNN regression models for inter-vehicle distance prediction in a Cooperative Adaptive Cruise Control (CACC) application. It leverages Tensorflow Lite to create optimized models through quantization and pruning for realtime inferencing on Raspberry Pi and On-board Unit (OBU) of Connected Autonomous Vehicles.

Major aspect of the project include:
* The [cacc_application.ipynb](https://github.com/simeonbabatunde/embedded-deep-learning-for-autonomous-vehicles/blob/main/cacc_application.ipynb) file contains the different steps taken to load, clean and noromalize traffic data. This is followed by training, optimizing and conversion of a tensforlow saved model to tensorflow lite model. It finally describes how to export the final .tflite model. 
* The [predict.py](https://github.com/simeonbabatunde/embedded-deep-learning-for-autonomous-vehicles/blob/main/predict.py) script uses TFlite interpreter on the embedded device to predict inter-vehicle distance of the CACC application using six vehicle mobility features. It describes how to Load the trained TFLite model and how to allocate tensors.


### Built With

This project leverages the following frameworks.
* [TensorFlow](https://www.tensorflow.org/)
* [TensorFlow Lite](https://www.tensorflow.org/lite)
* [ns-3 network simulator](https://www.nsnam.org/)


<!-- GETTING STARTED -->
## Getting Started

Access the [cacc_application.ipynb](https://github.com/simeonbabatunde/embedded-deep-learning-for-autonomous-vehicles/blob/main/cacc_application.ipynb) file to train and optimize the TFlite model. Transfer the the TFlite models to a Raspberry Pi or OBU.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Install Python 3.7.3 on the Raspberry Pi/OBU.
* Install [TensorFlow 2.3.0](https://itnext.io/installing-tensorflow-2-3-0-for-raspberry-pi3-4-debian-buster-11447cb31fc4) for Raspberry Pi3+/4.
* Generate mobility training data (with 6 features in this example) on ns-3.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/simeonbabatunde/embedded-deep-learning-for-autonomous-vehicles
   ```
2. Train and export an optimized TFlite model using  [cacc_application.ipynb](https://github.com/simeonbabatunde/embedded-deep-learning-for-autonomous-vehicles/blob/main/cacc_application.ipynb)

3. Copy the TFlite model and [predict.py](https://github.com/simeonbabatunde/embedded-deep-learning-for-autonomous-vehicles/blob/main/predict.py) into a directory on the Raspberry Pi/OBU.
  
4. Run predict.py to initiate inferencing on the edge device.
   ```sh
   chmod+x predict.py
   ./predict.py
   ```

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.


<!-- CONTACT -->
## Contact

Simeon Babatunde - [@simbabatunde](https://twitter.com/your_username) - babatunde.simeon@gmail.com

Project Link: [https://github.com/simeonbabatunde/embedded-deep-learning-for-autonomous-vehicles](https://github.com/simeonbabatunde/embedded-deep-learning-for-autonomous-vehicles)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Basic regression: Predict fuel efficiency](https://www.tensorflow.org/tutorials/keras/regression)
* [Testing TensorFlow Lite models](https://colab.research.google.com/github/frogermcs/TFLite-Tester/blob/master/notebooks/Testing_TFLite_model.ipynb)
* [Installing TensorFlow 2.3.0 for Raspberry Pi3+/4](https://itnext.io/installing-tensorflow-2-3-0-for-raspberry-pi3-4-debian-buster-11447cb31fc4)