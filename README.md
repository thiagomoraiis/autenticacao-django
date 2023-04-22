<h2>Auntenticação com django</h2>
<p>Autenticação simples, usando a classe abstrata "AbstractUser" para criar e autenticar usarios, adicionado campos extras, como: idade, ano de nascimento</p>
<h3>
Como rodar o projeto:
<g-emoji class="g-emoji" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f973.png">
<img class="emoji" height="20" width="20" src="https://github.githubassets.com/images/icons/emoji/unicode/1f973.png">    
</g-emoji>
</h3>

<p>No linux:</p>

<div class="snippet-clipboard-content notranslate position-relative overflow-auto">
<pre class="notranslate">
<code>
#Clone o repositorio
git clone https://github.com/thiagomoraiis/autenticacao-django.git
cd autenticacao-django
<div></div>

#Crie e ative o ambiente virtual
python3 -m venv venv
source venv/bin/activate

#Instale as dependencias necessarias
pip install -r requirements.txt

#Rode o servidor
python3 manage.py runserver
</code>
</pre>
</div>

<p>No windowns</p>

<div class="snippet-clipboard-content notranslate position-relative overflow-auto">
<pre class="notranslate">
<code>
#Clone o repositorio
git clone https://github.com/thiagomoraiis/autenticacao-django.git
cd autenticacao-django
<div></div>

#Crie e ative o ambiente virtual
python3 -m venv venv
./venv/Scripts/activate

#Instale as dependencias necessarias
pip install -r requirements.txt

#Rode o servidor
python3 manage.py runserver
</code>
</pre>
</div>
