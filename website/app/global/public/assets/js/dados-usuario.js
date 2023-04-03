let nome = document.querySelector('#nome')

let cpf = document.querySelector('#cpf')

let email = document.querySelector('#email')

let telefone = document.querySelector('#telefone')

function lerForm() {
    var nome_localstorage = localStorage.getItem('nomeCad')
    document.getElementById("nome").innerHTML = "Nome: " + nome_localstorage;
}

//function enviar(){
    //alert('salvo')
//}