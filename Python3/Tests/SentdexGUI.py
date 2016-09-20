class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        #fill, let's fill based on limitations you set. Expand, let's fill everything we can
        container.pack(side='top', fill='both', expand=True)
        #0 is a size component, weight is about priority
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = []

        frame = StartPage(container, self)

        self.frames[StartPage] = frame

        #alignment and stretch (north, south, east, west)
        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
