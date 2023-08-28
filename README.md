# Sentiment Analysis Model(using LSTM) with User Interface

## Introduction

Hello! My name is Harsh Gurjar, and I've developed a sentiment analysis model using a Long Short-Term Memory (LSTM) neural network. This model is capable of predicting the sentiment (positive or negative) of a given text. In addition to the model, I've created a user-friendly web interface using HTML and CSS, allowing users to input text and receive sentiment analysis results. The interface restricts input to a maximum of 500 words.

## Sentiment Analysis Model

The sentiment analysis model utilizes LSTM, a type of recurrent neural network (RNN), to understand and analyze the sentiment of text data. LSTMs are particularly effective at capturing sequential patterns, making them well-suited for tasks involving text data.

The model has been trained on a suitable dataset, likely containing examples of both positive and negative sentiments. It has learned to recognize patterns in the text that correlate with different sentiments. This training enables the model to make accurate sentiment predictions when given new input.

## User Interface

To make the sentiment analysis model accessible to users, I've created a user interface using HTML and CSS. The interface provides a user-friendly way for individuals to input text and receive sentiment analysis results in real-time. Some key features of the interface include:

- **Input Text Box**: Users can enter the text they want to analyze in a designated input box.
- **Character Limit**: To ensure efficient processing and prevent abuse, the input is limited to a maximum of 500 words.
- **Analyze Button**: A button that users can click to initiate the sentiment analysis process.
- **Sentiment Result**: Once the analysis is complete, the interface displays the predicted sentiment (positive or negative) of the provided text.
- **Clear Button**: Users can choose to clear the input box and analysis result for a new analysis.

## Repository Contents

The GitHub repository contains the following components:

1. **LSTM Model Code**: This section includes the code for building, training, and evaluating the sentiment analysis LSTM model. It provides details about the model architecture, training process, and performance metrics.

2. **User Interface Files**: This section contains the HTML and CSS files responsible for creating the user interface. These files are used to structure the interface elements, apply styling, and enable user interactions.

3. **README.md**: A comprehensive README file that explains the purpose of the project, provides instructions for setting up and using the model and interface, and offers insights into the design choices and considerations.

4. **Model File**: A Model file in h5 format for using prebuilt model.

## Usage

To use this project:

1. Clone the repository to your local machine.
2. Set up the required dependencies and libraries as specified in the README.
3. Run the sentiment analysis model code to train the model on a suitable dataset.
4. Launch the user interface using the provided HTML and CSS files.
5. Input the text you want to analyze (up to 500 words) and click the "Analyze" button.
6. View the predicted sentiment result on the interface.

## Conclusion

The sentiment analysis LSTM model and user interface project combines the power of deep learning with user accessibility. By allowing users to analyze text sentiment through an easy-to-use interface, this project has the potential to find applications in various fields, such as social media monitoring, customer feedback analysis, and more. Feel free to explore the repository and adapt the code to your needs!

