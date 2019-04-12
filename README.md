# Volume-Rendering
It is a demo of user interactive volume rendering by applying ray casting algoritm in Python. It has not integrated with image rotation function yet. But it has unser interactive Transfer Function. 

Since the goal of this work is to understand the algorithm, the code does not contain any image processing packages such as OpenGL, OpenCV, etc.

To run the code, change the file path in InteractiveDirectVolRendering.py and run this file.


# Example Results
Due to the lack of CT iamge, I used MR image as input. We should notice that MR image is not suitable for volume rendering, but CT image is.

When given a MR 3D iamge, the program produces a histogram of the input image, an interactive transfer function and a result image. From the given results(who have different transfer functions), we can see that the inner organ(brain) is visible, which shows this implementation is working. However, the quality of the result heavily depends on the setting of the Transfer Function, namely the setting of the interactive plot shown as below. In orther words, finding a good transfer function is significant for obtaining a good result. The result can be improved significantly if CT image as the input image.

<img src="https://user-images.githubusercontent.com/47189577/55031022-f2370600-500d-11e9-9c4a-77ddc2e7a2db.png" width="192" height="256"> <img src="https://user-images.githubusercontent.com/47189577/55031036-f5ca8d00-500d-11e9-9c27-3f50382aa52b.png" width="192" height="256"> <img src="https://user-images.githubusercontent.com/47189577/55031041-f95e1400-500d-11e9-9a34-d69b296eb845.png" width="60%" height="60%">
