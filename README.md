# 🚀 Fit Fusion - AI-Powered Workout Tracker  

**Fit Fusion** is an intelligent workout tracker that uses **computer vision and real-time angle detection** to count exercise repetitions automatically. This project leverages **Flask, SQLite, and GitHub Actions** to provide a seamless user experience.  

![Fitness Banner](https://www.behance.net/gallery/220429653/Fitfusion-A-way-to-change-peoples-personality/modules/1257115985)  

---

## **🔥 Features**
✅ **Automatic Exercise Detection** – Counts reps based on body angles.  
✅ **User Authentication** – Secure login and registration.  
✅ **Real-time Tracking** – Detects movements and stores exercise data.  
✅ **GitHub Actions CI/CD** – Deploy with ease using GitHub Pages.  
✅ **REST API** – Fetch and store user workout data easily.  

---

## **📌 Technologies Used**
- **Backend:** Flask, SQLite3, Python  
- **Frontend:** HTML, CSS, JavaScript (if applicable)  
- **Deployment:** GitHub Actions, GitHub Pages  
- **Security:** Bcrypt.js, CORS  

---

## **📊 Exercise Detection Angles**
| **Exercise**    | **Key Points** | **Up Position** | **Down Position** |
|---------------|--------------|--------------|--------------|
| **Push-Up**   | Shoulder, Elbow, Wrist | ≥ 145° | ≤ 75° |
| **Squat**     | Hip, Knee, Ankle | > 170° | < 90° |
| **Hammer Curl** | Shoulder, Elbow, Wrist | > 150° | < 50° |

📌 **How it Works:**  
- The **camera** detects the user's body position.  
- **AI-driven motion tracking** counts reps automatically.  
- Data is **saved securely** in the SQLite database.  

---

## **🛠 Setup & Installation**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/FlexItOut-Hackathon/CODEX_SRMBFHL13.git
cd CODEX_SRMBFHL13

pip install -r requirements.txt
python server.py

