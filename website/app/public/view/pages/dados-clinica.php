<head>
    <link rel="stylesheet" href="assets/css/dados-clinica.css">
</head>

<div class="confirmar">
    <h1>Cadastre-se</h1>
    <p>Confirme seus dados</p>

</div>

<div id="msgError"></div>

<div class="content">
    <div class="titulo-secao">

        <p>Dados de Identificação</p>
        <hr>

    </div>

    <div class="dados" id="">

        <span id="nome"></span>
        <span id="cnpj"></span>
        <span id="cnes"></span>

    </div>

    <div class="titulo-secao">

        <p>Dados de Endereço</p>
        <hr>

    </div>

    <div class="dados" id="">

        <span id="cep"></span>
       <span id="uf"></span>
        <span id="cidade"></span>
        <span id="bairro"></span>
       <span id="endereco"></span>
        <span id="numero"></span>
        <span id="complemento"></span>

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
        <button href="/clinica" id="btn-voltar" class="btn-voltar" onclick="cadastrar()"><a>Voltar</a></button>
    </div>

    <div id="avancar">
        <button href="#" id="btn-submit" class="btn-avancar" onclick="enviar()"><a>Enviar</a></button>
    </div>

</div>

<script src="./assets/js/dados-clinica.js"></script>