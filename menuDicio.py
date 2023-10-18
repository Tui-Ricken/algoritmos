import biblioteca as bib
import os
x=0
while(x!=11):
    q=input("")
    os.system('cls')
    print("""1. Inserir dados
2. Listar todos dados
3. Buscar dados 
4. Listar emails
5. Listar pessoas por ano de nascimento
6. Listar pessoas com salários acima
7. Somar salários (todos)
8.Relatório da soma dos salários por ano de nascimento
9. Relatório da soma de salários por nome
10. Relatório de média de salários por idade
11. Sair""")
    x=int(input("Escolha um opção: "))
    if(x==1):
        dicio={}
        dicio["nome"]=input("Qual o nome? ")
        dicio["email"]=input("Qual o E-mail? ")
        dicio["sal"]=input("Qual o salario? ")
        dicio["nasc"]=input("Qual a data de nascimento? ")
        
        bib.inserirDadosDicio("aaa.txt",dicio)
    elif(x==2):
        x=bib.listarTodosDados("aaa.txt")
        print(x)
    elif(x==3):
        nome=input("Qual nome voce deseja procurar? ")
        x=bib.buscarDados("aaa.txt",nome)
        print(x)
    elif(x==4):
        vet=bib.listarTodosDados("aaa.txt")
        vetor=bib.listarEmail(vet)
        print(vetor)
    elif(x==5):
        ano=input("Qual o ano que vc deseja procurar? ")
        x=bib.listarPessoaporAno("aaa.txt",ano)
        print(x)
    elif(x==6):
        sal=input("Qual o salario vc quer deixar como minimo? ")
        x=bib.salariosAcima("aaa.txt",sal)
        print(x)
    elif(x==7):
        vet=bib.listarTodosDados("aaa.txt")
        x=bib.somarSalarios(vet)
        print(x)

    elif(x==8):
        ano=input("Qual ano vc quer saber o relatorio dos salarios? ")
        vet=bib.listarTodosDados("aaa.txt")
        x=bib.relatorioSalarios(vet,ano)
        print(x)
    elif(x==9):
        nome=input("Qual nome vc deseja saber? ")
        vet=bib.listarTodosDados("aaa.txt")
        x=bib.relatorioSalarioNome(vet,nome)
        print(x)

    elif(x==10):    
        idade=input("Qual a data de nascimento vc quer saber ?(digite incluindo as barras.) ")
        vet=bib.listarTodosDados("aaa.txt")
        x=bib.mediaSalarioIdade(vet,idade)
        print(x)