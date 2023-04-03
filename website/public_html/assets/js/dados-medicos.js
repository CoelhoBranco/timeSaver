let btnsubmit = document.querySelector('#btn-submit')

function inserirHTML(id, ls) {

    element = document.getElementById(id);
    //nomeHTML.value = nome;
    let key = id + 'Cad';
    console.log(key);
    console.log(ls[key]);
    element.innerHTML =  ls[key];
}

function inserirDados() {

    let array_names = [ 'nome', 'cpf', 'conselho','uf','registro','cbo', 'operadora','codigo']
    var ls = JSON.parse(localStorage.getItem('listaMedico'));
    
    array_names.forEach(function (key) {
    
        inserirHTML(key, ls);
    })

}


document.querySelector('main').addEventListener("load", (event) => {
    //console.log("page is fully loaded");
    inserirDados(
        //console.log("ola mundo")
    )
}
);

inserirDados();

function enviar() {

    //enviar pro banco de dados aqui, se vira
    alert('salvo')
}