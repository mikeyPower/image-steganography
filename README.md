# image-steganography
Image steganography refers to hiding information i.e. text, images or audio files in another image or video files. The current project aims to use steganography for an image with another image using spatial domain technique. This hidden information can be retrieved only through proper decoding technique.

Current version supports text, bytes and integers will add audio and images later

## Prerequisite

    $ ./install.sh
  
## Run

    $ python3 steganography.py
  
## Output

Encoding

    Image Steganography 
    1. Encode the data 
    2. Decode the data 
    Your input is: 1
    Encoding....
    Enter image name(with extension): cool_dog.png
    The shape of the image is:  (512, 512, 3)
    Enter data to be encoded : top secret
    Enter the name of new encoded image(with extension): cool_dog_v1.png
    Maximum bytes to encode: 98304
    Messaged Encoded
  
Decoding

    Image Steganography 
    1. Encode the data 
    2. Decode the data 
    Your input is: 2
    Decoding....
    Enter the name of the steganographed image that you want to decode (with extension) :cool_dog_v1.png
    Decoded message is top secret
  
