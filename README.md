# *AstroNet*
## *Abstract*
The aim of the project is to study the variation of biomass on planet Earth. To achieve this goal, it was assumed to photograph the planet with the infrared camera, identifying the areas with the presence of vegetation through NDVI (Normalized Difference Vegetation Index) processing. To obtain the state and the variation of biomass in a given period of time, a comparison with archive photographs was hypothesized.
Substantially, the software verifies that the space station flies over a sunlit area, taking photographs with a cadence compatible with the memory occupation established by Team AstroPi.

The project foresees the study of the collected photographs, comparing the ndvi value of the biomass areas not covered by clouds with the value of the archive photographs, in order to verify the differences and possible contractions of the areas covered by vegetation.


## *Criticality of the objectives*

In relation to the objectives set, a prerequisite for the comparison on NDVI values, as confirmed by the Astropi team, the archive photos provided by the experiences of previous years are not usable, because taken with different tools, unsuitable filters and the earth was mainly obscured by clouds. 
We will then proceed with the collection of the images which in a next phase will be discarded according to the biomass areas detected. Downstream of the selection, they will be properly compared with archive images of other sensors. In order to make this comparison, parametric corrections will be made for the calculation of the NDVI value, as suggested by the Department of Electrical Engineering and Information Technologies (DIETI) of the University of Naples Federico II, contacted to better understand the management and the evaluation of the NDVI value. Another benefit of the massive collection of images, without any selection before saving, is the availability to offer them for future scientific projects. In this way it will be possible to build up an archive of images taken with updated tools, so as to be able, possibly in a future project, to compare photographs with the same tool


## *Development process*

As described above, the software performs a continuous cycle lasting 180 minutes, as indicated by the Support Team. Inside the cycle, it is checked whether the overflight area is illuminated by the sun. During the test phase, the reliability of the function that verifies this condition was verified, by comparing the data extracted from this with others on the astronomical site, which reports the position of the ISS in real time. In this way it was found that for the function implemented by astroNat the duration of the day is 5 minutes longer than that of the site. For reasons related to the organization of the project, it was not possible to optimize this aspect, and in any case the error committed by the implemented functionality is considered acceptable. Once the position has been verified, the photograph is taken and the CSV file for the collection of information related to the position is updated: longitude, latitude and altitude. To create this software we proceeded by successive approximations, so as to be able to find a balance between the waiting time for shooting and the maximum amount of usable space.


## *Code structure*
The software was structured in modules. The main function is developed in such a way as to import the necessary external modules, and the utils module developed by the astroNet team.
The functions used by main in the main.py file have been implemented in utils.

### *utils.py*
- “**dayNight**”allows you to distinguish day and night, is based on the orbit and skyfield.api library.
- “**capture**”allows the acquisition of the image, saving it in jpg format with the name consisting of the date and time of the acquisition. It includes the addition of data regarding the acquired image to the csv file which collects all the data of the shots, is based on the picamera and time library.
- “**create_csv**”  is the function that creates the csv file and structures the columns, it is based on the csv and path library.
- “**add_csv_data**” is the function that uses capture to add the data of the image acquired into the csv, it is based on the csv library.


### *main.py structure*
The main is the cycle lasting 180 minutes in which all the functions are enclosed, the logic is as follows:
![Diagramma di flusso](https://user-images.githubusercontent.com/74982114/154856678-1769d868-8525-4828-91db-a0860660bd0a.jpg)
In the image above, "add_csv_data" is missing.

## *Built with*

- *[picamera 1.13](https://picamera.readthedocs.io/en/release-1.13/)*
- *[random](https://docs.python.org/3/library/random.html)*
- *[csv](https://docs.python.org/3/library/csv.html)*
- *[orbit](https://orbit-ml.readthedocs.io/en/latest/)*
- *[skyfield](https://rhodesmill.org/skyfield/)*
- *[time](https://docs.python.org/3/library/time.html)*
- *[datetime](https://docs.python.org/3/library/datetime.html#module-datetime)*
- *[pillow](https://pillow.readthedocs.io/en/stable/)*




