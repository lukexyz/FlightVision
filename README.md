# 🎯 FlightVision
> Serious bar sports. With seriously accurate XY coordinates.  

A realtime solution to track dart targets with `fastai` and `unets`, using segmentations layers rather than classical regression. 

<p align="center">
  <img src="https://github.com/lukexyz/FlightVision/blob/master/media/tracker_shot_hq.gif"> 
</p>


## Existing Solution  
FlightClub is a modernised [social darts experience](https://flightclubdarts.com/london/our-story), similar to bowling or mini-golf. It has become a popular franchise around London where it's main selling point is a automated and gamified scoring system. It has an effective and near invisible 3D vision system of cameras placed around the dart board, and also includes a well-polished interface which runs on a screen above the board. This opens the traditional game up for improved entertainment with the inclusion of minigames like team elimination, or a snakes-and-ladders adaption – where the target of your dart throw is how far forward you move on the board. 

As of 2020 it has expanded into 3 locations in the UK and one in Chicago, USA. 

<p align="center">
  <img src="https://github.com/lukexyz/FlightVision/blob/master/media/location.JPG?raw=true" width=70%> 
</p>  

#### How it works

Powered by a "[highly sophisticated 3D vision system](https://www.stemmer-imaging.com/en-gb/applications/imaging-systems-for-sports-tracking/)", the software brute-forces the solution using calibrated cameras positioned in a near-invisible frame above the dart board. 

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


# Training method

The real dataset I built (300 pictures of me holding a dart) simply wasn't training. I knew something must be wrong with my training pipelines - beacuse conceptually the CNN only needs to identify a couply of lines and the dart tip (!) so I was deeply suspicious and confused when the regression model wouldn't converge on anything near the correct coordinates.  

Using blender I simulated a simplified version of the problem. With this I could determine whether it was my training database that was wrong, or whether it was my ML/Dl approach that was wrong. 

<p align="center">
  <img src="https://github.com/lukexyz/FlightVision/blob/master/media/blender_generation.JPG?raw=true" width=50%>
</p>

<p align="center">
  <img src="https://github.com/lukexyz/FlightVision/blob/master/media/blender_output.JPG?raw=true" width=50%>
</p>





