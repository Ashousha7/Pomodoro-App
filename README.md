# 🍅 Pomodoro Timer (Tkinter GUI)
A simple Pomodoro Timer app built using Python and Tkinter, based on the Pomodoro time management technique. The app cycles between work and break intervals and visually tracks progress using checkmarks.

![image](https://github.com/user-attachments/assets/cb9550de-825a-4df8-884e-883efa31df50)


## 📌 Features

- ✅ Simple and clean GUI using Tkinter  
- ⏱ 25-minute work sessions  
- ☕ 5-minute short breaks  
- 💤 15-minute long breaks after every 4 work sessions  
- ✔️ Checkmarks to indicate completed sessions  
- 🔄 Reset button to start over  
- 🔁 Auto-transitions between sessions  

---

## 🧠 How It Works

This app follows the **Pomodoro Technique**:

- 25 minutes of work  
- 5 minutes of short break  
- After every 4 work sessions: 15-minute long break  

The app uses a repetition counter to track whether the next session should be a work period or a break. It displays a green label during work, pink during short breaks, and red during long breaks.

---

## 🚀 Getting Started

### Requirements

- Python 3.x

### Setup

1. Clone the repository:

```bash
git clone https://github.com/your-username/Pomodoro-App.git
cd pomodoro-timer
```

2.  Make sure tomato.png is in the same directory as main.py.

3.  Run the app.
   
```bash
python pomodoro.py
```


## 📁 Project Structure

```bash
Pomodoro-App/
│
├── tomato.png         # Tomato image used in the UI
├── pomodoro.py        # Main Python script
└── README.md          # This documentation file
```

## 🖼️ Interface Overview

- ⏳ Timer: Displays the countdown.  
- 🍅 Tomato Image: Used for visual appeal.  
- ✅ Checkmarks: Indicate completed work sessions. 
- 🔘 Start/Reset Buttons: Controls to begin or reset the timer.

## 📃 Code Highlights
```bash
start_timer()
# Determines the session type (Work / Short Break / Long Break) based on the reps counter and starts the countdown accordingly.
count_down()
# Handles the countdown logic using window.after(1000, ...) and updates the UI each second. After countdown ends, it starts the next session and updates checkmarks.
reset_time()
# Cancels the ongoing timer, resets all values, and updates the interface back to the initial state.
```

## 🎨 Design Constants

| Constant                         | Description                    |
| -------------------------------- | ------------------------------ |
| `WORK_MIN`                       | 1500 seconds (25 min)          |
| `SHORT_BREAK_MIN`                | 300 seconds (5 min)            |
| `LONG_BREAK_MIN`                 | 900 seconds (15 min)           |
| `YELLOW`, `RED`, `PINK`, `GREEN` | UI theme colors                |
| `FONT_NAME`                      | Font used for text ("Courier") |


## 🛠️ Ideas for Improvement

- Add sound notifications when sessions end.  
- Allow users to configure durations for work and break times.  
- Show statistics (e.g., sessions completed today). 
- Export to a standalone .exe using PyInstaller.

## 📸 Screenshots

![image](https://github.com/user-attachments/assets/b76c8628-6cb8-48dd-b45a-976ece860769)

![image](https://github.com/user-attachments/assets/e89f16fc-6d05-4bd7-b85e-5cb3f2652bd5)

## 📝 License
This project is open-source and available under the MIT License.

## 🙌 Acknowledgments

- Inspired by the Pomodoro Technique.
- Built using Python’s built-in Tkinter librarr.











