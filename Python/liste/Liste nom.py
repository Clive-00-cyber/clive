import tkinter as tk
from tkinter import messagebox, filedialog
import random
from reportlab.lib.pagesizes import A4 # type: ignore
from reportlab.pdfgen import canvas # type: ignore
from reportlab.lib.utils import ImageReader # type: ignore
import tempfile
from PIL import Image, ImageDraw, ImageFont # type: ignore
import json
import os
import sys
from datetime import datetime

class NameGridApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Classement Aléatoire des Noms - V2.0")
       
        # Centrer la fenêtre
        self.center_window(800, 700)
       
        # Liste pour stocker les noms
        self.names = []
        self.grid_data = []
       
        # Configuration de l'interface
        self.create_widgets()
       
    def center_window(self, width, height):
        """Centre la fenêtre sur l'écran"""
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.root.geometry(f"{width}x{height}+{x}+{y}")
       
    def create_widgets(self):
        # Cadre principal
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
       
        # Titre
        title_label = tk.Label(main_frame, text="Générateur de Tableaux de Noms",
                              font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
       
        # Cadre pour l'entrée des noms
        input_frame = tk.Frame(main_frame)
        input_frame.pack(fill=tk.X, pady=10)
       
        tk.Label(input_frame, text="Entrez un nom:", font=("Arial", 10)).grid(row=0, column=0)
       
        self.name_entry = tk.Entry(input_frame, width=20, font=("Arial", 10))
        self.name_entry.grid(row=0, column=1, padx=5)
        self.name_entry.bind('<Return>', lambda e: self.add_name())
        self.name_entry.focus_set()
       
        add_btn = tk.Button(input_frame, text="Ajouter", command=self.add_name,
                           bg="#4CAF50", fg="white", font=("Arial", 9))
        add_btn.grid(row=0, column=2, padx=5)
       
        # Boutons de gestion de liste
        list_management_frame = tk.Frame(main_frame)
        list_management_frame.pack(fill=tk.X, pady=5)
       
        save_list_btn = tk.Button(list_management_frame, text="💾 Sauvegarder la liste",
                                 command=self.save_names_list, bg="#2196F3", fg="white", font=("Arial", 9))
        save_list_btn.grid(row=0, column=0, padx=2)
       
        load_list_btn = tk.Button(list_management_frame, text="📂 Charger la liste",
                                 command=self.load_names_list, bg="#FF9800", fg="white", font=("Arial", 9))
        load_list_btn.grid(row=0, column=1, padx=2)
       
        clear_list_btn = tk.Button(list_management_frame, text="🗑️ Vider la liste",
                                  command=self.clear_names_list, bg="#f44336", fg="white", font=("Arial", 9))
        clear_list_btn.grid(row=0, column=2, padx=2)
       
        # Boutons de génération et export
        button_frame = tk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=5)
       
        generate_btn = tk.Button(button_frame, text="🎲 Générer le tableau",
                                command=self.generate_grid, bg="#9C27B0", fg="white", font=("Arial", 10, "bold"))
        generate_btn.grid(row=0, column=0, padx=5)
       
        self.export_btn = tk.Button(button_frame, text="📄 Exporter en PDF",
                                   command=self.export_to_pdf, state=tk.DISABLED,
                                   bg="#607D8B", fg="white", font=("Arial", 10))
        self.export_btn.grid(row=0, column=1, padx=5)
       
        # Liste des noms avec scrollbar
        list_frame = tk.Frame(main_frame)
        list_frame.pack(fill=tk.BOTH, expand=True, pady=10)
       
        tk.Label(list_frame, text="Liste des noms:", font=("Arial", 11, "bold")).pack(anchor=tk.W)
       
        # Cadre pour listbox et scrollbar
        listbox_frame = tk.Frame(list_frame)
        listbox_frame.pack(fill=tk.BOTH, expand=True)
       
        scrollbar = tk.Scrollbar(listbox_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
       
        self.names_listbox = tk.Listbox(listbox_frame, width=50, height=12,
                                       yscrollcommand=scrollbar.set, font=("Arial", 10))
        self.names_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.names_listbox.yview)
       
        # Bouton pour supprimer un nom sélectionné
        delete_btn = tk.Button(main_frame, text="❌ Supprimer le nom sélectionné",
                              command=self.delete_selected_name, bg="#ff5252", fg="white", font=("Arial", 9))
        delete_btn.pack(pady=5)
       
        # Cadre pour le tableau
        table_frame = tk.Frame(main_frame)
        table_frame.pack(fill=tk.X, pady=10)
       
        tk.Label(table_frame, text="Tableau généré:", font=("Arial", 11, "bold")).pack(anchor=tk.W)
       
        self.grid_frame = tk.Frame(table_frame, relief=tk.RAISED, borderwidth=1)
        self.grid_frame.pack(fill=tk.X, pady=5)
       
        # Statut
        self.status_var = tk.StringVar()
        self.status_var.set("Prêt - Ajoutez des noms")
        status_label = tk.Label(main_frame, textvariable=self.status_var,
                               relief=tk.SUNKEN, anchor=tk.W, bg="#E0E0E0", font=("Arial", 9))
        status_label.pack(side=tk.BOTTOM, fill=tk.X)
       
    def update_status(self):
        """Met à jour la barre de statut avec le nombre de noms"""
        count = len(self.names)
        status_color = "#4CAF50" if count >= 8 else "#ff9800"
        status_bg = "#C8E6C9" if count >= 8 else "#FFECB3"
       
        self.status_var.set(f"Noms enregistrés: {count} | Minimum requis: 8")
        # Mettre à jour la couleur du statut
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Label) and widget.cget("textvariable") == str(self.status_var):
                widget.config(bg=status_bg)
       
    def add_name(self):
        name = self.name_entry.get().strip()
        if name:
            if name not in self.names:
                self.names.append(name)
                self.names_listbox.insert(tk.END, name)
                self.name_entry.delete(0, tk.END)
                self.update_status()
            else:
                messagebox.showwarning("Doublon", "Ce nom a déjà été ajouté.")
        else:
            messagebox.showwarning("Champ vide", "Veuillez entrer un nom.")
   
    def delete_selected_name(self):
        """Supprime le nom sélectionné dans la listbox"""
        selection = self.names_listbox.curselection()
        if selection:
            index = selection[0]
            name = self.names_listbox.get(index)
            self.names_listbox.delete(index)
            self.names.remove(name)
            self.update_status()
            messagebox.showinfo("Succès", f"Nom '{name}' supprimé.")
        else:
            messagebox.showwarning("Aucune sélection", "Veuillez sélectionner un nom à supprimer.")
   
    def save_names_list(self):
        """Sauvegarde la liste des noms dans un fichier JSON"""
        if not self.names:
            messagebox.showwarning("Liste vide", "Aucun nom à sauvegarder.")
            return
           
        file_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("Fichiers JSON", "*.json"), ("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")],
            title="Sauvegarder la liste des noms"
        )
       
        if file_path:
            try:
                data = {
                    "names": self.names,
                    "count": len(self.names),
                    "saved_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "app_version": "2.0"
                }
               
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=4, ensure_ascii=False)
               
                messagebox.showinfo("Succès", f"Liste sauvegardée!\n{len(self.names)} noms enregistrés")
               
            except Exception as e:
                messagebox.showerror("Erreur", f"Erreur lors de la sauvegarde:\n{str(e)}")
   
    def load_names_list(self):
        """Charge une liste de noms depuis un fichier JSON"""
        file_path = filedialog.askopenfilename(
            filetypes=[("Fichiers JSON", "*.json"), ("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")],
            title="Charger une liste de noms"
        )
       
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
               
                if isinstance(data, dict) and "names" in data:
                    loaded_names = data["names"]
                elif isinstance(data, list):
                    loaded_names = data
                else:
                    messagebox.showerror("Format invalide", "Le fichier ne contient pas une liste de noms valide.")
                    return
               
                choice = messagebox.askyesnocancel(
                    "Charger la liste",
                    f"Le fichier contient {len(loaded_names)} noms.\n\n"
                    f"Voulez-vous:\n"
                    f"- 'Oui' pour ajouter à la liste actuelle\n"
                    f"- 'Non' pour remplacer la liste actuelle\n"
                    f"- 'Annuler' pour ne rien faire"
                )
               
                if choice is None:
                    return
                elif choice:
                    new_names = [name for name in loaded_names if name not in self.names]
                    duplicates = len(loaded_names) - len(new_names)
                   
                    self.names.extend(new_names)
                    self.names_listbox.delete(0, tk.END)
                    for name in self.names:
                        self.names_listbox.insert(tk.END, name)
                   
                    message = f"{len(new_names)} nouveaux noms ajoutés."
                    if duplicates > 0:
                        message += f"\n{duplicates} doublons ignorés."
                   
                else:
                    self.names = loaded_names
                    self.names_listbox.delete(0, tk.END)
                    for name in self.names:
                        self.names_listbox.insert(tk.END, name)
                   
                    message = f"Liste remplacée avec {len(self.names)} noms."
               
                self.update_status()
                messagebox.showinfo("Succès", message)
               
            except json.JSONDecodeError:
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                   
                    loaded_names = [line.strip() for line in lines if line.strip()]
                   
                    choice = messagebox.askyesnocancel(
                        "Charger la liste",
                        f"Le fichier texte contient {len(loaded_names)} noms.\n\n"
                        f"Voulez-vous:\n"
                        f"- 'Oui' pour ajouter à la liste actuelle\n"
                        f"- 'Non' pour remplacer la liste actuelle\n"
                        f"- 'Annuler' pour ne rien faire"
                    )
                   
                    if choice is None:
                        return
                    elif choice:
                        new_names = [name for name in loaded_names if name not in self.names]
                        duplicates = len(loaded_names) - len(new_names)
                       
                        self.names.extend(new_names)
                        self.names_listbox.delete(0, tk.END)
                        for name in self.names:
                            self.names_listbox.insert(tk.END, name)
                       
                        message = f"{len(new_names)} nouveaux noms ajoutés."
                        if duplicates > 0:
                            message += f"\n{duplicates} doublons ignorés."
                    else:
                        self.names = loaded_names
                        self.names_listbox.delete(0, tk.END)
                        for name in self.names:
                            self.names_listbox.insert(tk.END, name)
                       
                        message = f"Liste remplacée avec {len(self.names)} noms."
                   
                    self.update_status()
                    messagebox.showinfo("Succès", message)
                   
                except Exception as e:
                    messagebox.showerror("Erreur", f"Impossible de charger le fichier:\n{str(e)}")
           
            except Exception as e:
                messagebox.showerror("Erreur", f"Erreur lors du chargement:\n{str(e)}")
   
    def clear_names_list(self):
        """Vide complètement la liste des noms"""
        if not self.names:
            messagebox.showinfo("Liste vide", "La liste est déjà vide.")
            return
           
        if messagebox.askyesno("Confirmation", f"Voulez-vous vraiment vider la liste?\n{len(self.names)} noms seront supprimés."):
            self.names.clear()
            self.names_listbox.delete(0, tk.END)
            self.update_status()
            messagebox.showinfo("Succès", "Liste vidée avec succès.")
   
    def generate_grid(self):
        if len(self.names) < 8:
            messagebox.showerror("Erreur", f"Ajoutez au moins 8 noms différents.\nActuellement: {len(self.names)} noms.")
            return
       
        for widget in self.grid_frame.winfo_children():
            widget.destroy()
       
        self.grid_data = []
       
        headers = []
        for col in range(4):
            header_label = tk.Label(self.grid_frame, text=f"Colonne {col+1}",
                    borderwidth=2, relief="solid", width=15, bg="#2196F3", fg="white", font=("Arial", 9, "bold"))
            header_label.grid(row=0, column=col, padx=1, pady=1)
            headers.append(f"Colonne {col+1}")
       
        self.grid_data.append(headers)
       
        available_names = self.names.copy()
        random.shuffle(available_names)
       
        for row in range(8):
            if len(available_names) < 4:
                available_names = self.names.copy()
                random.shuffle(available_names)
           
            line_names = []
            for _ in range(4):
                name = random.choice(available_names)
                available_names.remove(name)
                line_names.append(name)
           
            for col, name in enumerate(line_names):
                bg_color = "#FFFFFF" if row % 2 == 0 else "#F5F5F5"
                tk.Label(self.grid_frame, text=name,
                        borderwidth=1, relief="solid", width=15, bg=bg_color, font=("Arial", 9)).grid(row=row+1, column=col, padx=1, pady=1)
           
            self.grid_data.append(line_names)
       
        self.export_btn.config(state=tk.NORMAL, bg="#4CAF50")
        self.status_var.set(f"✅ Tableau généré avec {len(self.names)} noms | PDF prêt à exporter")
   
    def create_table_image(self):
        width = 600
        height = 400
        cell_width = width // 4
        cell_height = height // 9
       
        image = Image.new('RGB', (width, height), 'white')
        draw = ImageDraw.Draw(image)
       
        try:
            font = ImageFont.truetype("arial.ttf", 12)
            header_font = ImageFont.truetype("arial.ttf", 14)
        except:
            try:
                font = ImageFont.load_default()
                header_font = ImageFont.load_default()
            except:
                font = None
                header_font = None
       
        for row_idx, row_data in enumerate(self.grid_data):
            for col_idx, cell_text in enumerate(row_data):
                x0 = col_idx * cell_width
                y0 = row_idx * cell_height
                x1 = x0 + cell_width
                y1 = y0 + cell_height
               
                draw.rectangle([x0, y0, x1, y1], outline='black')
               
                if row_idx == 0:
                    draw.rectangle([x0+1, y0+1, x1-1, y1-1], fill='#2196F3')
               
                if font and header_font:
                    text_bbox = draw.textbbox((0, 0), cell_text, font=font if row_idx > 0 else header_font)
                    text_width = text_bbox[2] - text_bbox[0]
                    text_height = text_bbox[3] - text_bbox[1]
                   
                    text_x = x0 + (cell_width - text_width) // 2
                    text_y = y0 + (cell_height - text_height) // 2
                   
                    draw.text((text_x, text_y), cell_text, fill='black' if row_idx > 0 else 'white',
                             font=font if row_idx > 0 else header_font)
                else:
                    # Fallback si les polices ne sont pas disponibles
                    text_x = x0 + 10
                    text_y = y0 + 10
                    draw.text((text_x, text_y), cell_text, fill='black' if row_idx > 0 else 'white')
       
        return image
   
    def export_to_pdf(self):
        if not self.grid_data:
            messagebox.showerror("Erreur", "Aucun tableau à exporter. Veuillez d'abord générer un tableau.")
            return
       
        file_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("Fichiers PDF", "*.pdf"), ("Tous les fichiers", "*.*")],
            title="Enregistrer le PDF"
        )
       
        if not file_path:
            return
       
        try:
            c = canvas.Canvas(file_path, pagesize=A4)
            width, height = A4
           
            # Titre
            c.setFont("Helvetica-Bold", 16)
            c.drawString(100, height - 50, "Tableau de Répartition des Noms")
           
            # Date de génération
            c.setFont("Helvetica", 10)
            c.drawString(100, height - 70, f"Généré le : {datetime.now().strftime('%d/%m/%Y à %H:%M')}")
           
            # Image du tableau
            table_image = self.create_table_image()
           
            with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as temp_file:
                temp_path = temp_file.name
                table_image.save(temp_path, 'PNG')
           
            img = ImageReader(temp_path)
            c.drawImage(img, 50, height - 500, width=500, height=300)
           
            # Informations supplémentaires
            c.setFont("Helvetica", 10)
            c.drawString(50, height - 520, f"Total des noms : {len(self.names)}")
            c.drawString(50, height - 540, "Règle : Aucun nom ne se répète sur une même ligne")
           
            # Liste des noms
            if len(self.names) <= 30:
                c.drawString(50, height - 570, "Liste complète des noms:")
                y_position = height - 590
                names_per_line = 5
                for i in range(0, len(self.names), names_per_line):
                    line_names = self.names[i:i+names_per_line]
                    c.drawString(70, y_position, ", ".join(line_names))
                    y_position -= 20
            else:
                c.showPage()
                c.setFont("Helvetica-Bold", 16)
                c.drawString(100, height - 50, "Liste complète des noms")
                c.setFont("Helvetica", 10)
                y_position = height - 80
                for i, name in enumerate(self.names):
                    c.drawString(50, y_position, f"{i+1}. {name}")
                    y_position -= 20
                    if y_position < 50:
                        c.showPage()
                        y_position = height - 50
           
            c.save()
           
            import os
            os.unlink(temp_path)
           
            messagebox.showinfo("Succès", f"PDF exporté avec succès!\n{file_path}")
           
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de l'export PDF:\n{str(e)}")

def main():
    root = tk.Tk()
    app = NameGridApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()