<head>
    <link rel="stylesheet" href="assets/css/atualizar-senha.css">
</head>

<div class="atualizar">
    <h1>Atualizar Dados</h1>
    <p>Escolha a plataforma</p>

</div>


<div class="content">
    <div class="plataforma">
        <span id="empresa" class="empresa"></span>
        <div class="logosenha">
            <div class="img">
                <img id="logo" src="" alt="">
            </div>
            <div class="form-group">
                <div id="fields" class="fields">
                    <label for="user">Usuário</label>
                    <input type="text" id="user" value='17434838728' class="password" id="nome" minlength="8">
                </div>
                <div id="fields" class="fields">
                    <label for="labelPassword">Senha</label>
                    <input type="password" id="password" class="password" value='leonardo' id="password" minlength="8" required>
                </div>

                <div id="fields" class="fields">
                    <label for="labelPassconfirmation">Confirme sua senha</label>

                    <input type="password" id="passconfirmation" class="passconfirmation" id="passconfirmation" value='leonardo' required>
                </div>

            </div>
            <div id="avancar">
                <button href="#" id="btn-submit" class="btn-avancar" onclick="cadastrar()"><a>Atualizar</a></button>
            </div>
        </div>
    </div>


</div>

<script src="./assets/js/atualizar-senha.js"></script>