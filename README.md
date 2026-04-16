# geo-volunteer
uses different approaches* to find volunteers near a certain issue report

<sub><sup>*brute force and quadtrees</sub></sup>

## approach 1: brute force
involves having one user at a certain coordinate wrt origin, and various volunteers at coordinates wrt origin.

This program scours through every single volunteer in determining the closest possible volunteer to client.

Very time consuming if we consider in a global scale, but if we limit our bounding area to just a single city it still is very inefficient but gets the job done.

## [WIP] approach 2: bounding boxes / quadtrees
