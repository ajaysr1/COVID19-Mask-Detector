# Multi-Task Cascaded Convolutional Neural Networks (MTCNN)
MTCNN is a combined CNN model and it has three stages - P-Net, R-Net, and O-net. This model deals with face area detection and facial feature detection. It is used to get facial landmarks, bounding box of the face, and the score (confidence on bounding box).

## Stages of MTCNN
Firsty, MTCNN takes the images and resize it to different scales so as to create an image pyramid which is then used as the input for the three stages.

<p align="center">
  <img src = "https://miro.medium.com/max/875/1*dQsF84De415OSLDSormZwQ.png" width="50%">
</p>

* <b> The Proposal Network (P-Net) </b> <br/>
P-Net is a FCN (dense layer absent). It extracts the initial facial features to decide the bounding box using regression. Bounding Box Regression is a popular method to locate faces. This layer outputs candidates for bounding box based on the basic features extracted. Further, it uses NMS to optimize the results.

<p align="center">
  <img src = "https://miro.medium.com/max/875/1*6xkYymO5qetLLjUt0MYJXg.jpeg" width="50%">
</p>

* <b> The Refine Network (R-Net) </b> <br/>
R-Net is CNN (dense layer present). The output from P-Net are fed in R-Net. R-Net further adds a 128 FCN to extract more features than P-Net. It further reduces the number of candidates of bounding box using stricter rules. R-net optimizes the output result with Bounding-Box Regression and NMS as well.

<p align="center">
  <img src = "https://miro.medium.com/max/875/1*PoMst7LfCfRSADzSFHXIJg.jpeg" width="50%">
</p>

* <b> The Output Network (O-Net) </b> <br/>
This is also a CNN, similar to R-Net. The output from R-Net is fed in O-Net. This optimizes the data in more detail and outputs three things - Bounding Box Coordinates, Five Facial Features, and Confidence.

<p align="center">
  <img src = "https://miro.medium.com/max/875/1*GEHEFApb0VF9poTIh1Bmng.jpeg" width="70%">
</p>

## Training Method
* <b> Face Classification </b> <br/>
It is a binary classification problem, and it uses cross-entropy loss function.

<p align="center"> <b>
  𝐿<sub>𝑖</sub><sup>𝑑𝑒𝑡</sup> = − (𝑦<sub>𝑖</sub><sup>𝑑𝑒𝑡</sup>𝑙𝑜𝑔(𝑝<sub>i</sub>) + (1 − 𝑦<sub>𝑖</sub><sup>𝑑𝑒𝑡</sup>)(1 − 𝑙𝑜𝑔(𝑝<sub>i</sub>))) </b>
</p> <br/>
𝑝<sub>i</sub> = probability that the face predicted by MTCNN is actually a face <br/>
𝑦<sub>𝑖</sub><sup>𝑑𝑒𝑡</sup> = ground truth. It is either 0 or 1. <br/> <br/>

* <b> Bounding Box Regression </b> <br/>
This is a regression problem problem. The loss function used is square loss function.

<p align="center"> <b>
  𝐿<sub>𝑖</sub><sup>𝑏𝑜𝑥</sup> = ||𝑦<sub>𝑖</sub><sup>^𝑏𝑜𝑥</sup> − 𝑦<sub>𝑖</sub><sup>𝑏𝑜𝑥</sup>||<sup>2</sup> </b>
  </p> <br/>
𝑦<sub>𝑖</sub><sup>^𝑏𝑜𝑥</sup> = predicted output. <br/>
𝑦<sub>𝑖</sub><sup>𝑏𝑜𝑥</sup> = ground truth. <br/> <br/>

* <b> Face Landmark Detection </b> <br/>
It is similar to Bounding Box Regression problem. The loss function used is square loss function.

<p align="center"> <b>
  𝐿<sub>𝑖</sub><sup>𝑙𝑎𝑛𝑑𝑚𝑎𝑟𝑘</sup> = ||𝑦<sub>𝑖</sub><sup>^𝑙𝑎𝑛𝑑𝑚𝑎𝑟𝑘</sup> − 𝑦<sub>𝑖</sub><sup>𝑙𝑎𝑛𝑑𝑚𝑎𝑟𝑘</sup>||<sup>2</sup> </b>
</p> <br/>
𝑦<sub>𝑖</sub><sup>^𝑙𝑎𝑛𝑑𝑚𝑎𝑟𝑘</sup> = predicted output. <br/>
𝑦<sub>𝑖</sub><sup>𝑙𝑎𝑛𝑑𝑚𝑎𝑟𝑘</sup> = ground truth. <br/> <br/>

* <b> Non-Maximum Suppression (NMS) </b>
While extracting bounding boxes, there are many cases when they overlap with each other. NMS is method to get rid of those redundant boxes.
