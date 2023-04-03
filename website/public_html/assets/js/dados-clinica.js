let btnsubmit = document.querySelector('#btn-submit')

function inserirDados() {
    var nome = localStorage.getItem('listaClinica');
    nome = JSON.parse(nome);
    console.log(nome);
    nomeHTML = document.getElementById('nome'); 
    nomeHTML.value = nome;
    nomeHTML.innerHTML = 'Nome: ' + nome.nomeCad;

    var cnpj = localStorage.getItem('listaClinica');
    cnpj = JSON.parse(cnpj);
    console.log(cnpj);
    cnpjHTML = document.getElementById('cnpj'); 
    cnpjHTML.value = cnpj;
    cnpjHTML.innerHTML = 'CNPJ: ' + cnpj.cnpjCad;

    var cnes = localStorage.getItem('listaClinica');
    cnes = JSON.parse(cnes);
    console.log(cnes);
    cnesHTML = document.getElementById('cnes'); 
    cnesHTML.value = cnes;
    cnesHTML.innerHTML = 'CNES: ' + cnes.cnesCad;

    var cep = localStorage.getItem('listaClinica');
    cep = JSON.parse(cep);
    console.log(cep);
    cepHTML = document.getElementById('cep'); 
    cepHTML.value = cep;
    cepHTML.innerHTML = 'CEP: ' + cep.cepCad;

    var uf = localStorage.getItem('listaClinica');
    uf = JSON.parse(uf);
    console.log(uf);
    ufHTML = document.getElementById('uf'); 
    ufHTML.value = uf;
    ufHTML.innerHTML = 'UF: ' + uf.ufCad;

    var cidade = localStorage.getItem('listaClinica');
    cidade = JSON.parse(cidade);
    console.log(cidade);
    cidadeHTML = document.getElementById('cidade'); 
    cidadeHTML.value = cidade;
    cidadeHTML.innerHTML = 'Cidade: ' + cidade.cidadeCad;

    var bairro = localStorage.getItem('listaClinica');
    bairro = JSON.parse(bairro);
    console.log(bairro);
    bairroHTML = document.getElementById('bairro'); 
    bairroHTML.value = bairro;
    bairroHTML.innerHTML = 'Bairro: ' + bairro.bairroCad;

    var endereco = localStorage.getItem('listaClinica');
    endereco = JSON.parse(endereco);
    console.log(endereco);
    enderecoHTML = document.getElementById('endereco'); 
    enderecoHTML.value = endereco;
    enderecoHTML.innerHTML = 'Endereço: ' + endereco.enderecoCad;

    var numero = localStorage.getItem('listaClinica');
    numero = JSON.parse(numero);
    console.log(numero);
    numeroHTML = document.getElementById('numero'); 
    numeroHTML.value = numero;
    numeroHTML.innerHTML = 'Número: ' + numero.numeroCad;

    var complemento = localStorage.getItem('listaClinica');
    complemento = JSON.parse(complemento);
    console.log(complemento);
    complementoHTML = document.getElementById('complemento'); 
    complementoHTML.value = complemento;
    complementoHTML.innerHTML = 'Complemento: ' + complemento.complementoCad;

    var email = localStorage.getItem('listaClinica');
    email = JSON.parse(email);
    console.log(email);
    emailHTML = document.getElementById('email'); 
    emailHTML.value = email;
    emailHTML.innerHTML = 'E-mail: ' + email.emailCad;

    var telefone = localStorage.getItem('listaClinica');
    telefone = JSON.parse(telefone);
    console.log(telefone);
    telefoneHTML = document.getElementById('telefone'); 
    telefoneHTML.value = telefone;
    telefoneHTML.innerHTML = 'Telefone: ' + telefone.telefoneCad;

    var password = localStorage.getItem('listaClinica');
    password = JSON.parse(password);

}


document.querySelector('main').addEventListener("load", (event) => {
    inserirDados(
    )
}
);

inserirDados();

function enviar() {


        //enviar pro banco de dados aqui, se vira



    alert('salvo')
}