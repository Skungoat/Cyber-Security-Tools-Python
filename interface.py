import customtkinter as ctk
import arithmetic
import encryptor
import random

class interface(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Example of rsa")
        self.geometry("600x500")
        ctk.set_appearance_mode("dark")

        self.public_key = None
        self.private_key = None
        self.n = None
        self.e=None
        self.d=None
        self.crypted=None
        self.setup_ui()

    def setup_ui(self):
        self.gen_button = ctk.CTkButton(self, text="Générer les clés (1024 bits)", command=self.generate_keys)
        self.gen_button.pack(pady=20)
        self.input_label = ctk.CTkLabel(self, text="Message à chiffrer :")
        self.input_label.pack()
        self.encrypt_button = ctk.CTkButton(self, text="Chiffrer", command=self.encryption)
        self.encrypt_button.pack(pady=10)
        self.encrypt_button = ctk.CTkButton(self, text="Déchiffrer", command=self.decryption)
        self.encrypt_button.pack(pady=10)
        self.input_entry = ctk.CTkEntry(self, width=400)
        self.input_entry.pack(pady=10)
        self.output_box = ctk.CTkTextbox(self, width=500, height=150)
        self.output_box.pack(pady=20)

    def generate_keys(self):
        p = arithmetic.generate_prime(32)
        q = arithmetic.generate_prime(32)
        self.n = p * q
        phi_n=arithmetic.euler(p,q)
        e= 65537
        while(arithmetic.is_prime_with(e,phi_n)!=True):
            e= random.randint(2, phi_n-1)
        self.e=e
        self.public_key=(e,self.n)
        d=arithmetic.inverse_modulo(e,phi_n)
        self.d=d
        self.private_key=(d,self.n)
        self.output_box.insert("0.0", f"Public Key  = {str(self.public_key)[:50]}...\nPrivate Key=  {str(self.private_key)[:50]}\n")

    def encryption(self):
        if self.n is None:
            self.output_box.insert("end", "⚠️ Erreur : Génère d'abord les clés !\n")
            return
        msg = self.input_entry.get()
        m_int = encryptor.Encryptor.string_to_int(msg)
        c = arithmetic.exp_modulo(m_int, self.e, self.n)
        self.crypted=c
        
        self.output_box.insert("end", f"🔒 Message chiffré : {str(c)[:50]}\n")
    def decryption(self):
        if self.crypted is None:
            self.output_box.insert("end", "⚠️ Erreur : Chiffre d'abord ton message !\n")
            return
        chiffre= arithmetic.exp_modulo(self.crypted,self.d,self.n)
        m_msg= encryptor.Encryptor.int_to_string(chiffre)
        self.output_box.insert("end", f"🔒 Message déchiffré : {str(m_msg)[:50]}\n")

if __name__ == "__main__":
    app = interface()
    app.mainloop()