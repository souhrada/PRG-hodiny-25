from nicegui import ui

def hokus():
    # ui.notify vytvoří upozornění
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

# ui.element("div") vytvoří div
# .classes() přidává css classy, předvytvořené ve frameworku Tailwind
with ui.element("div").classes("w-full h-screen flex items-center justify-center flex-col gap-5"):

    # ui.label vytvoří label, neboli textové pole
    ui.label("Hello!").classes("text-blue-400 font-bold text-4xl")
    ui.label("Bye!").style("color: blue")

    # ui.button vytvoří tlačítko
    ui.button("Klikni sem!", on_click=hokus)

    # ui.grid vytvoří grid (mřížku o 3 sloupcích) a cyklem for projdeme dictionary tlacitka a pro každý key-value vytvoříme tlačítko
    # kde key = název tlačítka, value je funkce, kterou spouští
    with ui.grid(columns=3):
        for jmeno, funkce in tlacitka.items():
            ui.button(jmeno, on_click=funkce)

# spuštění našeho ui - native=True skryje prohlížeč
ui.run(native=True)