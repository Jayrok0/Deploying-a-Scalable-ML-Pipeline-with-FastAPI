# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
The model contained in this repo is a Random Forest Classifier trained to predict income level based on demographic and employment data. The model was built in scikit-learn and classifies whether or not the individual will have a salary greater or less than $50K. The training and inference functions for this model are stored in ml/model.py and ml/data.py.
## Intended Use
Primarily for educational purposes as part of the Machine Learning DevOps project, as well as practically predicting financial outcomes given certain demographic data.
## Training Data
Our data is read from the census.csv dataset stored in data/census.csv, with all needed demographic and employment data, split to use 80% of the data for training.
## Evaluation Data
The remaining 20% of data is stored and utilized for testing after training and is not used during the training portion (golden rule). 
## Metrics
Precision: The ratio of correctly predicted positive observations against the total predicted positive observations. 
Recall: The ratio of correctly predicted positive observations to all observations in the class. 
F1 Score: The weighted average of Precision and Recall. 

Metrics from first run:

Precision: 0.7419 | Recall: 0.6384 | F1: 0.6863

## Ethical Considerations
Our dataset contains sensitive demographic features such as race, sex and native-country (nationality). These features could potentially amplify biases present in the training data, leading to distinct performance differences between demographics. Without full understanding of the models limitations, it should not be used for impactful decisions.
## Caveats and Recommendations
Given that the dataset is not a perfect representation of the entire populous, the models performance may vary when different data is provided/trained on. Cross validation or alternative models (such as SVMs or GB models) could perform better. 