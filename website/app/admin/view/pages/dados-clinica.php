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

        <p>Nome: <span id="nome"></span></p>
        <p>CNPJ: <span id="cnpj"></span></p>
        <p>CNES: <span id="cnes"></span></p>

    </div>

    <div class="titulo-secao">

        <p>Dados de Endereço</p>
        <hr>

    </div>

    <div class="dados" id="">

        <p>CEP: <span id="cep"></span></p>
        <p>UF: <span id="uf"></span></p>
        <p>Cidade: <span id="cidade"></span></p>
        <p>Bairro: <span id="bairro"></span></p>
        <p>Endereço: <span id="endereco"></span></p>
        <p>Número: <span id="numero"></span></p>
        <p>Complemento: <span id="complemento"></span></p>

    </div>

    <div class="titulo-secao">

        <p>Dados de Contato</p>
        <hr>

    </div>

    <div class="dados" id="">

        <p>E-mail: <span id="email"></span></p>
        <p>Telefone: <span id="telefone"></span></p>

    </div>

</div>
<div class="botoes">

    <div id="voltar">
        <button href="/clinica" id="btn-voltar" class="btn-voltar" onclick="cadastrar()"><a>Voltar</a></button>
    </div>

    <div id="avancar">
        <button href="#" id="btn-submit" class="btn-avancar" onclick="cadastrar()"><a>Enviar</a></button>
    </div>

</div>

<script src="./assets/js/clinica.js"></script>