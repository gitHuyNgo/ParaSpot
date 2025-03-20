# 🚗 ParaSpot

This is a **real-time parking space detection system** that uses OpenCV and Flask to process video footage and detect free and occupied parking spaces. The results are displayed on a web interface with real-time updates.

---

## 📷 Project Preview
ParaSpot Preview
![preview](https://github.com/user-attachments/assets/426cea79-1df7-4e0b-9395-dd8dd714224d)

---

## 🛠 Features
✅ **Real-time Video Processing** – Uses OpenCV to analyze a parking lot video and detect available spaces.  
✅ **Web Interface** – Flask serves a webpage displaying the video stream and real-time parking statistics.  
✅ **Dynamic Updates** – The number of free and occupied parking spaces updates every second.  
✅ **API Integration** – Exposes an API (`/space_count`) that returns parking data in JSON format.  

---

## 🚀 How to Run the Project
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/gitHuyNgo/ParaSpot.git
cd ParaSpot
```
### 2️⃣ Set Up Dependencies
```bash
pip install -r requirements.txt
```
### 3️⃣ Run the Application
```bash
python main.py
```
### 4️⃣ Open the Web App
Go to http://127.0.0.1:5000/ in your browser.

---

## 🔧 Project Structure
```bash
ParaSpot/
│── data/                 # Folder containing video and parking positions
│   ├── parking_position  # Pickled file storing predefined parking positions
│   ├── parking_video.mp4 # Video file of the parking lot
│   ├── parking.png       # Image for marking objects
│   ├── preview.png       # Image for project preview
│── templates/            # HTML templates for the web interface
│   ├── index.html        # Main webpage displaying the video feed
│── LICENSE               # Project license
│── main.py               # Main script (Flask server & video processing)
│── README.md             # Project documentation
│── requirements.txt      # List of dependencies
│── space_picker.py       # Script to define parking positions
```

---

## 🛠 Possible Improvements
🔹 Add multiple camera support for real-world parking lots.  
🔹 Use Deep Learning (YOLO, SSD) for more accurate car detection.  
🔹 Store parking data in a database to analyze trends over time.
