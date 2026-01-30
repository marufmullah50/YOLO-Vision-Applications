# YOLO Computer Vision Pipeline with Roboflow

This repository demonstrates a complete **computer vision workflow using YOLO**, covering:

* ✅ Image Classification
* ✅ Object Detection
* ✅ Instance Segmentation
* ✅ Object Tracking (Bot Sort)
* ✅ Live Camera Deployment for Real-Time Tracking

All datasets are **sourced, annotated, and managed using Roboflow**, then trained and evaluated using **YOLO models**.

---

## 📌 Project Overview

This project shows how to build end‑to‑end YOLO pipelines for multiple vision tasks using high‑quality datasets from **Roboflow**. The workflow includes dataset annotation, preprocessing, training, evaluation, and inference for real‑world applications.

---

## 🧠 Tasks Covered

### 1️⃣ Image Classification

* Classifies images into predefined categories
* Useful for scene recognition, quality inspection, and category prediction

### 2️⃣ Object Detection

* Detects and localizes multiple objects in an image using bounding boxes
* Outputs: class labels + bounding box coordinates

### 3️⃣ Instance Segmentation

* Extends object detection by predicting pixel‑level masks
* Useful for precise object boundary understanding

### 4️⃣ Object Tracking (ByteTrack)

* Tracks detected objects across video frames
* Uses **ByteTrack** for high‑performance multi‑object tracking
* Assigns consistent IDs to objects over time

---

## 🗂 Dataset Preparation (Roboflow)

All datasets used in this project are handled through **Roboflow**.

### 🔹 Dataset Source

* Datasets are imported from **Roboflow Universe** or uploaded manually

### 🔹 Annotation

* Images are annotated using **Roboflow Annotate**
* Supported annotations:

  * Classification labels
  * Bounding boxes (Object Detection)
  * Segmentation masks (Instance Segmentation)

### 🔹 Preprocessing & Augmentation

* Auto‑resize to YOLO format
* Data augmentation such as:

  * Flip
  * Rotation
  * Brightness/contrast adjustment

### 🔹 Export Format

* Exported in **YOLO format** compatible with:

  * YOLOv11 / YOLOv26

---

## 📁 Dataset Structur for Detection and segmentation (YOLO)

```text
Dataset_folder/
├── README.dataset.txt
├── README.roboflow.txt
├── data.yaml
│
├── train/
│   ├── images/
│   └── labels/
│
├── valid/
│   ├── images/
│   └── labels/
│
└── test/
    ├── images/
    └── labels/

```

---

---

## 📁 Dataset Structur for classification (YOLO)

```text
Dataset-Classification/
├── train/
│   ├── class_1/
│   │   ├── img001.jpg
│   │   ├── img002.jpg
│   │   └── ...
│   ├── class_2/
│   ├── class_3/
│   └── class_N/
│
├── valid/
│   ├── class_1/
│   ├── class_2/
│   ├── class_3/
│   └── class_N/
│
└── test/
    ├── class_1/
    ├── class_2/
    ├── class_3/
    └── class_N/


```

---

## ⚙️ Training Setup

### 🔹 Environment

* Python 3.x
* Ultralytics YOLO
* PyTorch
* OpenCV

### Realtime detection Environment

* conda create -n facial python=3.12 -y

* conda activate 

* pip install ultralytics

### 🔹 Example Training Commands

#### Classification

```bash
yolo classify train model=yolov11n-cls.pt data=dataset epochs=50
```

#### Object Detection

```bash
yolo detect train model=yolov11n.pt data=data.yaml epochs=50
```

#### Segmentation

```bash
yolo segment train model=yolov11n-seg.pt data=data.yaml epochs=50
```

---

## 🎥 Object Tracking with ByteTrack

ByteTrack is used for real‑time multi‑object tracking.

### 🔹 Detection + Tracking

```bash
yolo track model=yolov8n.pt source=video.mp4 tracker=bytetrack.yaml
```

### 🔹 Key Features

* High accuracy
* Robust ID assignment
* Works well with crowded scenes

---

## 📊 Results & Evaluation

* mAP, precision, recall for detection & segmentation
* Accuracy for classification
* Visual inspection of tracking IDs across frames

---

## 🚀 Applications

* Surveillance and monitoring
* Autonomous systems
* Industrial inspection
* Sports analytics
* Smart agriculture

---

## 🧩 Tools & Technologies

* YOLO (Ultralytics)
* Roboflow (Annotation & Dataset Management)
* ByteTrack
* Python, PyTorch, OpenCV

---

## 📌 Acknowledgements

* **Roboflow** for dataset hosting, annotation, and augmentation
* **Ultralytics** for YOLO implementation
* **ByteTrack** for efficient multi‑object tracking
* **Tutorials followed to learn:**https://www.youtube.com/playlist?list=PLkz_y24mlSJad5ywmU2gy81LrsX5iNZXG

---

## 📄 License

This project is for educational and research purposes.

---

## ⭐ If you find this useful

Consider starring ⭐ the repository and sharing feedback!
