import cv2
import numpy as np


def message_to_binary(message):
	if type(message) == str:
		return ''.join([ format(ord(i), "08b") for i in message ])
	elif type(message) == bytes or type(message) == np.ndarray:
		return [format(i, "08b") for i in message ]
	elif  type(message) == int or type(message) == np.uint8:
		return format(message, "08b")
	else:
		raise TypeError("Input type not supported")



# Function to hide the secret message in the image

def hide_data(image, secret_message):

	# calculate the maximum bytes to encode by (lenght of column * number of rows * r,g,b (number of channels) divide by 8 to represent in bytes)
	n_bytes = image.shape[0] * image.shape[1] * 3 // 8
	print("Maximum bytes to encode:", n_bytes)

	# Check if the number of bytes to encode is les than the maximum bytes in the image
	if len(secret_message) > n_bytes:
		raise ValueEror("Error encountered insufficient bytes, need bigger image or less data !!")

    # you can use any string as the delimeter
	secret_message += "####"


	data_index = 0

	# convert input data to binary format using message_to_binary() function
	binary_secret_msg = message_to_binary(secret_message)

	# Find the length of data that needs to be hidden
	data_len = len(binary_secret_msg)

	for values in image:
		for pixel in values:


		# convert RGB values to binary format
			r = message_to_binary(pixel[0])
			g = message_to_binary(pixel[1])
			b = message_to_binary(pixel[2])

			# modify the least significant bit only if there is still data to store

			if data_index < data_len:
			# hide the data into least significant bit of red pixel
				pixel[0] = int(r[:-1] + binary_secret_msg[data_index],2)
				data_index += 1
			if data_index < data_len:
				# hide the data in the least significant bit of the green pixel
				pixel[1] = int(g[:-1] + binary_secret_msg[data_index],2)
				data_index += 1
			if data_index < data_len:
				# hide the data into least significant bit of the blue pixel
				pixel[2] = int(b[:-1] + binary_secret_msg[data_index],2)
				data_index += 1
			# if data is encoded, just break out of the loop
			if data_index >= data_len:
				break

	return image

# Function to decode hidden message from image

def show_data(image):

	binary_data = ""
	for values in image:
		for pixel in values:
			# convert red, green and blue values into binary format
			r, g, b = message_to_binary(pixel)
			# extracting data from the least significant bit of red pixel
			binary_data += r[-1]
			# extracting data from the least significant bit of green pixel
			binary_data += g[-1]
			# extracting data from the least significant bit of blue pixel
			binary_data += b[-1]

	# split by 8-bits
	all_bytes = [ binary_data[i: i+8] for i in range(0, len(binary_data), 8)]

	# convert from bits to characters
	decoded_data = ""
	for byte in all_bytes:
		decoded_data += chr(int(byte,2))
		# check if we have reached the delimeter which is "#####"
		if decoded_data[-5:] == "#####":
			break

	# return everything except the delimeter
	return decoded_data[:-5]

def encode_text():
    image_name = input("Enter image name(with extension): ")
    image = cv2.imread(image_name) # Read the input image using OpenCV-Python.
  	#It is a library of Python bindings designed to solve computer vision problems.

    #details of the image
    #check the shape of image to calculate the number of bytes in it
    print("The shape of the image is: ",image.shape )
    data = input("Enter data to be encoded : ")
    if (len(data) == 0):
   		raise ValueError('Data is empty')

    filename = input("Enter the name of new encoded image(with extension): ")
     # call the hide_data function to hide the secret message into the selected image
    encoded_image = hide_data(image, data)
    cv2.imwrite(filename, encoded_image)


# Decode the data in the image
def decode_text():
  	# read the image that contains the hidden image
  	image_name = input("Enter the name of the steganographed image that you want to decode (with extension) :")
  	image = cv2.imread(image_name) #read the image using cv2.imread()

  	text = show_data(image)
  	return text



# Image Steganography
def Steganography():
    	a = input("Image Steganography \n 1. Encode the data \n 2. Decode the data \n Your input is: ")
    	userinput = int(a)
    	if (userinput == 1):
      		print("\nEncoding....")
      		encode_text()

    	elif (userinput == 2):
      		print("\nDecoding....")
      		print("Decoded message is " + decode_text())
    	else:
        	raise Exception("Enter correct input")

Steganography() #encode image
