# FlightVision
> Precision dart coordinates for serious bar sports.

A realtime solution to track `(x,z)` coordinates with `fastai` and `unets` using segmentations layers, rather than classical regression. 

<p align="center">
  <img src="https://github.com/lukexyz/FlightVision/blob/master/media/tracker_shot_hq.gif"> 
</p>

# Existing Solution  

### Booking Experience 

* Call the location, booking lead time `4-5 months `
* Table service, imported beer `£5.80` (330ml bottle)  

<p align="center">
  <img src="https://github.com/lukexyz/FlightVision/blob/master/media/location.JPG?raw=true"> 
</p>  


# Bootleg Method via `fastai` v2
> Why go out with your friends, when you can recreate it at home and have 35% of the fun by youself? 

Take your own pictures, find the `x,y` coordinates of the dart point using a bastardized unet segmentation layer.

<p align="center">
  <img src="https://github.com/lukexyz/FlightVision/blob/master/media/training_centroid_01.JPG?raw=true" width=50%>
</p>


<p align="center">
  <img src="https://github.com/lukexyz/FlightVision/blob/master/media/training_sofa_01.JPG?raw=true" width=50%>
</p>

<p align="center">
  <img src="https://github.com/lukexyz/FlightVision/blob/master/media/centroid_handhold.JPG?raw=true" width=50%>
</p>


# Secret Training method

The real dataset I built (300 pictures of me holding a dart) simply wasn't training. I new something must be wrong with my training pipelines - beacuse conceptually the CNN only needs to identify a couply of lines and the dart tip (!) so I was deeply suspicious and confused when the regression model wouldn't converge on anything near the correct coordinates.  

Using blender I simulated a simplified version of the problem. With this I could determin whether it was my training database that was wrong, or whether it was my ML/Dl approach that was wrong. 

<p align="center">
  <img src="https://github.com/lukexyz/FlightVision/blob/master/media/blender_generation.JPG?raw=true" width=50%>
</p>

<p align="center">
  <img src="https://github.com/lukexyz/FlightVision/blob/master/media/blender_output.JPG?raw=true" width=50%>
</p>





