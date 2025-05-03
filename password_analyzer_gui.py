import customtkinter as ctk
import re
import webbrowser

# ----- Password Strength Logic -----
def analyze_password(password):
    feedback = []
    score = 0

    if len(password) >= 8: score += 1
    else: feedback.append("Use at least 8 characters.")
    if re.search(r'[a-z]', password): score += 1
    else: feedback.append("Add lowercase letters.")
    if re.search(r'[A-Z]', password): score += 1
    else: feedback.append("Add uppercase letters.")
    if re.search(r'[0-9]', password): score += 1
    else: feedback.append("Add numbers.")
    if re.search(r'[^a-zA-Z0-9]', password): score += 1
    else: feedback.append("Add special characters.")

    if score == 5: return "Very Strong 💪", "#00D26A", feedback
    if score == 4: return "Strong", "#3498db", feedback
    if score == 3: return "Moderate", "#f39c12", feedback
    if score == 2: return "Weak", "#e67e22", feedback
    return "Very Weak ❌", "#e74c3c", feedback

# ----- Analysis Trigger -----
def on_analyze():
    password = password_entry.get()
    strength, color, feedback = analyze_password(password)
    result_label.configure(text=f"Strength: {strength}", text_color=color)

    feedback_box.configure(state="normal")
    feedback_box.delete("0.0", "end")
    if feedback:
        for tip in feedback:
            feedback_box.insert("end", f"• {tip}\n")
    else:
        feedback_box.insert("end", "Your password is strong! 🎉")
    feedback_box.configure(state="disabled")

# ----- Toggles -----
def toggle_password():
    password_entry.configure(show="" if show_var.get() else "*")

def toggle_theme():
    theme = "light" if ctk.get_appearance_mode() == "Dark" else "dark"
    ctk.set_appearance_mode(theme)

def open_github(event):
    webbrowser.open_new("https://github.com/KiraxD")

# ----- App UI Setup -----
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.geometry("540x540")
app.title("🔐 Password Analyzer - Made by Kira xD")
app.after(100, lambda: app.wm_attributes("-alpha", 1.0))  # Fade effect
app.wm_attributes("-alpha", 0.0)

# ----- Title Section -----
title = ctk.CTkLabel(app, text="Password Analyzer", font=("Segoe UI", 22, "bold"))
title.pack(pady=(20, 4))
ctk.CTkLabel(app, text="Check how secure your password is", font=("Segoe UI", 13)).pack()

# ----- Password Entry -----
password_entry = ctk.CTkEntry(app, placeholder_text="Enter your password", width=300, font=("Segoe UI", 12), show="*")
password_entry.pack(pady=14)
password_entry.bind("<KeyRelease>", lambda e: on_analyze())

# ----- Show Password Toggle -----
show_var = ctk.BooleanVar()
ctk.CTkCheckBox(app, text="Show Password", variable=show_var, command=toggle_password).pack()

# ----- Analyze Button -----
analyze_btn = ctk.CTkButton(app, text="Analyze", command=on_analyze)
analyze_btn.pack(pady=12)

# ----- Result Display -----
result_label = ctk.CTkLabel(app, text="", font=("Segoe UI", 14, "bold"))
result_label.pack(pady=(8, 4))

# ----- Feedback Box -----
ctk.CTkLabel(app, text="Suggestions:", font=("Segoe UI", 12, "underline")).pack(pady=(10, 4))
feedback_box = ctk.CTkTextbox(app, height=100, width=420, font=("Segoe UI", 11), state="disabled")
feedback_box.pack(pady=(0, 10))

# ----- Theme Toggle -----
ctk.CTkButton(app, text="🌗 Toggle Dark/Light Mode", command=toggle_theme).pack(pady=(0, 8))

# ----- Footer -----
footer = ctk.CTkLabel(app, text="Made by Kira xD", font=("Segoe UI", 15, "italic"), cursor="hand2", text_color="#888")
footer.pack(pady=(5, 2))
footer.bind("<Button-1>", open_github)

# ----- Launch with Fade In -----
def fade_in():
    alpha = 0.0
    while alpha < 1.0:
        app.wm_attributes("-alpha", alpha)
        alpha += 0.05
        app.update()
        app.after(25)

fade_in()
app.mainloop()
