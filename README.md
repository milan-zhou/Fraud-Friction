# Fraud Friction

Instructions
If you wish to build the file from scratch, do the following:
  1) Supply custom training data (/w each training point having the format "<FRAUD|LOGIN> <IP>" OR use the default train.txt that was generated with generateFraudTrain.py on sample.txt. 
  2) Run "preprocess.py -f train.txt" on that file. This parallelizes the API calls for the location of each ip address in train.txt
  2) Run "predict.py precomputed.txt <ip address>" to get the score!
  
 Future Considerations
 1) What circumstances may lead to false positives or false negatives when using solely this score? 
If a user is travelling to a country which had numerous FRAUD login attempts, then we would get a false positive. If a hacker spoofed their ip or travelled to the location which the account owner is located, then we may have a false negative.
 
2) What challenges are there with computing distances based on latitude/longitude? 
"Crows flies" distance is not the perfect metric because it doesn't take into account how difficult it is to get to a location. For example, two large cities in US and Europe, may have a large distance in terms of latitude/longitude. However, if someone travels frequently and there are many flights between those two cities, then the "distance" score should not actually be as great as the latitude/longitude makes it out to be. One future consideration is to consider minimum travel time between two locations instead of the crows flies distance.
