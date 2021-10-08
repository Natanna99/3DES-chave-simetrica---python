import DES3
import hashlib

key= DES3.DES3Cipher("prova-ss")

def criaHash():
    string = input("Digite a msg: ")
    chave= input("Digite a chave: ")
    msgKey= string+chave
    resultado = hashlib.md5(msgKey.encode('utf-8'))
    print("Chave: ",chave)
    print("Mensagem: ", string)
    print("\nHash gerado: ",resultado.hexdigest())
    return resultado

def concatenaMsg():
    hashMsg = criaHash()
    MsgEntrada = "natanna rocha santos"
    concatenacao= MsgEntrada+" "+hashMsg.hexdigest()
    return concatenacao

msg= concatenaMsg()
msg2="AAAAB3NzaC1yc2EAAAADAQABAAABgQCohSTU3kl8jooJTWuVclcO5nL/PyjURMXl6nT0RdLi7BFMyK9HOQeliW+xKbjc+MzsZ/0AApks7yffAzWSjlainM70R72XEXyODIMHxC5/djGuQpngyPBD32HXv3eWSaawGAUt7EdN+59UzxsHJzTPZjQMB2hL4p4tMaat4IMdDqQKx+CIROA1pijx6m/eGrvrngqGxnk1zbs2I2CK/IKCoC1W4PeQ4aj1+BTnXed27pmd7RlYtmPUk8vchRGbgitRjQQPGRdk/jXj3Mj5D2Xi1cSy6yydBrbT342fy8Jy/3dTHFVAoB95tKeW6m19bh3lybdpv2em1gINgWz094Qapu3XLqFsvn21eouaWeyhh6yLzBxoiuVB+eWlb9vymPRxUe+riiS3/SNlhqn7Y1MYvLIsvAo/bynAOkvmhqeL6NoRhCVspdcfZnkyTbBR/6lzq5EUdakBO2nmG2I2g0Heftk36s9VU3U3rDQGZrz47ag8aJdcW9g8CHPc96Qo2xs= erzafairy79@gmail.com"


print("\n-----------Mensagem encriptada-------------\n")
FraseCript = key.encrypt(msg)
print("Mensagem encriptada: \n", FraseCript, "\n")

print("-----------Destinatario----------------------\n")
FraseDescript = key.decrypt(msg2)
print("Mensagem descriptada: \n", FraseDescript)
verificaçao= criaHash()
