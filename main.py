import signal
# Este parche es para que Streamlit no de error de "signal"
try:
    signal.signal(signal.SIGINT, signal.SIG_DFL)
except:
    pass

import flet as ft
import os

def main(page: ft.Page):
    page.title = "Calculadora de Masas"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = "adaptive"
    page.padding = 20

    # --- LÓGICA DE CÁLCULO ---
    def calcular(e):
        try:
            # Obtenemos el peso total y los porcentajes
            total = float(txt_peso_total.value)
            p_harina = float(txt_p_harina.value) / 100
            p_agua = float(txt_p_agua.value) / 100
            p_sal = float(txt_p_sal.value) / 100
            p_levadura = float(txt_p_levadura.value) / 100

            # Calculamos la base (divisor)
            base = p_harina + p_agua + p_sal + p_levadura
            
            # Peso de la harina (ingrediente principal)
            harina = total / base
            
            # Resultados finales
            res_harina.value = f"Harina: {harina:.2f} gr"
            res_agua.value = f"Agua: {(harina * p_agua):.2f} gr"
            res_sal.value = f"Sal: {(harina * p_sal):.2f} gr"
            res_levadura.value = f"Levadura: {(harina * p_levadura):.2f} gr"
            
        except ValueError:
            res_harina.value = "Error: Ingresa números válidos"
        
        page.update()

    # --- INTERFAZ ---
    txt_peso_total = ft.TextField(label="Peso total de la masa (gr)", value="1000", keyboard_type=ft.KeyboardType.NUMBER)
    
    # Porcentajes panaderos (Valores por defecto comunes)
    txt_p_harina = ft.TextField(label="% Harina", value="100", keyboard_type=ft.KeyboardType.NUMBER)
    txt_p_agua = ft.TextField(label="% Agua (Hidratación)", value="60", keyboard_type=ft.KeyboardType.NUMBER)
    txt_p_sal = ft.TextField(label="% Sal", value="2", keyboard_type=ft.KeyboardType.NUMBER)
    txt_p_levadura = ft.TextField(label="% Levadura", value="1", keyboard_type=ft.KeyboardType.NUMBER)

    res_harina = ft.Text(size=20, weight="bold", color="blue")
    res_agua = ft.Text(size=18)
    res_sal = ft.Text(size=18)
    res_levadura = ft.Text(size=18)

    page.add(
        ft.Text("Calculadora de Panadería", size=25, weight="bold"),
        ft.Divider(),
        txt_peso_total,
        ft.Row([txt_p_harina, txt_p_agua]),
        ft.Row([txt_p_sal, txt_p_levadura]),
        ft.ElevatedButton("Calcular Ingredientes", on_click=calcular, icon=ft.icons.CALCULATE),
        ft.Divider(),
        res_harina,
        res_agua,
        res_sal,
        res_levadura
    )

# --- CONFIGURACIÓN PARA LA NUBE (STREAMLIT) ---
if __name__ == "__main__":
    # Streamlit usa el puerto 8501 por defecto en su nube
    port = int(os.environ.get("PORT", 8501))
    ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=port)
