# Discussion: Log Ex Pro  

## 📌 Solutions Considered  

### 1️⃣ **Naïve Approach (Line-by-Line Scan)**
- **Method:** Read the log file line by line and check if the date matches the given input.  
- **Pros:** Simple to implement.  
- **Cons:** Extremely slow for a **1TB file**, as it requires scanning the entire file every time.  

### 2️⃣ **Indexing with Preprocessing**  
- **Method:** Create an **index file** mapping each date to its byte offset in the log file.  
- **Pros:**  
  - Speeds up log retrieval by jumping directly to the required date’s section.  
  - Reduces unnecessary file reads.  
- **Cons:** Requires **preprocessing time** to generate the index before the first query.  

### 3️⃣ **Memory Mapping (mmap) for Fast Search**  
- **Method:** Use `mmap` to directly access the file in memory and perform searches efficiently.  
- **Pros:**  
  - Avoids loading the whole file into RAM.  
  - Faster than basic line-by-line reading.  
- **Cons:** May still be slow for very large files without an index.  

---

## ✅ **Final Solution Summary**  
We chose a **hybrid approach** combining **indexing & memory-mapped file access**:  
1. **Indexing Phase:** Preprocess the log file and store byte offsets for each date.  
2. **Query Phase:**  
   - Use the index to directly seek to the required date.  
   - Use `mmap` to read only relevant portions of the file, avoiding unnecessary disk access.  

### **🔹 Why This Approach?**  
✔ Efficient for **1TB+ logs** ✅  
✔ Reduces **I/O operations** ✅  
✔ Faster **log extraction** ✅  

---

## ⚡ **Performance Considerations**  
- **Time Complexity:** `O(1)` lookup + `O(N/D)` reads (where `N` is total lines, `D` is days).  
- **Space Complexity:** `O(D)` (stores only small index file).  

