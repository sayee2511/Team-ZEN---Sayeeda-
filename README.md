# 🦾 SAKSHAM AI
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

# 📑 Table of Contents

- Overview
- Problem Statement
- Project Description
- Key Features
- System Architecture
- Workflow
- Technology Stack
- Future Scope
- Conclusion

---

# 🌍 Overview

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

# 💡 Project Description

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

# ✨ Key Features

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

## 🌐 Multilingual Support

Supports communication across major Indian languages.

---

## 📡 Offline Functionality

Works without an internet connection, making it suitable for:

- Rural areas
- Disaster situations
- Low-connectivity environments

---

# 🏗️ System Architecture

text
                      USER

                      │

          Voice / Camera / Document

                      │

                      ▼

             STREAMLIT FRONTEND

                      │

                      ▼

        BACKEND CONTROLLER (Python)

        ┌─────────────┼──────────────┐
        │             │              │
        ▼             ▼              ▼
 Voice Module      OCR Module     ISL Module
        │                              │
        └─────────────┬────────────────┘
                      ▼
            Object Detection (YOLOv8)

                      │

                      ▼

             AI PROCESSING ENGINE

                      │

         ┌────────────┼────────────┐
         │            │            │
         ▼            ▼            ▼
   Voice Output   Text Output  Live Camera

                      │

                      ▼

                     USER


---

# ⚙️ Workflow

text
User Input
     │
     ▼
Voice / Camera / Document Upload
     │
     ▼
Streamlit Frontend
     │
     ▼
Backend Controller
     │
     ├── Voice Assistant
     ├── OCR Engine
     ├── ISL Recognition
     └── Object Detection
     │
     ▼
AI Processing Engine
     │
     ▼
Accessible Output
(Text • Speech • Camera Feedback)
     │
     ▼
User


---

# 🛠️ Technology Stack

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

# 🚀 Future Scope

- AI-powered emergency SOS system
- GPS-based navigation assistance
- Smart wearable device integration
- Real-time multilingual translation
- Cloud synchronization
- Personalized AI assistant
- Mobile application for Android and iOS
- Healthcare monitoring integration

---

# 🎯 Conclusion

SAKSHAM AI represents a significant step toward creating a more inclusive society by combining multiple accessibility technologies into one intelligent platform.

Its offline capability, multilingual support, and AI-powered assistance make it a practical solution for individuals with disabilities, particularly in rural and underserved communities.

By empowering users with greater independence, improving communication, and enhancing accessibility, *SAKSHAM AI* strives to bridge the gap between technology and inclusivity—ensuring that accessibility is not a privilege but a right for everyone.

---

<div align="center">

## ❤️ Built with passion for an inclusive future

### *SAKSHAM AI*
*Empowering Ability • Enhancing Life*

</div>
