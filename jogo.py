import tkinter as tk
from tkinter import messagebox
import random
import spacy

words = [
    "apple",      
    "run",         
    "quickly",     
    "computer",   
    "write",      
    "beautiful",   
    "slowly",      
    "book",        
    "jump",        
    "bright",      
    "carefully",   
    "dog",         
    "sing",        
    "dark",        
    "loudly",      
    "city",       
    "dance",       
    "cold",       
    "quietly",     
    "flower",     
    "read",       
    "hot",         
    "quickly",     
    "mountain",    
    "swim",        
    "soft",        
    "happily",     
    "car",         
    "think"        
]

drawn_word = random.choice(words)


def calcular_similaridade(player_word: str, drawn_word: str) -> float:
    nlp = spacy.load('en_core_web_lg')  
    player_word = nlp(player_word)     
    drawn_word = nlp(drawn_word)        
    return player_word.similarity(drawn_word)  


def main():
    declared_word = inputed_word.get().strip().lower()

   
    if not declared_word:
        messagebox.showwarning('Aviso', 'Digite uma palavra!')
        return


    if declared_word == drawn_word:
        messagebox.showinfo('Resultado', 'Você acertou a palavra exata!')
        root.quit()
        return

 
    similarity = calcular_similaridade(declared_word, drawn_word)

  
    if similarity < 0.3:  
        messagebox.showinfo('Game Over', f'Palavra muito diferente! Similaridade: {similarity:.2f}')
        root.quit()
    else:  
        messagebox.showinfo('Resultado', f'Palavra similar! Similaridade: {similarity:.2f}')

    label_word.config(text=f'Palavra sorteada: {drawn_word}')
    inputed_word.delete(0, tk.END)


root = tk.Tk()
root.title('Jogo de Palavras Similares')
root.geometry('400x300')


label_instrucao = tk.Label(root, text="Digite uma palavra similar à sorteada!", font=("Arial", 12))
label_instrucao.pack(pady=10)

label_word = tk.Label(root, text=f"Palavra sorteada: {drawn_word}", font=("Arial", 14, "bold"))
label_word.pack(pady=10)


inputed_word = tk.Entry(root, font=("Arial", 12))
inputed_word.pack(pady=5)


botao_enviar = tk.Button(root, text="Enviar", command=main, font=("Arial", 12))
botao_enviar.pack(pady=10)

root.mainloop()