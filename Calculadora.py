from tkinter import Tk, Text, Button



class Interfaz:
    def __init__(self, ventana):
        self.ventana=ventana
        self.ventana.title("Calculadora")
        self.ventana_text=Text(ventana, state="disabled", width=40, height=5, background="orchid", foreground="white", font=("Helvetica", 15))
        self.ventana_text.grid(row=0, column=0, columnspan=5, padx=5, pady=5, sticky = ("e", "w"))
        self.operacion=""

        boton1=self.createButton(7)
        boton2=self.createButton(8)
        boton3=self.createButton(9)
        boton4=self.createButton(u"\u232B", escribir=False)
        boton5=self.createButton(4)
        boton6=self.createButton(5)
        boton7=self.createButton(6)
        boton8=self.createButton(u"\u00F7")
        boton9=self.createButton(1)
        boton10=self.createButton(2)
        boton11=self.createButton(3)
        boton12=self.createButton("*")
        boton13=self.createButton(".")
        boton14=self.createButton(0)
        boton15=self.createButton("+")
        boton16=self.createButton("-")
        boton17=self.createButton("/")
        boton18=self.createButton("=", escribir=False, ancho=20, alto=2)
        botones=[boton1, boton2, boton3, boton4, boton5, boton6, boton7, boton8, boton9, boton10, boton11, boton12, boton13, boton14, boton15, boton16, boton17, boton18]
        contador=0

        for fila in range(1, 5):
            for columna in range(1, 5):
                botones[contador].grid(row=fila, column=columna)
                contador+=1
        botones[17].grid(row=5, column=0, columnspan=5, sticky = ("e","w"))

    def createButton(self, valor, escribir=True, ancho=9, alto=1):
        return Button(self.ventana, text=valor, width=ancho, height=alto, font=("Helvetica", 15), command=lambda:self.click(valor, escribir))


if __name__ == "__main__":
    ventana_principal=Tk()
    calculadora=Interfaz(ventana_principal)
    ventana_principal.mainloop()
