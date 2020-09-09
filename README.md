# Short Term Loans Database
A database of public information about short term (payday) loan providers in the US.

This repo contains code to gather and store in a MongoDB database information about short term loan providers in the states.

Most company information is gathered by hand - with the exception of store locations. Store locations are gathered by scraping the public data on the sites' store locators.

# Current Capabilities
Right now we can scrape data on about 2,800 of the about 22,000 short term loan facilities in the country. Mostly just addresses & lat/long points.
Some data on APRs and membership in lobbying groups such as [Community Financial Services Association of America](https://en.wikipedia.org/wiki/Community_Financial_Services_Association_of_America) is hand-gathered

# Goals
1. Provide more transparency in an industry that is a bit mysterious. I personally have wanted to see public data on short term loan providers for various school projects and been quite frustrated by the lack of available data.
2. Get an idea of where there are opportunities to improve services for the unbanked or underbanked in America

# Future plans
1. Add more crawlers - starting with the biggest names from 
2. Gather data on services/products by location - this data is available for most, but we aren't scrapping it yet
3. Programmatically update the hand-gathered data
4. Deploy a visualization service for people to interact with - likely to include a map of locations - open to other ideas here

# Some very quick sample visualizations from the data so far

### A map of all the locations in the country
![All over the country](https://github.com/Sars47/loans_db/blob/master/assets/global_markers.png)
### The same locations but as a heat map for easier visualization
![Heatmap of the country](https://github.com/Sars47/loans_db/blob/master/assets/heatmap.png)
### A map of all the locations around Washington, DC
![Image of DC short term loan locations](https://github.com/Sars47/loans_db/blob/master/assets/dc.png)
