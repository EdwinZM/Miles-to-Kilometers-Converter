import tkinter

window = tkinter.Tk()
window.title("Miles to kilometers Converter")
window.config(padx=20, pady=20)

is_to_label = tkinter.Label(text="is equal to")
is_to_label.grid(column=0, row=1)

m_input = tkinter.Entry()
m_input.grid(column=1, row=0)

result = tkinter.Label(text="0")
result.grid(column=1, row=1)

def get_result():
    value = int(m_input.get())
    calc = round(value * 1.6, 1)
    result.config(text=f"{calc}")

calc_button = tkinter.Button(text="Calculate", command=get_result)
calc_button.grid(column=1, row=2)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)

window.mainloop()