# 🚀 Efficient Log Retrieval from Large Files (1TB Optimized)

## 📌 Overview
This project provides a **high-performance Python script** to efficiently extract logs for a specific date from a **1TB+ log file**.  
The script uses **memory-mapped files (`mmap`)** to enable **fast searching without excessive memory usage**.

---

## ⚡ How It Works
✅ **Uses `mmap` (Memory-Mapped Files)** → Super fast log extraction without loading full file into RAM.  
✅ **Reads Line-by-Line** → Handles **1TB+ files** efficiently.  
✅ **Stores Logs in `/output/` Directory** → Each extraction is saved separately.

## 🚀 How to Run
download and put log files in logs folder 


### 1️⃣ **Clone the Repository**
```sh
git clone <your-forked-repo-url>
cd file name 

