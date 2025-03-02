# CODEX_SRMBFHL13
Here are the angles used for detecting different exercises in your code:

### **1. Push-Up**
- **Key Points:** Shoulder, Elbow, Wrist (LEFT SIDE)
- **Angles Used:**
  - **Up Position:** `> (150 - up_tolerance)` → Default: **≥ 145°**
  - **Down Position:** `< (70 + down_tolerance)` → Default: **≤ 75°**
  - **Motion Detection:** Moving from **Up** → **Down** increments the counter.

---

### **2. Squat**
- **Key Points:** Hip, Knee, Ankle (LEFT SIDE)
- **Angles Used:**
  - **Up Position:** `> 170°`
  - **Down Position:** `< 90°`
  - **Motion Detection:** Moving from **Up** → **Down** increments the counter.

---

### **3. Hammer Curl**
- **Key Points:** Shoulder, Elbow, Wrist (BOTH SIDES)
- **Angles Used:**
  - **Up Position:** `> 150°`
  - **Down Position:** `< 50°`
  - **Motion Detection:** Moving from **Up** → **Down** increments the counter for each arm separately.

---

### **Summary of Angles:**
| Exercise     | **Up Position Angle** | **Down Position Angle** |
|-------------|----------------------|----------------------|
| **Push-Up**  | ≥ 145°  | ≤ 75°  |
| **Squat**    | > 170°  | < 90°  |
| **Hammer Curl** | > 150° | < 50° |

Each exercise uses angles to determine motion states and count repetitions based on transitions between the **Up** and **Down** positions. 🚀
