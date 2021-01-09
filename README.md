# 🎯 FlightVision
> Serious bar sports. With seriously accurate XY coordinates.  

A realtime solution to track dart targets with `fastai` and `unets`, using segmentations layers rather than classical regression. 

<p align="center">
  <img src="https://github.com/lukexyz/FlightVision/blob/master/media/tracker_shot_hq.gif"> 
</p>

 :bookmark_tabs: [FlightVision_Unet_c950.ipynb.ipynb](https://github.com/lukexyz/FlightVision/blob/master/nbs/16fastai2_FlightVision_Unet_c950.ipynb)

## Background
Flight Club is a modernised [social darts experience](https://flightclubdarts.com/london/our-story). It has become a popular franchise around London where it's main selling point is a gamified and automated scoring system. It has an effective and near invisible 3D vision system of cameras placed around the dart board, and also includes a well-polished interface which runs on a screen above the board. This opens the traditional game up for improved entertainment with the inclusion of minigames like team elimination, or a snakes-and-ladders adaption – where the target of your dart throw is how far forward you move on the board. 

As of 2020 it has expanded into 3 locations in the UK and one in Chicago, USA. 

<p align="center">
  <img src="https://github.com/lukexyz/FlightVision/blob/master/media/location.JPG?raw=true" width=70%> 
</p>  

#### How it works

Powered by a "[highly sophisticated 3D vision system](https://www.stemmer-imaging.com/en-gb/applications/imaging-systems-for-sports-tracking/)", the software brute-forces the solution using calibrated cameras positioned in a frame above the dart board. 

> A normal dart impact on the board triggers Flight Club Darts’ specially developed 3D fitting algorithms to identify, recognise and measure the precise position, pose and score of the dart to within a fraction of a millimetre. **The software manipulates three virtual darts through millions of different orientations and angles until it finds what matches where the dart landed on the board.** Using multiple cameras reduces obscuration effects.

A deep learning approach was attempted with a [challenge to PhD students as part of a country-wide university competition](https://www.telegraph.co.uk/connect/small-business/flight-club-innovation-written-into-business-objectives/) around 2014. At that time no solution was found, and so more conventional computer vision techniques were used. 

# Bootleg Flightclub using `fastai` v2

Take your own pictures, find the `x,y` coordinates of the dart point using a unet segmentation layer.

<p align="center">
  <img src="https://github.com/lukexyz/FlightVision/blob/master/media/training_centroid_01.JPG?raw=true" width=70%>
</p>


<p align="center">
  <img src="https://github.com/lukexyz/FlightVision/blob/master/media/training_sofa_01.JPG?raw=true" width=50%>
</p>

<p align="center">
  <img src="https://github.com/lukexyz/FlightVision/blob/master/media/centroid_handhold.JPG?raw=true" width=50%>
</p>


# Development

### 1. What Didn't Work

In [lesson 3](https://nbviewer.jupyter.org/github/fastai/course-v3/blob/master/nbs/dl1/lesson3-head-pose.ipynb) of the fastai deep learning course, it explains how regression can be used within computer vision. Unlike `classification` tasks, which are used to make a categorical predicions (i.e. *cat or dog*), `regression` is used to find a continuous numerical values. This fits for our example, because we are trying to determine the `x, y` pixel locations of the dart point. 

<p align="center">
  <img src="https://github.com/lukexyz/FlightVision/blob/master/media/biwi_regression.JPG?raw=true" width=70%>
</p>

I spent a fair amount of time trying to get this regression based `cnn_learner` working – but it simply failed to converge during training. I was surprised that the model couldn't accurately predict the validation data given the simplicity of some of the samples. For example, the third image down was a picture of a dart, by itself, on a plain background – and it still couldn't make a reasonable prediction.

<p align="center">
  <img src="https://github.com/lukexyz/FlightVision/blob/master/media/regression_training_problems.JPG?raw=true" width=40%>
</p>

I knew something must be wrong either with the training process and architecture, or there was a limitation with the dataset I had created. In order to isolate the problem I generated a new dataset.

### 2. Synthetic Dataset with `Blender`

Using blender I simulated a simplified version of the problem. With this I could determine whether it was my training database that was wrong, or whether it was my ML/Dl approach that was wrong. 

  :bookmark_tabs: [blender_script.py](https://github.com/lukexyz/FlightVision/blob/master/blender/blender.py)

<p align="center">
  <img src="https://github.com/lukexyz/FlightVision/blob/master/media/blender_generation.JPG?raw=true" width=50%>
</p>

<p align="center">
  <img src="https://github.com/lukexyz/FlightVision/blob/master/media/blender_output.JPG?raw=true" width=50%>
</p>





