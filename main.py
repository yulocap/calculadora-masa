import flet as ft
import os

def main(page: ft.Page):
    page.title = "Calculadora Panadera"
    page.padding = 20
    
    # Entradas de datos
    txt_total = ft.TextField(label="Peso Total Masa (gr)", value="1000")
    txt_agua = ft.TextField(label="% Agua (Hidratación)", value="60")
    txt_sal = ft.TextField(label="% Sal", value="2")
    txt_lev = ft.TextField(label="% Levadura", value="1")

    # Etiquetas de resultado
    res_harina = ft.Text(size=20, weight="bold")
    res_ingredientes = ft.Text(size=18)

    def calcular(e):
        try:
            total = float(txt_total.value)
            # El % de harina siempre es 100
            p_agua = float(txt_agua.value) / 100
            p_sal = float(txt_sal.value) / 100
            p_lev = float(txt_lev.value) / 100
            
            # Fórmula: Total / (1 + %agua + %sal + %lev)
            harina = total / (1 + p_agua + p_sal + p_lev)
            
            res_harina.value = f"Harina: {harina:.0f} gr"
            res_ingredientes.value = (
                f"Agua: {(harina * p_agua):.0f} gr\n"
                f"Sal: {(harina * p_sal):.0f} gr\n"
                f"Levadura: {(harina * p_lev):.0f} gr"
            )
        except:
            res_harina.value = "Error en los números"
        page.update()

    page.add(
        ft.Text("Calculadora de Masa", size=25),
        txt_total,
        txt_agua,
        txt_sal,
        txt_lev,
        ft.ElevatedButton("CALCULAR", on_click=calcular),
        res_harina,
        res_ingredientes
    )

if __name__ == "__main__":
    # Forzamos el puerto de Render
    port = int(os.environ.get("PORT", 8080))
    ft.app(target=main, view=ft.AppView.WEB_BROWSER, host="0.0.0.0", port=port)
