import tkinter as tk

CURRENCIES = {
        'GE':
        {
            'unit': 1,
            'USD': 0.37,
            'LIRA': 12.64,
            'RUBL': 32.66,
        },
        'USD':
        {
            'unit': 1,
            'GE': 2.69,
            'LIRA': 34,
            'RUBL': 87.87,
        },
        'RUBL':
        {
            'unit': 1,
            'GE': 0.031,
            'LIRA': 0.39,
            'USD': 0.011,
        },
        'LIRA':
        {
            'unit': 1,
            'GE': 0.079,
            'USD': 0.029,
            'RUBL': 2.58,
        },
    }

currencies_list = [*CURRENCIES.keys()]

def main():

    global conversion_rate_label, base_curr, conversion_curr, result_label, amount_field

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

    
    # currencies frame
    currency_frame = tk.Frame(root, bd=1, relief=tk.SUNKEN)
    currency_frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

    base_curr_label = tk.Label(currency_frame, text='From', font=('Arial', 14)) 
    base_curr_label.grid(row=0, column=0, sticky='W', padx=10, pady=10)

    base_curr = tk.StringVar(currency_frame)
    base_curr.set(currencies_list[0])
    base_curr_menu = tk.OptionMenu(currency_frame, base_curr, *currencies_list, command=on_curr_change)
    base_curr_menu.grid(row=0, column=1, sticky='ew', padx=10, pady=10)

    conversion_curr_label = tk.Label(currency_frame, text='To', font=('Arial', 14))
    conversion_curr_label.grid(row=1, column=0, sticky='W', padx=10, pady=10)

    conversion_curr = tk.StringVar(currency_frame)
    conversion_curr.set(currencies_list[1])
    conversion_curr_menu = tk.OptionMenu(currency_frame, conversion_curr, *currencies_list, command=on_curr_change)
    conversion_curr_menu.grid(row=1, column=1, sticky='ew', padx=10, pady=10)

    first_num = round(float(CURRENCIES[base_curr.get()]['unit']), 2)
    second_num = round(float(CURRENCIES[base_curr.get()][conversion_curr.get()]), 2)

    conversion_rate_label = tk.Label(currency_frame, text=f'Rate : {convert(first_num, second_num)}', font=('Arial', 14))
    conversion_rate_label.grid(row=2, column=0, sticky='W', padx=10, pady=10)
    

    # actions frame
    action_frame = tk.Frame(root, bd=1, relief=tk.SUNKEN)
    action_frame.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)

    # amount for conversion
    amount_frame = tk.Frame(action_frame, relief=tk.SUNKEN)
    amount_frame.grid(row=0, column=0, sticky='ew', padx=10, pady=10)
    amount_label = tk.Label(amount_frame, text='Amount:', font=('Arial', 14))
    amount_label.pack(side='left', padx=10, pady=10)
    amount_field = tk.Entry(amount_frame, bg='lavender', highlightthickness=0)
    amount_field.pack(side='left', padx=10, pady=10)

    # action buttons
    btn_frame = tk.Frame(action_frame, relief=tk.SUNKEN)
    btn_frame.grid(row=1, column=0, sticky='ew', padx=10, pady=10)

    btn_convert = tk.Button(btn_frame, text='Convert', command=on_click_convert)
    btn_convert.pack(side='left', padx=10, pady=10)
    btn_clear = tk.Button(btn_frame, text='Clear', command=on_click_clear)
    btn_clear.pack(side='left', padx=10, pady=10)

    # result frame
    result_frame = tk.Frame(root, bd=1, relief=tk.SUNKEN)
    result_frame.grid(row=2, column=0, sticky='nsew', padx=10, pady=10)

    result_label = tk.Label(result_frame, text='Result : ', font=('Arial', 14))
    result_label.pack(side='left', padx=10, pady=10)

    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_columnconfigure(0, weight=1)

    root.mainloop()


# convert from one currency to another

def convert(first, second):
    return first * second


# recalculate exchange rate according to the selected currencies

def on_curr_change(event):
    base_currency = base_curr.get()
    conversion_currency = conversion_curr.get()
    if base_currency and conversion_currency:
        first_num = round(float(CURRENCIES[base_currency]['unit']), 2)
        if base_currency != conversion_currency:
            second_num = round(float(CURRENCIES[base_currency][conversion_currency]), 2)
        else:
            second_num = first_num
        conversion_rate = convert(first_num, second_num)
        conversion_rate_label.config(text=f'Rate : {conversion_rate}')


# on button click return all of widget values to its initial states

def on_click_clear():
    base_currency = currencies_list[0]
    conversion_currency = currencies_list[1]
    first_num = round(float(CURRENCIES[base_currency]['unit']), 2)
    second_num = round(float(CURRENCIES[base_currency][conversion_currency]), 2)
    base_curr.set(base_currency)
    conversion_curr.set(conversion_currency)
    amount_field.delete(0, tk.END)
    conversion_rate_label.config(text=f'Rate : {convert(first_num, second_num)}')
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
        first_num = round(float(CURRENCIES[base_currency]['unit']), 2)
        second_num = round(float(CURRENCIES[base_currency][conversion_currency]), 2)
        conversion_rate = convert(first_num, second_num)
        converted_amount = amount * conversion_rate
        result_label.config(text=f'Result : {int(amount)} {base_currency} is {converted_amount:.2f} {conversion_currency}')
    except ValueError:
        result_label.config(text='Result : Invalid amount. Please provide valid integer as amount!')


if __name__ == '__main__':
    main()
