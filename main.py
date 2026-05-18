import signal
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

    def calcular(e):
        try:
            total = float(txt_peso_total.value)
            p_harina = float(txt_p_harina.value) / 100
            p_agua = float(txt_p_agua.value) / 100
            p_sal = float(txt_p_sal.value) / 100
            p_levadura = float(txt_p_levadura.value) / 100
            base = p_harina + p_agua + p_sal + p_levadura
            harina = total / base
            res_harina.value = f"Harina: {harina:.2f} gr"
            res_agua.value = f"Agua: {(harina * p_agua):.2f} gr"
            res_sal.value = f"Sal: {(harina * p_sal):.2f} gr"
            res_levadura.value = f"Levadura: {(harina * p_levadura):.2f} gr"
        except ValueError:
            res_harina.value = "Error: Ingresa números"
        page.update()

    txt_peso_total = ft.TextField(label="Peso total (gr)", value="1000", border_color="blue")
    txt_p_harina = ft.TextField(label="% Harina", value="100")
    txt_p_agua = ft.TextField(label="% Agua", value="60")
    txt_p_sal = ft.TextField(label="% Sal", value="2")
    txt_p_levadura = ft.TextField(label="% Levadura", value="1")

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
        # Botón simple sin iconos para evitar errores de versión
        ft.ElevatedButton("Calcular Ingredientes", on_click=calcular),
        ft.Divider(),
        res_harina,
        res_agua,
        res_sal,
        res_levadura
    )

if __name__ == "__main__":
    puerto = int(os.environ.get("PORT", 8080))
    ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=puerto, host="0.0.0.0")
