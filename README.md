# Containerized Flask App to Classify a Bank Note Deployed in AWS Elastic Container Service

- This project is involves containerized a machine learning model trained on bank note data to classify a bank note based on features related to the quality of the bank note. The classification algorithim will tell us if the bank not is likely to be genuine or fake. The classification model has been saved as a pickle file which the flask_app.py script uses for inference.

- To make the application user friendly, a Swagger API has been employed. The application was built in AWS Cloud9 and containerized with Docker. The Docker image was pushed to AWS Elastic Container Registry after with it was deployed with AWS Elastic Container Service. 

- The application can be accessed via load balancer via the following DNS address. 

- http://flask-app-643981862.us-east-2.elb.amazonaws.com/apidocs/

- Since the cost of upgrading of AWS EC@ storage to 20GB to host the container image of the application is high, I will not be able to keep this application running for a long period. 


## Demo Video

The link to the demonstration can be found here:

![Demo Video](https://www.youtube.com/watch?v=2ozDPSCJGxo)
