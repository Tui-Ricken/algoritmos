def inserirDadosDicio(arq,dicio):
    arquivo=open(arq,"a")     
    arquivo.write(dicio["nome"].lower() + ";")
    arquivo.write(dicio["email"].lower()+";")
    arquivo.write(dicio["sal"].lower()+";")
    arquivo.write(dicio["nasc"].lower()+"\n")
    arquivo.close()

def listarTodosDados(arq):
    arquivo=open(arq,"r")
    linha=arquivo.readlines()
    vet=[""]*len(linha)
    for i in range(0, len(linha)):
        dados=linha[i].replace("\n","")
        dados=dados.split(";")    
        vet[i]={}
        vet[i]["nome"]=dados[0]
        vet[i]["email"]=dados[1]
        vet[i]["sal"]=dados[2]
        vet[i]["nasc"]=dados[3]
    
    arquivo.close()   
    return vet

def buscarDados(arq,nome):
    w=0
    j=0
    arquivo=open(arq,"r")
    linha=arquivo.readlines()
    for i in range(0,len(linha)):
        dados=linha[i].replace("\n","")
        dados=dados.split(";")        
        if(nome in dados):
            w+=1
    vet=listarTodosDados(arq)
    vetor=[""]*w                    
    for i in range(0,len(linha)):         
        dados=linha[i].replace("\n","")
        dados=dados.split(";") 
        if(nome in dados):
            vetor[j]={}
            vetor[j]["nome"]=dados[0]
            vetor[j]["email"]=dados[1]
            vetor[j]["sal"]=dados[2]
            vetor[j]["nasc"]=dados[3]
            j+=1
        
            
    arquivo.close()
    return vetor                  
                   
def listarEmail(vet):
    vetor=[""]*len(vet)
    for i in range(0,len(vet)):
        vetor[i]=vet[i]["email"] 
    return vetor

def listarPessoaporAno(arq,data):
    arquivo=open(arq,"r")
    linha=arquivo.readlines()
    w=0
    j=0
    for i in range(0,len(linha)):
        dados=linha[i].replace("\n","")
        dados=dados.split(";")
        batata=dados[3].split("/")
        if(data in batata[2]):
            w+=1
    vetor=listarTodosDados(arq)
    vet=[""]*w
    for i in range(0,len(linha)):   
        dados=linha[i].replace("\n","")
        dados=dados.split(";")
        batata=dados[3].split("/")
        if(data in batata):    
            vet[j]={}
            vet[j]["nome"]=dados[0]
            vet[j]["email"]=dados[1]
            vet[j]["sal"]=dados[2]
            vet[j]["nasc"]=dados[3]
            j+=1 
    arquivo.close()
    return vet

def salariosAcima(arq,sal):
    arquivo=open(arq,"r")
    linha=arquivo.readlines()
    w=0
    j=0
    for i in range(0,len(linha)):
        dados=linha[i].replace("\n","")
        dados=dados.split(";")
        if(sal<float(dados[2])):
            w+=1
    vetor=listarTodosDados(arq)  
    vet=[""]*w        
    for i in range(0,len(linha)):
        dados=linha[i].replace("\n","")
        dados=dados.split(";")
        if(sal<float(dados[2])):
        
            vet[j]={}
            vet[j]["nome"]=dados[0]
            vet[j]["email"]=dados[1]
            vet[j]["sal"]=dados[2]
            vet[j]["nasc"]=dados[3]
            j+=1
    arquivo.close()
    return vet

def somarSalarios(vet):
    salarios=0
    sal=[0.0]*len(vet)
    for i in range(0,len(vet)):    
        sal[i]=(vet[i]["sal"])
        salarios=salarios+float(sal[i])
    return salarios

def relatorioSalarios(vet,ano):
    salarios=0
    sal=[0.0]*len(vet)
    for i in range(0,len(vet)):       
        if(ano in vet[i]["nasc"]):
            salarios=salarios+float(vet[i]["sal"])

    return salarios

def relatorioSalarioNome(vet,nome):
    salarios=0
    for i in range(0,len(vet)):       
        if(nome in vet[i]["nome"]):
            salarios=salarios+float(vet[i]["sal"])
    return salarios

def mediaSalarioIdade(vet,idade):
    salarios=0
    for i in range(0,len(vet)):
        if(idade in vet[i]["nasc"]):
            salarios=salarios+float(vet[i]["sal"])
    return salarios
