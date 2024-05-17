# Prática TDD
<hr>
Desafio técnico para os alunos da disciplina "Desenvolvimento Web 3"

## O que eu devo fazer?

### No ambiente Linux:

git clone https://github.com/beamclive/pratica_TDD.git <br><br>
cd Pratica_TDD_2/ <br><br>
virtualenv -p python3 venv <br><br>
source venv/bin/activate <br><br>
pip install -r requirements.txt <br><br>
cd agenda/ <br><br>
python manage.py migrate <br><br>
python manage.py test <br><br>
coverage run --source='.' manage.py test  <br><br>
coverage html <br><br>
python manage.py runserver <br><br>

### No ambiente Windows:

git clone https://github.com/beamclive/pratica_TDD.git <br><br>
cd Pratica_TDD_2/ <br><br>
virtualenv venv <br><br>
cd venv <br><br>
cd scripts <br><br>
activate.bat <br><br>
cd .. <br><br>
cd .. <br><br>
pip install -r requirements.txt <br><br>
cd agenda/ <br><br>
python manage.py migrate <br><br>
python manage.py test <br><br>
coverage run --source='.' manage.py test  <br><br>
coverage html <br><br>
python manage.py runserver <br><br>

O projeto apresenta um cadastro de agenda. Na rota raiz (/), se apresenta quatro botões onde é possível acessar a rota cadastro (/create) para cadastrar o contato, que armazena as seguintes informações: <br><br>

- Nome <br>
- Telefone <br>

Após cadastrar um contato, a rota listar (/read), lista todos os contatos cadastrados; <br><br>

Ao acessar a rota update (/update), é possível selecionar e atualizar um contato; <br><br>

Ao acessar a rota delete (/delete), é possível remover um contato; <br><br>


## Requisitos para a Sprint 2
Aqui começa o desafio. Para começar, foi preciso criar um superusuário com as seguintes credenciais: <br><br>

Username admin: <br>
E-mail address seu e-mail institucional: <br>
Password fatec: <br><br>

Ao acessar a Área do Django-Admin, foi registrado o modelo AgendaModel. <br><br>

Além do mais, foi incluído um novo campo de CPF. <br><br>

Requisitos para inclusão do campo: <br><br>

"Adicione um campo do tipo CharField com tamanho máximo de 30 caracteres. Não se esqueça de definir o valor default como ''." <br>

Validação do novo campo: <br><br>

"CPF: Espera-se exatos 11 caracteres." <br>
"Todos os campos devem ser obrigatórios." <br>

"Exibir novo campo nos templates" <br>
"Exibir o campo CPF em cadastro.html" <br>
"Exibir o campo CPF em detalhes.html" <br>
"Exibir o campo CPF em detalhes2.html" <br>

### Ajustes nos testes <br>
O código fonte passou por atualizações para acomodar estes novos requisitos. Com isso, também foi ajustado os testes existentes e criado novos testes. <br>

Recebemos a sprint 1 com uma cobertura de teste acima de 90%. E o esperado é que ao final da sprint 2 a cobertura mantenha-se neste patamar. <br><br>

No fim da prática, todos os desafios foram concluídos. 
