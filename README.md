# Fit Fusion

Fit_Fusion is a computer vision-based fitness application that tracks body movements to monitor exercise form and count repetitions. It analyzes joint angles using real-time video input to ensure accuracy in exercise tracking.

Built for Bajaj Finserv - FlexItOut.

Team Members : Shubham , Ushnish , Arnab , Arnav

## Features
- **Real-Time Exercise Monitoring**: Tracks body posture using key points.
- **Automatic Repetition Counting**: Detects correct form and counts valid reps.
- **Supports Multiple Exercises**: Push-ups, squats, and hammer curls.
- **Interactive Feedback**: Provides real-time visual guidance.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/cruz724/Fit_Fusion.git
   cd Fit_Fusion
   ```
2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Application:**
   ```bash
   python server.py
   ```
   Access the app at `http://localhost:5000`.

## Exercise Logic

### 1. Push-Up
**Key Points:** Shoulder (S), Elbow (E), Wrist (W)  
**Angle Calculation:**  
θ = cos⁻¹ [(SE ⋅ EW) / (|SE| ⋅ |EW|)]  
**Conditions:**
- Up Position: θ ≥ 145°
- Down Position: θ ≤ 75°
- Valid Rep: Transition from **Up → Down → Up**

### 2. Squat
**Key Points:** Hip (H), Knee (K), Ankle (A)  
**Angle Calculation:**  
θ = cos⁻¹ [(HK ⋅ KA) / (|HK| ⋅ |KA|)]  
**Conditions:**
- Standing Position: θ ≥ 170°
- Squat Position: θ ≤ 90°
- Valid Rep: Transition from **Up → Down → Up**

### 3. Hammer Curl
**Key Points:** Shoulder (S), Elbow (E), Wrist (W)  
**Angle Calculation:**  
θ = cos⁻¹ [(SE ⋅ EW) / (|SE| ⋅ |EW|)]  
**Conditions:**
- Rest Position: θ ≥ 150°
- Curl Position: θ ≤ 50°
- Valid Rep: Transition from **Rest → Curl → Rest**


## Contributing
1. **Fork the Repository**
2. **Create a Branch:**
   ```bash
   git checkout -b feature-name
   ```
3. **Make Changes & Commit:**
   ```bash
   git commit -m "Description of changes"
   ```
4. **Push to Fork & Create Pull Request**

## License
Fit_Fusion is licensed under the MIT License.

