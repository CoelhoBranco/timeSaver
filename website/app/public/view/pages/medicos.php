<head>
    <link rel="stylesheet" href="assets/css/medicos.css">
</head>

<body>

    <form>
        <h1>Cadastrar Profissional</h1>

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
                    <label for="labelCpf">CPF</label>
                    <input type="text" id="cpf" class="cpf" id="cpf" placeholder="000.000.000-00" required maxlength="18">
                </div>

            </div>

            <div class="titulo-secao">

                <p>Dados Profissionais</p>
                <hr>

            </div>

            <div class="form-group">

                <div id="fields" class="fields">
                    <label for="labelConselho">Conselho</label>
                    <select id="conselho" required="required">
                        <option value="">Selecione</option>
                        <option value="crm">CRM</option>
                        <option value="crp">CRP</option>
                        <option value="crefito">Crefito</option>
                    </select>
                </div>

                <div id="fields" class="fields">
                    <label for="labelUf">UF</label>
                    <select id="uf" required="required">
                        <option value="">Selecione</option>
                        <option value="rj">RJ</option>
                        <option value="sp">SP</option>
                        <option value="am">AM</option>
                    </select>
                </div>

                <div id="fields" class="fields">
                    <label for="labelRegistro">Registro</label>
                    <input type="text" id="registro" class="registro" id="registro" required>
                </div>


                <div id="fields" class="fields">
                <div class="info-texto" id="infotexto"></div>
                    <label for="labelCbo" class="cbo">CBO
                        <img src="/assets/img/circle-info-solid.png" alt="" id="info">
                        </label>
                    <input type="text" id="cbo" class="cbo" id="cbo" required>
                </div>

                <div id="fields" class="fields">
                    <label for="labelOperadora">Operadora</label>
                    <select id="operadora" required="required">
                        <option value="">Selecione</option>
                        <option value="unimed">Unimed</option>
                        <option value="stenci">Stenci</option>
                        <option value="sem">Sem operadora</option>
                    </select>
                </div>

                <div id="fields" class="fields">
                    <label for="labelCodigo">Código da Operadora</label>
                    <input type="text" id="codigo" class="codigo" id="codigo" required>
                </div>

            </div>

            <div id="avancar">
            <button id="btn-submit" class="btn-avancar" onclick="cadastrar()"><a href="/dados-medicos">Avançar</a></button>
        </div>

        </div>
    </form>

    <script src="./assets/js/medicos.js"></script>
</body>