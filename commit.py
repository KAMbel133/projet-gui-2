def search_text():
    recherche = tk.simpledialog.askstring("Search", "Enter text to search:")
    if recherche:
        debut= '1.0'
        while True:
            debut = text.search(recherche, debut, stopindex='end')
            if not debut:
                break
            fin = f"{debut}+{len(recherche)}c"
            text.tag_add("search", debut, fin)
            debut = fin
        text.tag_config("search", background="yellow")  
 