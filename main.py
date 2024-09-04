import tkinter as tk

CURRENCIES = {
        'GE': {
            'unit': 1,
            'USD': 0.37,
            'LIRA': 12.64,
            'RUBL': 32.66
            },
        'USD': {
            'unit': 1,
            'GE': 2.69,
            'LIRA': 34,
            'RUBL': 87.87
            },
        'RUBL': {
            'unit': 1,
            'GE': 0.031,
            'LIRA': 0.39,
            'USD': 0.011
            },
        'LIRA': {
            'unit': 1,
            'GE': 0.079,
            'USD': 0.029,
            'RUBL': 2.58,
            },
    }

currencies_list = [*CURRENCIES.keys()]

def main():

    global conversion_rate_label, base_curr, conversion_curr, result_label, amount_field, main_frame, root

    root = tk.Tk()
    window_width = 800
    window_height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_offset = (screen_width // 2) - (window_width // 2)
    y_offset = (screen_height // 2) - (window_height // 2)
    root.geometry(f'{window_width}x{window_height}+{x_offset}+{y_offset}')
    root.title('Currency Converter')
    root.resizable(width=False, height=False)
    
    main_frame = tk.Frame(root, bd=1, relief=tk.FLAT)
    main_frame.grid(row=0, column=0, sticky='nswe')
    main_frame.grid_rowconfigure(0, weight=1)
    main_frame.grid_rowconfigure(1, weight=1)
    main_frame.grid_rowconfigure(2, weight=1)
    main_frame.grid_columnconfigure(0, weight=1)

    # currencies frame
    curr_frame = tk.Frame(main_frame, bd=1, relief=tk.SUNKEN)
    curr_frame.grid(row=0, column=0, sticky='nswe', padx=10, pady=10)
    curr_frame.grid_rowconfigure(0, weight=1)
    curr_frame.grid_columnconfigure(0, weight=1)
    curr_frame.grid_columnconfigure(1, weight=1)

    # base currency 
    base_curr_frame = tk.Frame(curr_frame)
    base_curr_frame.grid(row=0, column=0, sticky='nswe', padx=10, pady=10)
    base_curr_label = tk.Label(base_curr_frame, text='From:', font=('Arial', 14))
    base_curr_label.grid(row=0, column=0, sticky='nswe')
    base_curr = tk.StringVar(base_curr_frame)
    base_curr.set(currencies_list[0])
    base_curr_menu = tk.OptionMenu(base_curr_frame, base_curr, *currencies_list, command=on_curr_change)
    base_curr_menu.grid(row=1, column=0, sticky='nswe')

    # conversion currency
    conversion_curr_frame = tk.Frame(curr_frame)
    conversion_curr_frame.grid(row=0, column=1, sticky='nswe', padx=10, pady=10)
    conversion_curr_label = tk.Label(conversion_curr_frame, text='To:', font=('Arial', 14))
    conversion_curr_label.grid(row=0, column=0, sticky='nswe')
    conversion_curr = tk.StringVar(conversion_curr_frame)
    conversion_curr.set(currencies_list[1])
    conversion_curr_menu = tk.OptionMenu(conversion_curr_frame, conversion_curr, *currencies_list, command=on_curr_change)
    conversion_curr_menu.grid(row=1, column=0, sticky='nswe')

    # amount
    amount_frame = tk.Frame(curr_frame)
    amount_frame.grid(row=0, column=2, sticky='nswe', padx=10, pady=10)
    amount_label = tk.Label(amount_frame, text='Amount:', font=('Arial', 14))
    amount_label.grid(row=0, column=0, sticky='nswe')
    amount_field = tk.Entry(amount_frame, bg='lavender', highlightthickness=0)
    amount_field.grid(row=1, column=0, sticky='nswe')


    # exchange rate 
    rate_frame = tk.Frame(curr_frame)
    rate_frame.grid(row=1, column=0, columnspan=3, sticky='w', padx=10, pady=10)
    conversion_rate_label = tk.Label (rate_frame, text=f'Rate: {convert(base_curr.get(),conversion_curr.get())}', font=('Arial', 14))
    conversion_rate_label.pack(side='top', pady=5)

    # actions
    action_frame = tk.Frame(main_frame, bd=1, relief=tk.SUNKEN)
    action_frame.grid(row=1, column=0, sticky='nswe', padx=10, pady=10)
    action_frame.grid_rowconfigure(0, weight=1)
    action_frame.grid_rowconfigure(1, weight=1)
    action_frame.grid_columnconfigure(0, weight=1)
    action_frame.grid_columnconfigure(1, weight=1)
    
    btn_convert = tk.Button(action_frame, text='Convert', command=on_click_convert)
    btn_convert.grid(row=0, column=0, padx=5, pady=5)
    btn_clear = tk.Button(action_frame, text='Clear', command=on_click_clear)
    btn_clear.grid(row=0, column=1, padx=5, pady=5)

    # result
    result_frame = tk.Frame(main_frame, bd=1, relief=tk.SUNKEN)
    result_frame.grid(row=2, column=0, sticky='nswe', padx=10, pady=10)
    result_frame.grid_rowconfigure(0, weight=1)

    result_label = tk.Label(result_frame, text='Result:', font=('Arial', 14))
    result_label.pack(side='top', pady=5)


    root.update_idletasks()
    center_main_frame()  

    root.mainloop()


# calculate the width and height of the main frame and according to that apply paddings for centering

def center_main_frame():
    main_frame.update_idletasks()  
    main_frame_width = main_frame.winfo_width()
    main_frame_height = main_frame.winfo_height()
    
    root_width = root.winfo_width()
    root_height = root.winfo_height()
    
    padx = (root_width - main_frame_width) // 2
    pady = (root_height - main_frame_height) // 2
    
    main_frame.grid_configure(padx=padx, pady=pady)

# convert from one currency to another

def convert(curr_1, curr_2):
    curr_1_value = round(float(CURRENCIES[curr_1]['unit']), 2)
    if curr_1 != curr_2:
        curr_2_value = round(float(CURRENCIES[curr_1][curr_2]), 2)
    else:
        curr_2_value = curr_1_value

    return curr_1_value * curr_2_value


# recalculate exchange rate according to the selected currencies

def on_curr_change(event):
    base_currency = base_curr.get()
    conversion_currency = conversion_curr.get()
    conversion_rate = convert(base_currency, conversion_currency)
    conversion_rate_label.config(text=f'Rate : {conversion_rate}')


# on button click return all of widget values to its initial states

def on_click_clear():
    base_currency = currencies_list[0]
    conversion_currency = currencies_list[1]
    base_curr.set(base_currency)
    conversion_curr.set(conversion_currency)
    amount_field.delete(0, tk.END)
    conversion_rate_label.config(text=f'Rate : {convert(base_currency, conversion_currency)}')
    result_label.config(text=f'Result : ')


# on button click convert given amount of base currency in to another and display the result

def on_click_convert():
    try:
        amount = amount_field.get()
        if not amount:
            result_label.config(text='Result : Please enter an amount')
            return

        amount = float(amount)
        base_currency = base_curr.get()
        conversion_currency = conversion_curr.get()
        conversion_rate = convert(base_currency, conversion_currency)
        converted_amount = amount * conversion_rate
        result_label.config(text=f'Result : {int(amount)} {base_currency} is {converted_amount:.2f} {conversion_currency}')
    except ValueError:
        result_label.config(text='Result : Invalid amount. Please provide valid integer as amount!')


if __name__ == '__main__':
    main()
