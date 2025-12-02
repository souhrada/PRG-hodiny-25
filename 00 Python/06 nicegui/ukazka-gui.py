from nicegui import ui

def hokus():
    ui.notify("Tlačítko hokus kliknuto")

def pokus():
    ui.notify("Tlačítko pokus kliknuto")

def lokus():
    ui.notify("Tlačítko lokus kliknuto")

tlacitka = {
    "První": hokus,
    "Druhé": pokus,
    "Třetí": lokus
}    

with ui.element("div").classes("w-full h-screen flex items-center justify-center flex-col gap-5"):

    ui.label("Hello!").classes("text-blue-400 font-bold text-4xl")
    ui.label("Bye!").style("color: blue")
    ui.button("Klikni sem!", on_click=hokus)

    with ui.grid(columns=3):
        for jmeno, funkce in tlacitka.items():
            ui.button(jmeno, on_click=funkce)


ui.run(native=True)