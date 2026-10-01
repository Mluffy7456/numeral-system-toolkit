import tkinter as tk
from tkinter import ttk, messagebox
from converter import convert_number
from ieee754 import encode_float
from ascii_converter import text_to_ascii, ascii_to_text
from utf8_converter import text_to_utf8, utf8_to_text
from twos_complement import encode_twos, decode_twos
from gray_code import encode_gray, decode_gray

class ToolkitGUI:
    def __init__(self, root):
        self.root = root
        root.title("Numeral System Toolkit")
        root.geometry("820x560")
        root.minsize(700, 480)
        notebook = ttk.Notebook(root)
        notebook.pack(fill="both", expand=True, padx=12, pady=12)
        self._converter(notebook)
        self._encoding(notebook)

    def _converter(self, notebook):
        frame = ttk.Frame(notebook, padding=18); notebook.add(frame, text="Converter")
        ttk.Label(frame, text="Number").grid(row=0,column=0,sticky="w")
        self.num = ttk.Entry(frame); self.num.grid(row=0,column=1,sticky="ew")
        ttk.Label(frame, text="From base").grid(row=1,column=0,sticky="w")
        self.fb = ttk.Entry(frame); self.fb.insert(0,"10"); self.fb.grid(row=1,column=1,sticky="ew")
        ttk.Label(frame, text="To base").grid(row=2,column=0,sticky="w")
        self.tb = ttk.Entry(frame); self.tb.insert(0,"16"); self.tb.grid(row=2,column=1,sticky="ew")
        ttk.Button(frame,text="Convert",command=self.convert).grid(row=3,column=0,columnspan=2,pady=12)
        self.out = tk.Text(frame,height=12); self.out.grid(row=4,column=0,columnspan=2,sticky="nsew")
        frame.columnconfigure(1,weight=1); frame.rowconfigure(4,weight=1)

    def convert(self):
        try: self.out.delete("1.0","end"); self.out.insert("end",convert_number(self.num.get().strip().upper(),int(self.fb.get()),int(self.tb.get())))
        except Exception as e: messagebox.showerror("Error",str(e))

    def _encoding(self, notebook):
        frame=ttk.Frame(notebook,padding=18); notebook.add(frame,text="Encoders")
        self.enc_in=tk.Text(frame,height=8); self.enc_in.grid(row=0,column=0,columnspan=3,sticky="nsew")
        self.enc_out=tk.Text(frame,height=8); self.enc_out.grid(row=2,column=0,columnspan=3,sticky="nsew")
        options=["ASCII encode","ASCII decode","UTF-8 encode","UTF-8 decode","Two's complement encode","Two's complement decode","Gray encode","Gray decode","IEEE 754 float32"]
        self.mode=ttk.Combobox(frame,values=options,state="readonly"); self.mode.current(0); self.mode.grid(row=1,column=0,sticky="ew")
        ttk.Button(frame,text="Run",command=self.run_encoding).grid(row=1,column=1,padx=8)
        ttk.Label(frame,text="For Two's complement encode: enter 'value,width'.").grid(row=3,column=0,columnspan=3,sticky="w")
        frame.columnconfigure(0,weight=1); frame.columnconfigure(1,weight=1); frame.columnconfigure(2,weight=1); frame.rowconfigure(0,weight=1); frame.rowconfigure(2,weight=1)

    def run_encoding(self):
        value=self.enc_in.get("1.0","end").strip()
        mode=self.mode.get()
        try:
            if mode=="ASCII encode": result=text_to_ascii(value)
            elif mode=="ASCII decode": result=ascii_to_text(value)
            elif mode=="UTF-8 encode": result=text_to_utf8(value)
            elif mode=="UTF-8 decode": result=utf8_to_text(value)
            elif mode=="Two's complement encode":
                n,w=value.split(",",1); result=encode_twos(int(n),int(w))
            elif mode=="Two's complement decode": result=str(decode_twos(value))
            elif mode=="Gray encode": result=str(encode_gray(int(value)))
            elif mode=="Gray decode": result=str(decode_gray(int(value)))
            else: result=encode_float(float(value),32)[3]
            self.enc_out.delete("1.0","end"); self.enc_out.insert("end",result)
        except Exception as e: messagebox.showerror("Error",str(e))

def run_gui():
    root=tk.Tk()
    ToolkitGUI(root)
    root.mainloop()

if __name__=="__main__": run_gui()
