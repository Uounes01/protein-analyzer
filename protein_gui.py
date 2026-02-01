import tkinter as tk
from tkinter import ttk, messagebox

# Create main window
Main_Window = tk.Tk()
Main_Window.title("Analyseur de Protéines")
Main_Window.geometry("800x700")
Main_Window.config(bg="#f0f4f8")
Main_Window.resizable(True, True)  # ✅ NOW YOU CAN RESIZE!
Main_Window.minsize(600, 500)      # ✅ Minimum size to prevent too small

# Color scheme - Modern & Professional
PRIMARY_COLOR = "#2563eb"      # Blue
SECONDARY_COLOR = "#1e40af"    # Dark Blue
SUCCESS_COLOR = "#10b981"      # Green
ERROR_COLOR = "#ef4444"        # Red
BG_COLOR = "#f0f4f8"          # Light Gray
TEXT_COLOR = "#1f2937"        # Dark Gray
WHITE = "#ffffff"

######################################################
# HEADER
######################################################

header_frame = tk.Frame(Main_Window, bg=PRIMARY_COLOR, height=80)
header_frame.pack(fill="x")

title_label = tk.Label(
    header_frame,
    text="🧬 Analyseur de Séquences Protéiques",
    font=("Segoe UI", 20, "bold"),
    bg=PRIMARY_COLOR,
    fg=WHITE,
    pady=20
)
title_label.pack()

######################################################
# INPUT SECTION
######################################################

input_frame = tk.Frame(Main_Window, bg=BG_COLOR, pady=30)
input_frame.pack(fill="x", padx=40)

label1 = tk.Label(
    input_frame,
    text="Séquence protéique:",
    font=("Segoe UI", 12, "bold"),
    bg=BG_COLOR,
    fg=TEXT_COLOR
)
label1.pack(anchor="w")

entry = tk.Entry(
    input_frame,
    width=50,
    font=("Consolas", 12),
    bd=2,
    relief="solid",
    highlightthickness=2,
    highlightcolor=PRIMARY_COLOR,
    highlightbackground="#cbd5e1"
)
entry.pack(pady=10, ipady=8)

# Analyze Button
analyze_button = tk.Button(
    input_frame,
    text="🔬 Analyser",
    font=("Segoe UI", 12, "bold"),
    bg=PRIMARY_COLOR,
    fg=WHITE,
    activebackground=SECONDARY_COLOR,
    activeforeground=WHITE,
    bd=0,
    padx=30,
    pady=12,
    cursor="hand2",
    command=lambda: analyse()
)
analyze_button.pack(pady=10)

######################################################
# RESULTS SECTION
######################################################

results_frame = tk.Frame(Main_Window, bg=WHITE, relief="solid", bd=1)
results_frame.pack(fill="both", expand=True, padx=40, pady=20)

# Scrollable results
canvas = tk.Canvas(results_frame, bg=WHITE, highlightthickness=0)
scrollbar = ttk.Scrollbar(results_frame, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg=WHITE)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True, padx=10, pady=10)
scrollbar.pack(side="right", fill="y")

result_label = tk.Label(
    scrollable_frame,
    text="Les résultats apparaîtront ici...",
    font=("Segoe UI", 11),
    bg=WHITE,
    fg="#6b7280",
    justify="left",
    anchor="nw",
    wraplength=680
)
result_label.pack(padx=20, pady=20, anchor="nw")

######################################################
# FOOTER
######################################################

footer_frame = tk.Frame(Main_Window, bg=BG_COLOR, height=40)
footer_frame.pack(fill="x", side="bottom")

footer_label = tk.Label(
    footer_frame,
    text="Développé pour l'analyse bioinformatique | © 2025",
    font=("Segoe UI", 9),
    bg=BG_COLOR,
    fg="#6b7280"
)
footer_label.pack(pady=10)

######################################################
# ANALYSIS LOGIC
######################################################

acides_aminés = ['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V']

def analyse():
    sequence = entry.get().upper().strip()
    
    # Validation
    if not sequence:
        result_label.config(
            text="⚠️ Veuillez entrer une séquence protéique",
            fg=ERROR_COLOR,
            font=("Segoe UI", 11, "bold")
        )
        return
    
    for i in sequence:
        if i not in acides_aminés:
            result_label.config(
                text=f"❌ Erreur: '{i}' n'est pas un acide aminé valide\n\nAcides aminés autorisés: A, R, N, D, C, Q, E, G, H, I, L, K, M, F, P, S, T, W, Y, V",
                fg=ERROR_COLOR,
                font=("Segoe UI", 11)
            )
            return

    length = len(sequence)
    
    # Build result text with better formatting
    result_text = f"📊 RÉSULTATS DE L'ANALYSE\n{'='*60}\n\n"
    result_text += f"🔹 Longueur de la chaîne: {length} acides aminés\n\n"
    
    # Count amino acids
    result_text += "🔹 Composition en acides aminés:\n"
    result_text += "-" * 60 + "\n"
    
    processed = []
    aa_list = []
    
    for x in sequence:
        if x not in processed:
            count = sequence.count(x)
            percentage = (count / length) * 100
            aa_list.append((x, count, percentage))
            processed.append(x)
    
    # Sort by count (descending)
    aa_list.sort(key=lambda item: item[1], reverse=True)
    
    for aa, count, percentage in aa_list:
        result_text += f"   {aa}: {count:3d} ({percentage:5.2f}%)\n"
    
    # Types analysis
    hydrophobes = sum(1 for x in sequence if x in ['G','A','V','L','I','M','F','W','P'])
    hydrophiles = sum(1 for x in sequence if x in ['S','T','C','Y','N','Q'])
    positifs = sum(1 for x in sequence if x in ['K','R','H'])
    negatifs = sum(1 for x in sequence if x in ['D','E'])
    
    result_text += f"\n{'='*60}\n"
    result_text += "🔹 Classification des acides aminés:\n"
    result_text += "-" * 60 + "\n"
    result_text += f"   💧 Hydrophobes (apolaires):        {hydrophobes:3d} ({hydrophobes/length*100:5.2f}%)\n"
    result_text += f"   💦 Hydrophiles (polaires):         {hydrophiles:3d} ({hydrophiles/length*100:5.2f}%)\n"
    result_text += f"   ➕ Chargés positivement (basique): {positifs:3d} ({positifs/length*100:5.2f}%)\n"
    result_text += f"   ➖ Chargés négativement (acide):   {negatifs:3d} ({negatifs/length*100:5.2f}%)\n"
    result_text += f"\n{'='*60}\n"
    result_text += "✅ Analyse terminée avec succès!"

    result_label.config(
        text=result_text,
        fg=TEXT_COLOR,
        font=("Consolas", 10),
        justify="left"
    )

######################################################
# RUN APPLICATION
######################################################

Main_Window.mainloop()