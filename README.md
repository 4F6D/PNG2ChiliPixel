# **PNG2ChiliPixel – Convert PNG Images to Chili Framework (DirectX) Code**

**Description:**  
PNG2ChiliPixel is a simple Python tool that converts PNG images into text files containing `gfx.PutPixel` commands, ready to be pasted directly into the **Chili Framework** (DirectX).

---

## 🚀 **Features**
- 📊 **PNG to Code:** Converts every pixel of a PNG image into `gfx.PutPixel` commands.  
- 🎯 **Direct Integration:** Seamlessly copy and paste the generated code into the Chili Framework.  
- 🛠️ **Customizable:** Supports various image sizes and color depths.  

---

## 🖥️ **Usage**
1. 📥 **Install Dependencies:**  
   ```bash
   pip install pillow
   ```  
2. 🖼️ **Place Your Image:** Save your PNG image as `input.png`.  
3. ▶️ **Run the Script:**  
   ```bash
   python script.py
   ```  
4. 📄 **Copy the Generated Code:** The `output.txt` file will contain the `gfx.PutPixel` commands.  

---

## 📚 **Example Output**
```cpp
gfx.PutPixel(x + 0, y + 0, 255, 0, 0);
gfx.PutPixel(x + 1, y + 0, 0, 255, 0);
gfx.PutPixel(x + 2, y + 0, 0, 0, 255);
```


---

✨ **Feel free to share feedback or contribute!** 😊
