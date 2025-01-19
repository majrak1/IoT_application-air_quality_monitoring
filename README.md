# Big Data Project: IoT Application

This project aims to harness the power of IoT to develop an air quality monitoring application that integrates data ingestion, predictive modeling, and data visualization into a cohesive system. By utilizing data from sensors and applying machine learning techniques, the system not only tracks air quality metrics but also forecasts key indicators such as benzene levels and temperature. The inclusion of advanced visualization tools ensures that complex datasets are translated into intuitive and actionable formats, enabling informed decision-making for policymakers, environmental agencies, and the public.

---

There are three main .ipynb files that perform ingestion, preprocessing, predictions and detailed visualization:

- [Preprocessing](./Preprocess/big_data_preprocess.ipynb)
- [Predictions](./Predictions/Predictions.ipynb)
- [Visualization](./Visualization/Visualization.ipynb)

In addition to those, there are also two Flask servers that act as "time simulators" ([processed](./Visualization/server.py) and [predicted](./Visualization/prediction_server.py)) . Those servers are used in the Node-RED flow (see the [json flow](./Visualization/node-red-json-flow.json)) for real time visualization of processed data and for comparison of processed and predicted datasets.

### Created by Maj Rakovec, Titouan Andre, Gauthier Patard