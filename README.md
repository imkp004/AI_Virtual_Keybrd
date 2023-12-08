# AI-Virtual-keyboard
Computing is not limited to desktops and laptops; it has found its way into mobile devices like cell phones. In this project, I will create a Virtual keyboard using sensor technology and artificial intelligence. The virtual keyboard should be accessible and functioning with the help of a camera image of a keyboard that will be fetched. For debugging this program, Tensorflow allows me to visualize the construction of the neural network with Tensorboad. The typing will be captured by the web camera, as the camera will capture finger movement which processes these frames to perform the keyboard function such as clicking the alphabets. I will use the Python coding language and OpenCV with mediapipe library which is a library of Python bindings designed to solve computer vision problems. To detect input, Pynput library allows me to control and monitor my input devices such as they keyboard and mouse. This project is based on deep learning for detecting the hands. AI virtual keyboard system is to develop an alternative system to perform and control the keyboard functions.

# Week 1
Setup :

In this week I learned python coding language and downloaded and setup the thing which
I am using to make this project. The project I am creating is virtual keyboard which is
based on artificial intelligence. the theory and development of computer systems able to
perform tasks that normally require human intelligence, such as visual perception, speech
recognition, decision-making, and translation between languages. I am using Pycharm Community 
for my platform which is a cross-platform IDE that provides consistent experience.

Importing Libraries :

This project is based on Image processing and it uses libraries like Dlib, OpenCV and 
other libraries with the help of which we would be able to detect points on face like 
eyes. After detecting eyes V.K.D will calculate the blinks and compare them with the 
standard MOSS codes with the help of blink detection and eye detection we are able to
find out the Character which a person wants to express.

I am using OpenCV which is a great tool for image processing and performing computer 
ision tasks. It is an open-source library that can be used to perform tasks like face
detection, objection tracking, landmark detection, and much more. It supports multiple
languages including python, java C++. Although, for this article, I will be limiting to
python only.

Mediapipe is Google’s open-source framework, used for media processing. It is 
cross-platform, or we can say it is platform friendly. It is run on Android, iOS,
web, and YouTube servers that’s what Cross-platform means, to run everywhere. Every
YouTube video we watch is processed with machine learning models using MediaPipe.

Loading webcam :

In this project, I have used 1280x720 pixel video footage using imutils. This is 
important as some of the laptop’s webcam only provides fixed height and width which
can be very small and not suitable for this project.

# Week 2
Defining the keys : 
 
the keyboard is projected optically on a flat surface and, 
as the user touches the image of a key, the optical device 
detects the stroke and sends it to the computer.
 
Drawing the letter on keyboard : 

To start creating the virtual keyboard, I first created an empty black window.
i call it keyboard and using numpy library I simply created a black image with
the size of 1500 pixels of width and 1000 pixels of height.
Then I can add the keys. Each key is simply a rectangle containing some text.
So I define the sizes and I draw the rectangle. Using two dimensional array this
program it will simply pass the letter and it’s position and run theough a loop so that 
it can appear on the screen while the webcam is on.

# Week 3
Setting and aligning text : 

In this Virtual keyboard I will first set the location of the letter inside a rectangel
box which will apper on the webcam when the program runs. Keyboar setup is numbers on 
the first row letters on the other three rows and in last there will be "Space" key. The
text is going to be plain letters and the colour is black for printing letters.

Calculations : 

I am going to set and calculate the location where it is going to show on the webcam
when the program runs, and the size of the text and the rectangel box which the text is in.

# Week 4
Using landmark points in the hands to detect multiple points of the Hands.

Calculating the Hand ratio using the mid points. 

# Week 5
Using landmark points in the hands to detect multiple points of the Hands.

Calculating the Hand ratio using the mid points. 

# Week 6
Starting the webcam Hand Tracking with Virtual Keyboard. 

Hand landmarks identification - MediaPipe finds the 21 hand landmarks on the cropped image of the hand.

# Week 7
Spring Break

# Week 8
Displaying the letters on keyboard.

Poocessing the hand trakcking with keyboard.

# Week 9
Showing the output and resetting the board.

Creating "Space" key and "Back-Space" key.

# Week 10
Running the program of Camrea, virtual keybaord with hand tracking.

Typing letters in Notpad, Chrome, Word etc.
