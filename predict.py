#!/usr/bin/env python3

# Author: Simeon Babatunde
# Date : 15 Nov 2020
# Purpose: This script uses TFlite to predicts the inter-vehicle distance of a CACC application using six vehicle mobility features.

# from tflite_runtime.interpreter import Interpreter
import numpy as np
# import argparse


# parser = argparse.ArgumentParser(description='CACC inter-vehicle distance')
# parser.add_argument('--model_path', type=str, help='Specify the tflite model path', required=True)

# args = parser.parse_args()

# model_path = args.model_path 

# Load TFLite model and allocate tensors
interpreter = Interpreter(model_path='cacc_model.tflite')

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Resize input and output tensors to handle input of 6 feature columns
interpreter.resize_tensor_input(input_details[0]['index'], (1, 6))
interpreter.resize_tensor_input(output_details[0]['index'], (1, 1))
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

while True:
	# Read in input features for prediction
	print("Input features")
	features = np.fromstring(input(), dtype='f', sep=',')
	print(features)

	# Point to data and run interpreter
	interpreter.set_tensor(input_details[0]['index'], features)
	interpreter.invoke()
	tflite_results = interpreter.get_tensor(output_details[0]['index'])

	print(tflite_results)

