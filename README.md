# 🧬 Protein Sequence Analyzer

A desktop application built with Python that analyzes protein sequences and provides detailed amino acid composition and classification.

## 📸 Screenshot

![App Screenshot](screenshots/screenshot.png)

## ✨ Features

- 🔬 **Amino Acid Analysis**: Count and percentage of each amino acid
- 📊 **Chemical Classification**: Groups amino acids by properties
  - Hydrophobic (apolar)
  - Hydrophilic (polar uncharged)
  - Positively charged (basic)
  - Negatively charged (acidic)
- ✅ **Input Validation**: Ensures only valid amino acids are processed
- 🎨 **Modern UI**: Clean, professional interface

## 🛠️ Technologies Used

- **Python 3.x**
- **Tkinter** (GUI)
- **Bioinformatics principles**

## 🚀 Installation & Usage

### Prerequisites
- Python 3.7 or higher

### Steps

1. Clone the repository:
```bash
git clone https://github.com/YOUR-USERNAME/protein-analyzer.git
cd protein-analyzer
```

2. Run the application:
```bash
python protein_analyzer.py
```

3. Enter a protein sequence (e.g., `ARNDCEQGHILKMFPSTWYV`) and click **Analyser**

## 📖 How It Works

1. User inputs a protein sequence
2. Application validates the input (only standard 20 amino acids)
3. Calculates:
   - Total length
   - Count of each amino acid
   - Percentage distribution
   - Classification by chemical properties
4. Displays results in an organized format

## 🧪 Example Input
```
AAACCCGGGHHH
```

## 📊 Example Output
```
📊 RÉSULTATS DE L'ANALYSE
============================================================

🔹 Longueur de la chaîne: 12 acides aminés

🔹 Composition en acides aminés:
------------------------------------------------------------
   A:   3 (25.00%)
   C:   3 (25.00%)
   G:   3 (25.00%)
   H:   3 (25.00%)

============================================================
🔹 Classification des acides aminés:
------------------------------------------------------------
   💧 Hydrophobes (apolaires):          6 (50.00%)
   💦 Hydrophiles (polaires):           3 (25.00%)
   ➕ Chargés positivement (basique):   3 (25.00%)
   ➖ Chargés négativement (acide):     0 ( 0.00%)
============================================================
✅ Analyse terminée avec succès!
```

## 🎯 Future Improvements

- [ ] Export results to CSV/PDF
- [ ] Support for protein sequence file upload (FASTA format)
- [ ] Graphical visualization (pie charts, bar graphs)
- [ ] Hydrophobicity plot
- [ ] Molecular weight calculation



- LinkedIn: [(https://linkedin.com/in/your-profile)](https://www.linkedin.com/in/younes-naaniaa-71bb46316/)
- GitHub:[(https://github.com/YourUsername)](https://github.com/Uounes01)

## 📄 License

This project is open source and available under the [MIT License]


- Built as my first Python project
- Inspired by bioinformatics and computational biology

---

⭐ If you find this project useful, please consider giving it a star!
```

# No external dependencies required
# Python standard library only (tkinter comes pre-installed)