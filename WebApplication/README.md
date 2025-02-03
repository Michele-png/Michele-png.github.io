# JaidPhis Start-Up Prototype

JaidPhis is a start-up developing an AI model capable of analyzing computer camera frames and diagnosing musculoskeletal disorders. The system leverages this information to devise a gamified recovery plan. A prototype was built to validate the B2B business model and was presented to HR directors for feedback. Below is a description of the MVP implementation and its components.

---

## Functional Analysis

The challenge was that no readily available AI model existed for the diagnostic task. To overcome this, a twofold architecture was created. Here’s how it works:

1. **Video Recording**: The corporate client records themselves using their laptop's front camera for one minute.
2. **Uploading the Video**: The client uploads the video to a web application.
3. **Postural Analysis**: The uploaded video is displayed with postural lines overlaid. These lines are derived from a simplified machine learning model using conventional Python libraries.
4. **Feedback**: During the presentation video call, a co-founder visually assesses the HR director's posture and provides feedback via an online form.
5. **Simulating AI Output**: The app simulates the final product by displaying the co-founder's feedback as if it were the output from a multimodal AI model.

---

<div align="center">
<img src="https://github.com/Michele-png/Michele-png.github.io/blob/main/Digital%20Resources/WebAppArchitecture.jpg" alt="Logo" width="500">
</div>


## Technical Implementation

Below, we present the key components of the app code that implements the described prototype.

---

### 1. `associate_app.py` - Feedback Input

This application is responsible for collecting feedback from the cofounder about the HR directors posture as assessed from the call video. The feedback is stored in a Firebase Firestore database.

**Key Features:**
- **Firebase Integration**: The feedback is saved to Firebase Firestore.
- **Streamlit Interface**: Provides a simple user interface for co-founders to submit feedback.

---

### 2. `customer_app.py` -  Analysis and Feedback Output

The  application allows a customer to upload a video, which is then processed for pose estimation using MediaPipe. The application displays the video frames with overlaid pose landmarks and retrieves feedback from Firebase Firestore for the customer after the video processing.

**Key Features:**
- **Video Upload**: The customer uploads a video in formats like `.mp4`, `.avi`, or `.mov`.
- **Pose Estimation**: Uses MediaPipe to detect and draw pose landmarks over the video frames.
- **Feedback Display**: After the video is processed, feedback is retrieved from Firebase Firestore and displayed on the interface.




