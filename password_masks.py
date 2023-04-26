# %% Importy

import secrets
import string
import random
import pandas as pd

# %% Parametry

# Ile haseł ma zostać wygenerowanych
ILOŚĆ_HASEŁ = 10000
# Ile najczęstszych masek ma zostać pokazanych
TOP = 5

# %% Generator haseł

letters = string.ascii_letters
digits = string.digits
special = string.punctuation
alphabet = letters + digits + special

pwd = ""
with open("passwords.txt", "w") as file:
    for i in range(ILOŚĆ_HASEŁ):
        for j in range(0, random.choice(range(6, 11))):
            pwd += secrets.choice(alphabet)
        file.write(pwd + "\n")
        pwd = ""

# %% Konwerter na maski

masks = []

with open("passwords.txt", "r") as file:
    for pwd in file:
        password = ""
        for smb in pwd:
            if smb.isalpha():
                if smb.isupper():
                    password += "?u"
                elif smb.islower():
                    password += "?l"
            elif smb.isdigit():
                password += "?d"
            elif smb != "\n":
                password += "?s"
        masks.append(password)
        password = ""

# %% Rozwiązanie Pandas

df = pd.DataFrame({"Maska":masks})
df.value_counts().sort_values(ascending=False).head(TOP)

# %%

