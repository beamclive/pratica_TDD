# Prática TDD
Desafio técnico para os alunos da disciplina "Desenvolvimento Web 3"

## O que eu devo fazer?

### No ambiente Linux:

```bash
git clone https://github.com/beamclive/pratica_TDD.git 
cd Pratica_TDD_2/ 
virtualenv -p python3 venv 
source venv/bin/activate 
pip install -r requirements.txt 
cd agenda/ 
python manage.py migrate 
python manage.py test 
coverage run --source='.' manage.py test 
coverage html 
python manage.py runserver 
```

### No ambiente Windows:

```bash
git clone https://github.com/beamclive/pratica_TDD.git 
cd Pratica_TDD_2/ 
virtualenv venv 
cd venv 
cd scripts 
activate.bat 
cd .. 
cd .. 
pip install -r requirements.txt 
cd agenda/ 
python manage.py migrate 
python manage.py test 
coverage run --source='.' manage.py test  
coverage html 
python manage.py runserver 
```

O projeto apresenta um cadastro de agenda. Na rota raiz (/), se apresenta quatro botões onde é possível acessar a rota cadastro (/create) para cadastrar o contato, que armazena as seguintes informações: <br>

- Nome <br>
- Telefone <br>

Após cadastrar um contato, a rota listar (/read), lista todos os contatos cadastrados; <br>

Ao acessar a rota update (/update), é possível selecionar e atualizar um contato; <br>

Ao acessar a rota delete (/delete), é possível remover um contato; <br>


## Requisitos para a Sprint 2
Aqui começa o desafio. Para começar, foi preciso criar um superusuário com as seguintes credenciais: <br>

- Username admin: 'admin' <br>
- E-mail address: nosso e-mail institucional <br>
- Password fatec: 123 <br><br>

Ao acessar a Área do Django-Admin, foi registrado o modelo AgendaModel. <br>

Além do mais, foi incluído um novo campo de CPF. <br>

### Requisitos para inclusão do campo: <br>

"Adicione um campo do tipo CharField com tamanho máximo de 30 caracteres. Não se esqueça de definir o valor default como ''." <br>

Validação do novo campo: <br>

- "CPF: Espera-se exatos 11 caracteres." <br>
- "Todos os campos devem ser obrigatórios." <br>

- "Exibir novo campo nos templates" <br>
- "Exibir o campo CPF em cadastro.html" <br>
- "Exibir o campo CPF em detalhes.html" <br>
- "Exibir o campo CPF em detalhes2.html" <br>

### Ajustes nos testes <br>
O código fonte passou por atualizações para acomodar estes novos requisitos. Com isso, também foi ajustado os testes existentes e criado novos testes. <br>

Recebemos a sprint 1 com uma cobertura de teste acima de 90%. E o esperado é que ao final da sprint 2 a cobertura mantenha-se neste patamar. <br><br>

No fim da prática, todos os desafios foram concluídos. 
