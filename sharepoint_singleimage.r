#program gets single image from sharepoint server and plots in RGB colors

require(httr)

url <- "https://sharepoint_or_something.company_name.com/dir/dir/dir/username/Shared%20Documents/some_more_directory/20171201.png" # change this too
username <- "change_this"
password <- "change_this"


r <- GET(url, authenticate(username,password,type="any"), verbose())

atmos <- content(r, "parsed")

dim(atmos) # dimensions of an image

library(grid)
grid.raster(atmos) # plot in true colors





