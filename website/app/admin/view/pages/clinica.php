<head>
    <link rel="stylesheet" href="assets/css/clinica.css">
</head>

<body>

    <form>
        <h1>Cadastre-se</h1>

        <div id="msgError"></div>

        </div>
        <div class="content">
            <div class="titulo-secao">

                <p>Dados de Identificação</p>
                <hr>

            </div>
            <div class="form-group">

                <div id="fields" class="fields">
                    <label for="labelNome">Nome</label>
                    <input type="text" id="nome" class="nome" id="nome" required>
                </div>

                <div id="fields" class="fields">
                    <label for="labelCnpj">CNPJ</label>
                    <input type="text" pattern="[0-9]+$" id="cnpj" class="cnpj" id="cnpj" placeholder="00.000.000/0000-00" required maxlength="18">
                </div>

                <div id="fields" class="fields">
                    <label for="labelCnes">CNES</label>
                    <input type="text" pattern="[0-9]+$" id="cnes" class="cnes" id="cnes" placeholder="0000000" required>
                </div>

            </div>

            <div class="titulo-secao">

                <p>Dados de Endereço</p>
                <hr>

            </div>

            <div class="form-group">

                <div id="fields" class="fields">
                    <label for="labelCep">CEP</label>
                    <input type="text" pattern="[0-9]+$" id="cep" class="cep" id="cep" placeholder="00.000-000" maxlength="10" required>
                </div>

                <div id="fields" class="fields">
                    <label for="labelUf">UF</label>
                    <input type="text" id="uf" class="uf" id="uf" required>
                </div>


                <div id="fields" class="fields">
                    <label for="labelCidade">Cidade</label>
                    <input type="text" id="cidade" class="cidade" id="cidade" required>
                </div>


                <div id="fields" class="fields">
                    <label for="labelBairro">Bairro</label>
                    <input type="text" id="bairro" class="bairro" id="bairro" required>
                </div>


                <div id="fields" class="fields">
                    <label for="labelEndereco">Endereço</label>
                    <input type="text" id="endereco" class="endereco" id="endereco" required>
                </div>

                <div id="fields" class="fields">
                    <label for="labelNumero">Número</label>
                    <input type="text" id="numero" class="numero" id="numero" required>
                </div>


                <div id="fields" class="fields">
                    <label for="labelComplemento">Complemento</label>
                    <input type="text" id="complemento" class="complemento" id="complemento" required>
                </div>

            </div>

            <div class="titulo-secao">
                <p>Dados de Contato</p>
                <hr>
            </div>

            <div class="form-group">


                <div id="fields" class="fields">
                    <label for="labelEmail">E-mail</label>
                    <input type="text" id="email" class="email" id="email" placeholder="exemplo@dominio.com" required>
                </div>


                <div id="fields" class="fields">
                    <label for="labelTelefone">Telefone</label>
                    <input type="text" pattern="[0-9]+$" id="telefone" class="telefone" id="telefone" placeholder="(00) 0 0000-0000" maxlength="16" required>
                </div>

            </div>

            <div class="titulo-secao">
                <p>Senha</p>
                <hr>
            </div>

            <div class="form-group">

                <div id="fields" class="fields">
                    <label for="labelPassword">Senha</label>
                    <input type="password" id="password" class="password" id="password" minlength="8" required>
                </div>

                <div id="fields" class="fields">
                    <label for="labelPassconfirmation">Confirme sua senha</label>

                    <input type="password" id="passconfirmation" class="passconfirmation" id="passconfirmation" required>
                </div>

            </div>

            <div id="avancar">
            <button href="/dados-clinica" id="btn-submit" class="btn-avancar" onclick="cadastrar()"><a>Avançar</a></button>
        </div>
        </div>
    </form>

    <script src="./assets/js/clinica.js"></script>
</body>