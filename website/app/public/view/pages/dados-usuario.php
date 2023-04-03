<head>
    <link rel="stylesheet" href="assets/css/dados-usuario.css">
</head>

<div class="confirmar">
    <h1>Cadastrar Usuário</h1>
    <p>Confirme seus dados</p>

</div>


<div class="content" >
    <div class="titulo-secao">

        <p>Dados de Identificação</p>
        <hr>

    </div>

    <div class="dados" id="">

        <span id="nome"></span>
        <span id="cpf"></span>

    </div>

    <div class="titulo-secao">

        <p>Dados de Contato</p>
        <hr>

    </div>

    <div class="dados" id="">

        <span id="email"></span>
        <span id="telefone"></span>

    </div>

</div>

<div class="botoes">
    <div id="voltar">
        <button href="/usuário" id="btn-voltar" class="btn-voltar" onclick="cadastrar()"><a>Voltar</a></button>
    </div>

    <div id="avancar">
        <button href="#" id="btn-submit" class="btn-avancar"><a>Enviar</a></button>
    </div>
</div>

</div>

<script src="assets/js/dados-usuario.js"></script>