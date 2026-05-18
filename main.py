import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora de Masas"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    
    # --- Componentes ---
    tipo_masa = ft.Dropdown(
        label="Selecciona Tipo de Masa",
        options=[
            ft.dropdown.Option("horno"),
            ft.dropdown.Option("freir"),
            ft.dropdown.Option("fideos"),
        ],
        width=300,
    )
    
    kg_harina = ft.TextField(
        label="Kg de Harina", 
        width=300
    )
    
    resultado = ft.Column()

    def calcular(e):
        resultado.controls.clear()
        masa = tipo_masa.value
        
        if not masa or not kg_harina.value:
            resultado.controls.append(ft.Text("Completa todos los campos", color="orange"))
            page.update()
            return

        try:
            kg = float(kg_harina.value)
        except:
            resultado.controls.append(ft.Text("Ingresa un número válido", color="red"))
            page.update()
            return

        datos = []
        error = False

        if masa == 'horno':
            if kg == 60:
                datos = [("Antimoho", "120 grs"), ("Sorbato", "60 grs"), ("Sal", "1.9 Kg"), ("Agua", "27.5 Kg")]
            elif kg == 40:
                datos = [("Antimoho", "80 grs"), ("Sorbato", "40 grs"), ("Sal", "1.25 Kg"), ("Agua", "18.3 Kg")]
            else: error = True
        
        elif masa == 'freir':
            if kg == 60:
                datos = [("Antimoho", "120 grs"), ("Sorbato", "60 grs"), ("Sal", "1.9 Kg"), ("Agua", "21 Kg"), ("Grasa", "6.5 Kg")]
            elif kg == 50:
                datos = [("Antimoho", "100 grs"), ("Sorbato", "50 grs"), ("Sal", "1.6 Kg"), ("Agua", "17.5 Kg"), ("Grasa", "5.4 Kg")]
            elif kg == 25:
                datos = [("Antimoho", "50 grs"), ("Sorbato", "25 grs"), ("Sal", "0.8 Kg"), ("Agua", "8.75 Kg"), ("Grasa", "2.7 Kg")]
            else: error = True

        elif masa == 'fideos':
            if kg == 50:
                datos = [("Antimoho", "100 grs"), ("Sorbato", "50 grs"), ("Colorante", "240 grs"), ("Huevos", "30 unidades"), ("Agua", "12.8 Kg")]
            else: error = True

        if error:
            resultado.controls.append(ft.Text("Cantidad de harina no válida", color="red"))
        else:
            resultado.controls.append(ft.Text(f"Receta para {masa.upper()}:", size=20, weight="bold"))
            for nombre, valor in datos:
                # Aquí quitamos los iconos por completo
                resultado.controls.append(ft.Text(f"• {nombre}: {valor}", size=16))
        
        page.update()

    # Botón sin icono para evitar errores
    btn_calcular = ft.FilledButton(
        "Calcular Receta", 
        on_click=calcular, 
        width=300
    )

    page.add(
        ft.Text("Calculadora de Producción", size=28, weight="bold"),
        ft.Divider(),
        tipo_masa,
        kg_harina,
        btn_calcular,
        ft.Divider(),
        resultado
    )

ft.app(target=main, view=None, port=8080, host="0.0.0.0")