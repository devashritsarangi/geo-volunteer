# geo-volunteer
Uses different _simple_ approaches to find volunteers near a certain client. 

## preliminary approaches (blank canvas)
### Approach 1: brute force
<img align="right" src="/assets/bruteForce.png" width="150">
Runs through each and every volunteer in the entire area under consideration and finds the (squared) distance relative to client's coordinates.

- Inefficient and cumbersome, but very simple to implement.
- Becomes very time-consuming when thousands of clients/volunteers are involved.

<br>

### Approach 2: bounding boxes
<img align="right" src="/assets/boundingBox.png" width="150">
Forms a "bounding box" around the particular client of a certain set size of sides and proceeds to find which volunteers fall within that bounding box and calculate their distances to the client.

- Efficiency is better versus the first approach. Simple-ish to implement.
- Time consumed is much less than brute forcing every single point.

<br>

## geographical approaches (actual map)
[WIP] Google Maps/OpenStreetMap integration.

## stack
Basic Python.
