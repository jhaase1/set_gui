import tkinter as tk
import tkinter.ttk as ttk
import os
from PIL import Image, ImageTk

card_creator_images_folder = 'create_card_images'

def create_card():
    """Convert the value for Fahrenheit to Celsius and insert the
    result into lbl_result.
    """
    add_card_window = tk.Toplevel()

    def add_card():
        print(add_card_window['0'])
        pass
    
    action_buttons = {
        'Add card': add_card,
        'Cancel card': add_card_window.destroy
    }
    
    card_attributes = {
        'count': [ str(i+1) for i in range(3) ],
        'color': ['red', 'purple', 'green'],
        'shape': ['squiggle', 'diamond', 'ellipse'],
        'fill': ['solid', 'hatched', 'empty']
    }
    
    insert_cancel_frame = tk.Frame(
        master=add_card_window,
        borderwidth=1
    )
    
    for row, (txt, command) in enumerate(action_buttons.items()):
        button_frame = tk.Frame(
            master=insert_cancel_frame
        )
            
        button_frame.grid(row=row, column=0, padx=5, pady=5)
    
        tk.Button(
            master=button_frame,
            text = txt,
            command=command
        ).pack(padx=5, pady=5)
    
    insert_cancel_frame.pack(fill=tk.Y, side=tk.LEFT)
    
    card_attribute_frame = tk.Frame(
        master=add_card_window,
        borderwidth=1
    )
    
    for j, attr_class in enumerate(card_attributes):
        attribute_frame = tk.Frame(
            master=card_attribute_frame,
            borderwidth=1
        )
        
        v = tk.StringVar(add_card_window, str(j))
        
        for i, attr in enumerate(card_attributes[attr_class]):           
            img = ImageTk.PhotoImage(
                Image.open(
                    os.path.join(
                        card_creator_images_folder,
                        attr + '.png'
                    )
                ).resize((72, 128), Image.BILINEAR)
            )
            
            button = tk.Radiobutton(
                master=attribute_frame,
                image=img,
                variable = v,
                value = i,
                indicator = 0,
                background = "black",
            )
            
            button.image = img
            button.pack(padx=5, pady=5)
    
        attribute_frame.pack(fill=tk.Y, side=tk.LEFT)
    
    card_attribute_frame.pack()
    
    tk.mainloop()


# Set up the window
window = tk.Tk()

frame1 = tk.Frame(master=window, width=200, height=100, bg="red")

# Create the conversion Button and result display Label
btn_convert = tk.Button(
    master=frame1,
    text="Add card",
    command=create_card
)

# Set up the layout using the .grid() geometry manager

btn_convert.pack(side=tk.LEFT)
frame1.pack(side=tk.LEFT)

# Run the application
window.mainloop()
