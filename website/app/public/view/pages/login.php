<div id='form'>
    <h1>Entrar</h1>

    <p>Cadastre-se<a href="/clinica"> aqui</a></p>

    <div class="fields">
        <label for="cnpj">CNPJ ou CPF</label>
        <input type="number" id='user' name="cnpj" value="82170701052" placeholder="CNPJ ou CPF" required>
    </div>

    <div class="fields">
        <label for="password">Senha</label>
        <input type="password" id='password' name="password" placeholder="Senha" required>
    </div>

    <div id="entrar">
        <input type='submit'name="loginbutton" id="loginbutton" class="btn-login"  value="Entrar">
    </div>

    <a href="/recovery" id='esqueceu' class="esqueceu">Esqueceu sua senha?</a>


    <div class="cadastro">
    </div>
</div>

<script src="./assets/js/login.js"></script>