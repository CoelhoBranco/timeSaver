<head>
    <link rel="stylesheet" href="assets/css/dados-medicos.css">
</head>

<div class="confirmar">
    <h1>Cadastrar Profissional</h1>
    <p>Confirme seus dados</p>

</div>

<div class="content">
    <div class="titulo-secao">

        <p>Dados de Identificação</p>
        <hr>

    </div>

    <div class="dados" id="">

       <p>Nome: <span id="nome"></span></p> 
       <p>CPF: <span id="cpf"></span></p>

    </div>

    <div class="titulo-secao">

        <p>Dados de Profissionais</p>
        <hr>

    </div>

    <div class="dados" id="">

        <p>Conselho: <span id="conselho"></span></p>
        <p>UF: <span id="uf"></span></p>
        <p>Registro: <span id="registro"></span></p>
        <p>CBO: <span id="cbo"></span></p>
        <p>Operadora: <span id="operadora"></span></p>
        <p>Código da Operadora: <span id="codigo"></span></p>

    </div>

    <div class="botoes">
        <div id="voltar">
            <button href="/medico" id="btn-voltar" class="btn-voltar" onclick="cadastrar()"><a>Voltar</a></button>
        </div>

        <div id="avancar">
            <button href="#" id="btn-submit" class="btn-avancar" onclick="enviar()"><a>Enviar</a></button>
        </div>
    </div>

</div>


<p class="error-validarion template"></p>

<script src="assets/js/dados-medicos.js"></script>
</body>