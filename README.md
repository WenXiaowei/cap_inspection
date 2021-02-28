# cap_inspection: cavity number preprocess
This is the repo used for the project  work in Computer Vision and Image processing.

Cavity number preprocessing:  
1. ### Introduction  
    The student should develop a software program to preprocess an image and get it ready for the OCR of the cavity number of a plastic cap.   
    The cap has an external tab at a fixed position in relation to the caivity number. Find in a picture of the external side of the cap and the image to be preprocessed. 
2. ### First task: Generate a crop of the cavity number  
    The student should:
    - Outline the cap by generating a circle that fits the cap mouth.  
    - Generate a crop containing he cavity number. The crop should contain the cavity number and it should appear upright as in the figure 9.  
    Hint:  Find the annular region (radius > cap radius) which contains the tab; get a binary image where the tab is a white connected component. The centroid of the connected component and the center of the cap mouth are the end-points of a line segment; this segment and a vertical line gives an angle; use this angle to rotate the image in order to put the tab at the top of the image; crop the image.
2. ### Second task: 
    Student should:
    - generate a rectified crop containing the cavity number (figure 10).  Hint: apply a polar transform. 