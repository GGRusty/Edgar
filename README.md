Created for a video idea on the edgar api right now it creates 3 dataframes from a us-gaap concept such as NI for a specified company.
It creates a dataframe for annual data that works as intended currently. It also creates a dataframe for quarterly data that still has some missing values. 
I need to figure out a way to generalize filling missing values. Currently have the idea to take the annual data and subtract off the given quarters to get the missing, but
for companies such as apple that have an odd schedule that will not work so I need to create a more general method. 
I'm working on the facts notebook next,  and the will have the submissions one last with a base sheet that explains the basics of each endpoint.
If you have any suggestions or would like to give any ideas/help feel free to email me :)
