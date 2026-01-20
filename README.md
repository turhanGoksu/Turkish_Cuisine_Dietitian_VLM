# 🥗 Turkish Cuisine Dietitian VLM (Turk-Mutfagi-Diyetisyen)

[![Hugging Face](https://img.shields.io/badge/🤗%20Hugging%20Face-Model%20Card-yellow)](https://huggingface.co/Turhan123/turk-mutfagi-diyetisyen-vlm)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/Python-3.10%2B-green)](https://www.python.org/)

> 🎓 **Academic Project:** This project was developed as a **Senior Design Project (Bitirme Projesi)** at **Fırat University, Department of Software Engineering**.

**Turk-Mutfagi-Diyetisyen-VLM** is a specialized Vision-Language Model (VLM) designed to recognize traditional Turkish foods from images, estimate their nutritional values, and provide dietary advice.

Fine-tuned on **Qwen2-VL-2B-Instruct** using **LoRA (Low-Rank Adaptation)**, this model bridges the gap between general AI and cultural gastronomy.

---

## 🚀 Model & Demo

The trained model weights and inference demo are available on Hugging Face:

👉 **[View Model on Hugging Face](https://huggingface.co/Turhan123/turk-mutfagi-diyetisyen-vlm)**

---

## 📂 Repository Structure

This repository contains the source code for data preparation, fine-tuning, and inference.

```
.
├── data_preparation/
│   ├── rename_images.py        # Standardize image filenames (e.g., mantı_1.jpg)
│   └── generate_dataset.py     # Generate CSV dataset with Q&A pairs
├── Turkish_Cuisine_AI.ipynb    # Main Notebook: Fine-tuning Qwen2-VL with LoRA
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## 🛠️ Installation

To run the code locally or in Google Colab, install the required dependencies:

```bash
git clone https://github.com/your-username/Turkish_Cuisine_Dietitian_VLM.git
cd Turkish_Cuisine_Dietitian_VLM
pip install -r requirements.txt
```

---

## ⚙️ Usage

### 1. Data Preparation

Before training, raw images must be processed into a structured format.

**Step 1:** Place your images in folders named after the food (e.g., `images/manti`, `images/kebab`).

**Step 2:** Run `rename_images.py` to standardize filenames:
```bash
python data_preparation/rename_images.py
```

**Step 3:** Run `generate_dataset.py` to create the `turkish_food_dataset.csv` file:
```bash
python data_preparation/generate_dataset.py
```

### 2. Fine-Tuning (Training)

Open `Turkish_Cuisine_AI.ipynb` in Jupyter Notebook or Google Colab.

- **Hardware:** Trained on NVIDIA A100 (40GB) / Compatible with T4 (16GB) using 4-bit quantization
- **Config:** Adjust `DATASET_PATH` and `OUTPUT_DIR` in the notebook
- **Run:** Execute the cells to start LoRA fine-tuning

### 3. Inference

You can use the trained model directly from Hugging Face without re-training:

```python
from transformers import Qwen2VLForConditionalGeneration, Qwen2VLProcessor
from peft import PeftModel
from PIL import Image

# Load Model
base_model = Qwen2VLForConditionalGeneration.from_pretrained(
    "Qwen/Qwen2-VL-2B-Instruct", 
    device_map="auto", 
    torch_dtype="auto"
)
model = PeftModel.from_pretrained(base_model, "Turhan123/turk-mutfagi-diyetisyen-vlm")
processor = Qwen2VLProcessor.from_pretrained("Qwen/Qwen2-VL-2B-Instruct")

# Inference
image = Image.open("path/to/kebab.jpg")
# ... (See notebook for full inference code)
```

---

## 📊 Methodology & Results

- **Base Model:** Qwen2-VL-2B-Instruct
- **Technique:** Supervised Fine-Tuning (SFT) with LoRA (Rank: 64, Alpha: 128)
- **Dataset:** Custom dataset containing 34+ Turkish food categories
- **Results:** The model successfully distinguishes visually similar foods (e.g., Et Tantuni vs. Tavuk Tantuni) and provides context-aware health advice (e.g., "Contains high sugar, consume moderately")

---

## 🎓 Academic Context

This study was conducted to address the challenge of global VLM models failing to recognize local cultural elements, specifically Turkish cuisine.

- **University:** Fırat University, Faculty of Technology
- **Department:** Software Engineering
- **Course:** Senior Design Project (Bitirme Projesi)
- **Supervisor:** Assoc. Prof. Dr. Özal Yıldırım
- **Student:** Turhan Göksu

---

## 🙏 Acknowledgements & References

This project was built using open-source resources and methodologies. Special thanks to:

### Technical Guide
- **Tutorial:** [Fine-tuning VLM Guide (YouTube)](https://www.youtube.com/watch?v=example) - The methodology for fine-tuning Qwen2-VL in this project was adapted from this guide

### Datasets
- [Turkish Food Dataset](https://www.kaggle.com/datasets/turkishfood)
- [Turkish Cuisine Net](https://www.kaggle.com/datasets/turkishcuisine)

### Academic Papers
- **Qwen2-VL:** Wang et al., "Qwen2-VL: To See the World More Clearly", arXiv:2409.12191
- **LoRA:** Hu et al., "LoRA: Low-Rank Adaptation of Large Language Models", arXiv:2106.09685

---

## 📜 License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.

---
