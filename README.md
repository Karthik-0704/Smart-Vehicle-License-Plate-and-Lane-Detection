# Smart-Vehicle-License-Plate-and-Lane-Detection

   <h2>1.1 Objectives</h2>
    <p>
        Road lanes are an essential part of driving irrespective of the vehicle and the driver. They are a crucial aspect of traffic rules and regulations, with stringent laws enforced. Due to the risks involved in violations of lane rules, road lanes are important for traffic safety.
    </p>
    <p>
        There are various systems to ensure safety while driving, such as seat belt indicators and red light detectors. Modern cars often come equipped with systems for lane detection and guidance. One such system involves image processing using high-level programming languages like Python. The primary objective of this project is to inform the driver about vehicle projection on the road and lane switching, especially in situations where cameras alone cannot be relied upon.
    </p>
    <p>
        This system can assist beginners in driving vehicles safely and support professional drivers during reverse gear operations. It can also detect different lane types, which convey various traffic rules. In summary, as a safety and smart assistant, lane detection using image processing can help reduce accidents and road risks.
    </p>

  <h2>1.2 Scope</h2>
    <p>
        Lane detection systems used in Advanced Driver Assistance Systems (ADAS) should perform reliably in all environments, considering:
    </p>
    <ul>
        <li>Weather conditions: fog, mist, cloudy, sunny, bright daylight, darkness, and shadows.</li>
        <li>Obstacles: road humps, speed breakers, and other irregularities.</li>
    </ul>
    <p>
        A lot of research is being conducted in this field. Efforts focus on integrating sensors efficiently to minimize computation time and cost while increasing perception accuracy. Additionally, ensuring highly secure ADAS systems to prevent misuse of technology and data theft is critical.
    </p>

  <h2>1.3 Applications</h2>
    <p>
        This system, when combined with appropriate hardware and software, can:
    </p>
    <ul>
        <li>Improve driver intuition and awareness of traffic regulations.</li>
        <li>Precisely detect vehicle projection and road lanes with accuracy.</li>
        <li>Provide promised results even in extreme situations with more features and advantages.</li>
    </ul>
    <p>
        It offers a cost-effective and straightforward solution for lane safety.
    </p>

  <h2>2.1 Design Approach</h2>

  <h3>2.1.1 Block Diagram</h3>
   
   ![image](https://github.com/user-attachments/assets/412de2c7-5d7b-480c-b559-37bb88575a17)
    <p><em>Fig 2.1.4.a: Block Diagram</em></p>


   <h3>2.1.2 Image Capturing and Filtering</h3>
    <p>
        Video frames from a camera module placed at necessary angles are captured at a fast rate for algorithm application. Capturing involves computer vision techniques. Filtering is critical for removing noise and extracting only the essential parts of an image.
    </p>
    <p>
        Filtering techniques include Gaussian blur for minute pixel errors, Canny edge detection for edge processing, and masking for specific regions of interest (ROI). The steps are:
    </p>
    <ul>
        <li>Extract and resize the image for visibility.</li>
        <li>Convert RGB to HSV to filter yellow and white lanes.</li>
        <li>Apply Gaussian blur after gray-scaling.</li>
        <li>Apply Canny edge detection for road detection.</li>
        <li>Perform dilation and erosion to enhance pixel detection.</li>
    </ul>
    
  ![image](https://github.com/user-attachments/assets/9bb49ae3-ee53-4ddf-8eb9-c29e97795c39)
  ![image](https://github.com/user-attachments/assets/d377dcf8-267b-40d7-b916-1ea2ae86aacd)
  ![image](https://github.com/user-attachments/assets/f0119b7e-add7-43b3-b8ff-c04a3e1eda9c)

<p align  = center><em>Fig 2.1.2.a: Color detection, canny edge detection and dilation</em></p>

    

   <p>
        The input video file is sourced from <a href="https://github.com/ysshah95/Lane-Detection-using-MATLAB/tree/master/Input">GitHub</a>.
    </p>

   <h3>2.1.3 Projection Using ROI and Masking</h3>
    <p>
      The final image after filtering now consists of the lanes some amount of noise and outliers. Further filtering can be done for improving detection. Projection is a crucial step in lane detection as it explains the position of the vehicle in the road and the driver can infer the details. This projection also serves for one another purpose – to decide the lane switching or in-lane position. For projection, manually, two lines are drawn based on the camera angle and position in the car and its perspective of the road. This is sufficient to extract the position of car in the lanes and know if the vehicle is switching lanes or travelling inside the lane. Figure 2.1.2.a represents the camera view and manually plotted projection (using lines) in the image.
After filtering, the image consists of lanes with some noise. Projection is critical for determining the vehicle's position on the road. Manually drawn lines based on camera angles are used to identify lane switching or in-lane positions.
    </p>

   ![image](https://github.com/user-attachments/assets/6c6ee541-d79f-49a4-9f3a-e0d29c79884a)
   ![image](https://github.com/user-attachments/assets/5563f67b-fb43-45d2-b84e-cd3381f8e677)
<p align  = center><em>Fig 2.1.2.b: original vs projection defined image</em></p>

    
  <p>
    Projection is represented using lines and is the ROI region of interest for the purpose it serves in lane detection. After projection, the next step involves using the ROI to detect lanes. Detecting lanes revolves around creating masks or cuts from the image and analyzing them. The image is simply split as ‘inside-ROI’ and ‘outside-ROI’. If lanes are found inside the ROI, it simply implies the vehicle has lanes between it. Which means there is a lane-switch. If there are no lanes detected inside the ROI, the exterior is check for lanes and if lanes are present, it is plotted to guide the vehicles path along with the projection. The lane switching and guiding is resolved with these steps. Detecting lanes comes under geometric analysis. Either ways, if lanes are inside ROI or not, they are plotted in the figure to be used for guidance. Lanes inside the ROI are separated from the actual picture by using a mask that captures it from the entire image and similarly for the lanes outside ROI, two masks, one in left and other in right is created and separated to identify lanes in the sides out of ROI. All these information is analyzed for detection and plotting. A polygon is drawn to capture and mask the ROI and the bitwises_AND function is applied on the image and mask to separate the mask out of image.
        ROI is defined using masks to analyze lanes inside and outside the region. A polygon is created to mask the ROI, and the bitwise AND function is applied to separate the mask from the image.
    </p>


   ![image](https://github.com/user-attachments/assets/c17db8c9-ddc7-468e-b925-27080e68ab08)
   ![image](https://github.com/user-attachments/assets/299a6ecf-6ef4-41a1-99ae-ba9e2735ecab)
   ![image](https://github.com/user-attachments/assets/0eb94822-2e3e-4e1b-9c68-4f92f8ce94d4)

  <p align  = center><em>Fig 2.1.2.c: left mask, right mask and inside ROI</em></p>

   
  <h3>2.1.4 Hough Transform and Warp Perspective</h3>
    <p>
      After the masking and detecting the position of vehicle w.r.t lane, the lanes should be plotted for guiding the vehicle. For detecting and plotting lanes, Hough line transforms are used. This algorithm is present in computer vision package of python. It detects the presence of lines in the image by accounting the pixel positions in the image and parametric model of line (slope-distance model). It processes each pixel and based on the threshold inputs, lines are detected and their coordinates are returned which is plotted. Figure below represents the Hough lines applied to the image.
        Hough line transforms are applied to detect lanes. This algorithm detects lines in an image by analyzing pixel positions and parametric line models (slope-distance). The detected lanes and vehicle positions are plotted. The warp perspective technique is used to convert the image to a bird's-eye view, offering a clearer understanding of the road and lanes.
    </p>

  ![image](https://github.com/user-attachments/assets/ac171f30-ee42-42c0-bbce-1936f32d6b1d)
 <p align  = center><em>Fig 2.1.3.a: image applied with Hough line transforms</em></p>

 <p>The detected lanes, lane-switching or in-lane, along with the ROI/ projection is displayed. Next step is the warp perspective which is an additional processing that converts the image to birds-eye perspective. This can be displayed along with the primary image to understand the road nature and lanes more clearly. The previous steps and processes can be applied to this to make the system provide more information and advantages.</p>

 ![image](https://github.com/user-attachments/assets/3059077b-1b5d-49cc-a27a-b15262a0cfe3)
![image](https://github.com/user-attachments/assets/e95e12ee-810e-4463-a2e0-940b7a419433)
![image](https://github.com/user-attachments/assets/37c858a2-6110-4190-b259-4fa471064ef3)
<p align  = center><em>Fig 2.1.3.b: Bird’s view, yellow filter, and final image with yellow lane detection</em></p>

  <h2>2.2 Proposed System</h2>
    <h3>2.2.1 Image Frame Extraction Video Capture Object</h3>
    <ol>
        <li>Create a video capture object and extract frames using a loop.</li>
        <li>Resize the image.</li>
    </ol>

   <h3>2.2.2 Filtering</h3>
    <ol>
        <li>Apply RGB to HSV conversion and filter yellow and white regions.</li>
        <li>Use Gaussian blur and Canny edge detection.</li>
        <li>Perform dilation and erosion for better pixel detection.</li>
        <li>Plot the projection or ROI using lines.</li>
    </ol>

   <h3>2.2.3 Masking and Detection</h3>
    <ol>
        <li>Create a polygon mask for the ROI.</li>
        <li>Apply AND operation to extract masks for the left, right, and center regions.</li>
        <li>Apply Hough transforms to the masks.</li>
        <li>Display detected lanes and relevant messages.</li>
    </ol>

   <h3>2.2.4 Warp Perspective and Yellow Filtering</h3>
    <ol>
        <li>Apply warp transformation to the output and original image.</li>
        <li>Use colorspace conversion to detect and filter yellow lanes.</li>
        <li>Display the final image.</li>
    </ol>

   <h2>2.3 Overview of Software</h2>
    <p>
        Python is a high-level, interpreted language that supports various tools and libraries for image processing, including:
    </p>
    <ul>
        <li><strong>Computer Vision (cv2) Package:</strong> Provides methods for image processing and computer vision applications.</li>
        <li><strong>NumPy Package:</strong> Offers support for large, multi-dimensional arrays and high-level mathematical functions.</li>
    </ul>
    <p>
        More information about Python can be found at <a href="https://www.python.org/">python.org</a>.
    </p>

 <h2>2.4 Software Requirement</h2>
    <p>
        The software used is PyCharm Community Edition 2021.3.2, which provides a simple and effective environment for implementing Python codes. The ease of installing modules aids in algorithm building.
    </p>
</body>
</html>
