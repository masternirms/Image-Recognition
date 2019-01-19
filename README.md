# KNN Facial Recognition
A user-friendly implementation of Adam Geitgey's Facial Recognition Python library that allows the user to train a model on facial data using the K-Nearest Neighbour algorithm and then predict the different faces in photos you feed to the program.

# Requirements
- Python 3.3+
- dlib
- Face Recognition 1.2.3
- Pillow 5.4.1
- Scikit Learn 0.20.2

# Installation Instructions
Make sure you have both Python and dlib installed on your laptop:
- [Installing dlib on macOS or Ubuntu](https://gist.github.com/ageitgey/629d75c1baac34dfa5ca2a1928a7aeaf)
- [Installing dlib on Windows](https://github.com/ageitgey/face_recognition/issues/175#issue-257710508)

This program is meant to be run on macOS or Linux and running it on Windows may take longer to set up.

After this, you can installed the required libraries using the requirements.txt file provided:
```bash
pip3 install -r requirements.txt
```

# Usage
To run the program, enter the following command in your terminal:
```bash
Python3 KNNClassifier.py
```

# Directory Layout
This is how each directory should look like while passing it through the program:
## Training Directory

        <train_directory_path>
        ├── <person1>      
        │   ├── <somename1>.jpeg      
        │   ├── <somename2>.jpeg       
        │   └── ...      
        ├── <person2>        
        │   ├── <somename1>.jpeg        
        │   └── <somename2>.jpeg 
        │   └── ...
        │
        └── ...
        
## Predicting Directory

        <predict_directory_path>
        ├── <photo1>.jpeg      
        ├── <photo2>.jpeg 
        ├── <photo3>.jpeg 
        ├── <photo4>.jpeg       
        ├── <photo5>.jpeg         
        ├── <photo6>.jpeg         
        ├── <photo7>.jpeg  
        └── ...
        
## Retrieve Directory

        <train_directory_path>
        ├── <person1>      
        │   ├── <photo1>.jpeg      
        │   ├── <photo2>.jpeg       
        │   └── ...     
        ├── <person2>        
        │   ├── <photo1>.jpeg        
        │   └── <photo3>.jpeg
        │   └── <photo5>.jpeg
        │   └── <photo6>.jpeg
        │   └── ... 
        │
        └── ... 
        
