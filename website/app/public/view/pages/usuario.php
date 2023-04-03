<head>
    <link rel="stylesheet" href="assets/css/usuario.css">
</head>

<form>
    <h1>Cadastrar Usuário</h1>

    <div id="msgError"></div>

    </div>
    <div class="content">
        <div class="titulo-secao">

            <p>Dados Pessoais</p>
            <hr>

        </div>
        <div class="form-group" id="usuario">

            <div name="fields" class="fields">
                <label id="labelNome" for="nome">Nome</label>
                <input type="text" name="nome" class="nome" id="nome" required>
            </div>

            <div id="labelCpf" name="fields" class="fields">
                <label for="cpf">CPF</label>
                <input type="text" type="text" name="cpf" class="cpf" id="cpf" placeholder="000.000.000-00" maxlength="14"
                    required>
            </div>

        </div>

        <div class="titulo-secao">

            <p>Dados de Contato</p>
            <hr>

        </div>

        <div class="form-group" id="usuario">

            <div name="fields" class="fields">
                <label id="labelEmail" for="email">E-mail</label>
                <input type="email" name="email" class="email" id="email" placeholder="exemplo@dominio.com"
                    required>
            </div>

            <div name="fields" class="fields">
                <label id="labelTelefone" for="telefone">Telefone</label>
                <input type="text" pattern="[0-9]+$" name="telefone" class="telefone" id="telefone" placeholder="(00) 0 0000-0000" maxlength="16"
                    required>
            </div>

        </div>

        <div id="avancar">
            <button id="btn-submit" class="btn-avancar" onclick="cadastrar()"><a href="/dados-usuario">Avançar</a></button>
        </div>

    </div>
</form>

<script src="assets/js/usuario.js"></script>
</body>