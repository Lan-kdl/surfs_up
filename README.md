# surfs_up

## Overview 

The purpose of this project was to give W. Avy more information about the temperature trends in June and Decemeber in Oahu before opening the surfshop. The data was analyzed to determine if the surf and ice-cream shop could be sustainable year round.

[Challenge](https://github.com/Lan-kdl/surfs_up/blob/main/SurfsUp_Challenge.ipynb)

[Data](https://github.com/Lan-kdl/surfs_up/blob/main/hawaii.sqlite)

## Results

![june_temps](https://user-images.githubusercontent.com/95589611/158072817-9256c574-1620-4c58-b73f-d800bffca940.png)
![dec_temps](https://user-images.githubusercontent.com/95589611/158072824-ed6685ef-c3bc-47ea-9a70-c69c339ca2a6.png)

- The average temperatures between June and December are not all that different with only about 4 degrees difference, both means are within a 70-80 degree range. 
- The greatest difference in temperatures between June and December are their minimum temperatures with June having a higher temperature by about 8 degrees; Their maximum temperatures are more similar as they are only different by 2 degrees and both within a 80-85 degree range. 
- The most significant determinate of the risk of business is that June and December have similar standard deviations of 3.26 and 3.75 respectively. This means that June and December have relativley high standard deviations, and therefore high variance in temperature. 

## Summary 

In closing, even though the average temperatures between June and December were not different enough to assume that the surf and ice-cream shop wouldn't be sustainable year round, their standard deviations tell a different story. The high variance of temperatures of June and December indicates that the temperatures within these months are likely to be far away from the average temperatures and eachother. This could pose a substantial risk for the business if the temperatures of December are much colder than the average temperature for a good portion of days; However, it should be noted that a small number of outliers could be contibuting to the high standard deviation. In this case, we can rely on the similarities in average temperatures betweeen the months of June and December which tell us that the surf and ice-cream shop will be sustainable year round. Further queries into the weather of June and December shop be conducted before drawing a confident conclusion.
### Additional queries

To better determine the significance of the high standard deviation in December, we can run a query which counts the total number of temperatures in the month of December which are under the mean temperature of 71 degrees. 

![query_1](https://user-images.githubusercontent.com/95589611/158075016-8366782e-af02-423a-86da-9fa055685c24.png)

From this query, we have found that 630 temperatures are below the average temperature of 71 degrees, meaning that 42% of December temperatures are under 71 degrees. 

We can also run a query which gathers the precipitation data for the months of June and December as rainy whether could drive away potential customers. 

![dec_and_june_prcp_data](https://user-images.githubusercontent.com/95589611/158075105-7b88879e-6951-4298-a6c7-a15e5be062c8.png)

From this query we have gathered the precipitation data for June and December which we will turn into lists and then into DataFrames. 

![dec_prcp_data](https://user-images.githubusercontent.com/95589611/158075134-51db59b1-f230-483c-b86a-2bc3beeb5d86.png)

![june_prcp_data](https://user-images.githubusercontent.com/95589611/158075145-f02e22aa-5f3f-4f51-aa12-a63bfc71142c.png)

Finally, we can create histograms from the precipitation data for the months of June and December to see the trends of rain for each month. 

![dec_prcp_graph](https://user-images.githubusercontent.com/95589611/158075193-ecd1210f-8a4a-4f71-909d-c2eeb47b1dfa.png)

![june_prcp_graph](https://user-images.githubusercontent.com/95589611/158075199-07c59d0b-4d20-4c66-814b-8e9cdda1c229.png)


