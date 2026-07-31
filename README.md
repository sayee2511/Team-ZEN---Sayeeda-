#  SAKSHAM AI
### Empowering Ability, Enhancing Life through AI-Powered Accessibility

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Streamlit-Web_App-red?style=for-the-badge&logo=streamlit">
  <img src="https://img.shields.io/badge/OpenCV-Computer_Vision-green?style=for-the-badge&logo=opencv">
  <img src="https://img.shields.io/badge/YOLOv8-Object_Detection-purple?style=for-the-badge">
  <img src="https://img.shields.io/badge/TensorFlow-AI-orange?style=for-the-badge&logo=tensorflow">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge">
</p>

---

#  Table of Contents

- Overview
- Problem Statement
- Project Description
- Key Features
- System Architecture
- Workflow
- Technology Stack
- Project Screenshots
- Future Scope
- Demo
- Conclusion

---

#  Overview

*SAKSHAM AI* is an AI-powered accessibility platform designed to empower individuals with visual, hearing, and speech impairments. The system integrates multiple assistive technologies into a single, offline-capable application, enabling users to communicate, access information, and navigate their surroundings independently.

Unlike conventional assistive tools that require multiple applications or constant internet access, *SAKSHAM AI* combines speech recognition, OCR, Indian Sign Language recognition, object detection, and multilingual assistance within one unified platform.

---

# 🎯 Problem Statement

Millions of individuals with *visual, hearing, and speech impairments* encounter daily barriers in communication, information access, and independent living.

Existing assistive technologies are often:

- Fragmented across multiple applications
- Expensive and inaccessible
- Dependent on internet connectivity
- Limited in multilingual support
- Unable to recognize Indian Sign Language effectively

These limitations create a critical need for an integrated, AI-powered assistive solution that promotes *inclusion, independence, and equal access for everyone*.

---

#  Project Description

*SAKSHAM AI* is an *offline, AI-powered assistive companion* that helps individuals with disabilities communicate and perform everyday tasks independently.

The application combines multiple AI technologies into one seamless platform capable of:

- 🤟 Recognizing *Indian Sign Language (ISL)* in real time
- 🎤 Converting speech into text instantly
- 📖 Reading printed documents aloud using OCR
- 👁️ Detecting objects, currency, and obstacles using Computer Vision
- 🌐 Supporting multilingual communication
- 📡 Operating completely *offline*, ensuring accessibility even in low-connectivity regions

The solution is designed with an intuitive Streamlit interface, making advanced AI accessible to everyone.

---

#  Key Features

## 🎤 Voice Assistant

- Speech-to-text conversion
- Text-to-speech responses
- Offline voice interaction
- Real-time communication assistance

---

## 🤟 Indian Sign Language Recognition

- Real-time ISL detection
- Converts signs into readable text
- Enables two-way communication
- AI-powered gesture recognition

---

## 📖 Reading Assistant (OCR)

- Reads books
- Reads printed documents
- Reads labels
- Reads signboards
- Converts printed text into speech

---

## 👁️ Object Detection

- Detects surrounding objects
- Identifies obstacles
- Currency recognition
- Navigation assistance for visually impaired users

---

## 📡 Offline Functionality

Works without an internet connection, making it suitable for:

- Rural areas
- Disaster situations
- Low-connectivity environments

---

#  System Architecture

```mermaid
flowchart LR

    U[👤 User] --> I[Input Sources]

    I --> V[🎤 Voice]
    I --> C[📷 Camera]
    I --> D[📄 Document]

    V --> F[🖥️ Streamlit Frontend]
    C --> F
    D --> F

    F --> B[⚙️ Python Backend]

    B --> M1[🎤 Voice Assistant]
    B --> M2[📖 OCR Module]
    B --> M3[🤟 ISL Recognition]
    B --> M4[👁️ Object Detection]

    M1 --> O[🔊 Accessible Output]
    M2 --> O
    M3 --> O
    M4 --> O

    O --> U
```
---
#  Workflow

```mermaid
flowchart LR

    A[👤 User] --> B[Provide Input]

    B --> C1[🎤 Voice]
    B --> C2[📷 Camera]
    B --> C3[📄 Document]

    C1 --> D[🖥️ Streamlit UI]
    C2 --> D
    C3 --> D

    D --> E[⚙️ Backend Controller]

    E --> F1[Voice Assistant]
    E --> F2[OCR]
    E --> F3[ISL]
    E --> F4[Object Detection]

    F1 --> G[Generate Result]
    F2 --> G
    F3 --> G
    F4 --> G

    G --> H[🔊 Speech Output]
    G --> I[📝 Text Output]

    H --> J[👤 User]
    I --> J
```

#  Technology Stack

| Category | Technologies |
|----------|--------------|
| *Frontend* | Streamlit, HTML, CSS |
| *Backend* | Python |
| *Voice Assistant* | SpeechRecognition, PyAudio, pyttsx3 |
| *Object Detection* | YOLOv8, OpenCV |
| *OCR* | EasyOCR, OpenCV |
| *ISL Recognition* | MediaPipe, TensorFlow / Scikit-learn |
| *Utilities* | NumPy, Pillow |
| *Version Control* | Git, GitHub |

---
## 📸 Project Screenshots

### SAKSHAM-AI - Complete UI Overview

<table>
  <tr>
    <td align="center"><img src="./Images/dash.jpeg" width="245" alt="dashboard"><br><strong>1. Dashboard</strong></td>
    <td align="center"><img src="./Images/voice.jpeg" width="245" alt="voice"><br><strong>2. Voice Assistant</strong></td>
    <td align="center"><img src="./Images/sign.jpeg" width="245" alt="Sign"><br><strong>3. Sign Language</strong></td>
  </tr>
  <tr>
    <td align="center"><img src="./Images/tts.jpeg" width="245" alt="tts"><br><strong>4. Text to Speech</strong></td>
    <td align="center"><img src="./Images/stt.jpeg" width="245" alt="stt"><br><strong>5. Speech to text</strong></td>
    <td align="center"><img src="./Images/ocr.png" width="245" alt="ocr"><br><strong>6. OCR</strong></td>
  </tr>
</table>

<p align="center">
  <em>SAKSHAM AI-Empowering every voice!</em>
</p>


#  Future Scope

- AI-powered emergency SOS system
- GPS-based navigation assistance
- Smart wearable device integration
- Real-time multilingual translation
- Cloud synchronization
- Personalized AI assistant
- Mobile application for Android and iOS
- Healthcare monitoring integration

---
#  Demo Video

<div align="center">

[![Watch Demo](https://img.shields.io/badge/▶%20Watch-Demo%20Video-red?style=for-the-badge)](https://drive.google.com/drive/folders/1k7myL-Og4b4LYcSfsACc1fORWfGhFzzI)

</div>

#  Conclusion

SAKSHAM AI represents a significant step toward creating a more inclusive society by combining multiple accessibility technologies into one intelligent platform.

Its offline capability, multilingual support, and AI-powered assistance make it a practical solution for individuals with disabilities, particularly in rural and underserved communities.

By empowering users with greater independence, improving communication, and enhancing accessibility, *SAKSHAM AI* strives to bridge the gap between technology and inclusivity—ensuring that accessibility is not a privilege but a right for everyone.

---

<div align="center">

## ❤️ Built with passion for an inclusive future

### *SAKSHAM AI*
*Empowering Ability • Enhancing Life*

</div>
