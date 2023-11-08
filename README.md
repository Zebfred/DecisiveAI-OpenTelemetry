# OpenTelemetry-DecisiveAI

gh repo clone Zebfred/DecisiveAI-OpenTelemetry

OpenTelemetry Customization
This repository contains customizations to the OpenTelemetry project, allowing you to collect and analyze traces, metrics, and logs for your applications. Please follow the instructions below to set up and run the code. Additionally, we'll address the challenges you may encounter during the setup process.


'Make Start'


This will run your containers 
​

Then
Attach the docker to bash i.e
Docker attach recomendation-server
​
​
​
Challenges
While customizing OpenTelemetry, you may encounter the following challenges:
​

Container Rerouting
One of the challenges you might face is container rerouting. Customizing and redirecting the flow of data within containers can be complex. Ensure that I've correctly configured your containers to collect the data you need and route it to the appropriate destination.
​

Data Dumping to Iceberg
I was facing difficulties in dumping data to Iceberg due to routing issues, ensure that my data routing paths are set up correctly. Review the configuration of my data export options and destination. Consider checking the OpenTelemetry exporter settings to make sure they are directing data to the right location.
​

Direct Docker Pull for OCTL Exporter Container
I was having trouble with the OCTL exporter container being directly pulled from Docker, validate the configuration and dependencies for the OCTL exporter. 