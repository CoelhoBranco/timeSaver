let nome = document.querySelector('#nome')
let labelNome = document.querySelector('#labelNome')
let validnome = false

let cnpj = document.querySelector('#cnpj')
let labelCnpj = document.querySelector('#labelCnpj')
let validCnpj = false

let cnes = document.querySelector('#cnes')
let labelCnes = document.querySelector('#labelCnes')
let validCnes = false

let cep = document.querySelector('#cep')
let labelCep = document.querySelector('#labelCep')
let validCep = false

let uf = document.querySelector('#uf')
let labelUf = document.querySelector('#labelUf')
let validUf = false

let cidade = document.querySelector('#cidade')
let labelCidade = document.querySelector('#labelCidade')
let validCidade = false

let bairro = document.querySelector('#bairro')
let labelBairro = document.querySelector('#labelBairro')
let validBairro = false

let endereco = document.querySelector('#endereco')
let labelEndereco = document.querySelector('#labelEndereco')
let validEndereco = false

let complemento = document.querySelector('#complemento')
let labelComplemento = document.querySelector('#labelComplemento')

let numero = document.querySelector('#numero')
let labelNumero = document.querySelector('#labelNumero')
let validNumero = false

let email = document.querySelector('#email')
let labelEmail = document.querySelector('#labelEmail')
let validEmail = false

let telefone = document.querySelector('#telefone')
let labelTelefone = document.querySelector('#labelTelefone')
let validTelefone = false

let password = document.querySelector('#password')
let labelPassword = document.querySelector('#labelPassword')
let validPassword = false

let passconfirmation = document.querySelector('#passconfirmation')
let labelPassconfirmation = document.querySelector('#labelPassconfirmation')
let validPassconfirmation = false

let msgError = document.querySelector('#msgError')


uf.disabled = true
cidade.disabled = true
bairro.disabled = true
endereco.disabled = true

//pesquisar sobre arrar

nome.addEventListener('keyup', () => {
    if (nome.value.length <= 1) {
        validNome = false
    }
    else {
        validNome = true
    }
})


//filtra numeros no cep
function apenasNumeros(number) {
    number = number.replace(/[^0-9]/g, '');
    return parseInt(number);
}

function validarCNPJ(cnpj) {

    cnpj = apenasNumeros(cnpj);
    console.log(cnpj);

    if (cnpj == '') return false;

    if (cnpj.length != 14)
        return false;

    // Elimina CNPJs invalidos conhecidos
    if (cnpj == "00000000000000" ||
        cnpj == "11111111111111" ||
        cnpj == "22222222222222" ||
        cnpj == "33333333333333" ||
        cnpj == "44444444444444" ||
        cnpj == "55555555555555" ||
        cnpj == "66666666666666" ||
        cnpj == "77777777777777" ||
        cnpj == "88888888888888" ||
        cnpj == "99999999999999")
        return false;

    // Valida DVs
    tamanho = cnpj.length - 2
    numeros = cnpj.substring(0, tamanho);
    digitos = cnpj.substring(tamanho);
    soma = 0;
    pos = tamanho - 7;
    for (i = tamanho; i >= 1; i--) {
        soma += numeros.charAt(tamanho - i) * pos--;
        if (pos < 2)
            pos = 9;
    }
    resultado = soma % 11 < 2 ? 0 : 11 - soma % 11;
    if (resultado != digitos.charAt(0))
        return false;

    tamanho = tamanho + 1;
    numeros = cnpj.substring(0, tamanho);
    soma = 0;
    pos = tamanho - 7;
    for (i = tamanho; i >= 1; i--) {
        soma += numeros.charAt(tamanho - i) * pos--;
        if (pos < 2)
            pos = 9;
    }
    resultado = soma % 11 < 2 ? 0 : 11 - soma % 11;
    if (resultado != digitos.charAt(1))
        return false;

    return true;

}

//completa o cnpj
cnpj.addEventListener('keyup', () => {
    let cnpjlenght = cnpj.value.length


    if (cnpjlenght <= 17) {
        validCnpj = false
    }
    else {
        validCnpj = true
    }

    if (cnpjlenght === 2 || cnpjlenght === 6) {
        cnpj.value += '.'
    }
    else if (cnpjlenght === 10) {
        cnpj.value += '/'
    }

    else if (cnpjlenght === 15) {
        cnpj.value += '-'
    }

    if (cnpjlenght == 17) {

    }

    if (validarCNPJ(cnpj.value)) {
        validCnpj = true;
    }

})

//pesquisar sobre switch case
//para preenchimento automático do cep

async function pesquisarCep() {
    //const cep = document.getElementById(/[^0-9]/g, 'cep').value;
    const cepValue = document.getElementById('cep').value;
    //const cepNum = cep.replace(/./g, "").replace(/\-/g, "");

    let cep = apenasNumeros(cepValue);
    //console.log(cep);

    //if(cep.length !== 8)
    //  alert('cep invalido')
    //  return;

    //
    //async function preencherFormulário(endereco) 
    const url = 'http://viacep.com.br/ws/' + cep + '/json/';


    //async function getItem(url) 
    // let x = await fetch(file);
    //let y = await x.text();
    //myDisplay(y);
    //

    //const dados = await fetch(url);
    //const endereco = await dados.json();


    /*fetch(url).then(res => res.json().then(data => obj = data) {
        //console.log(data)

        return data;
    
;*/
    return await fetch(url).then(res => res.json())
        .then(data => obj = data).then((data) => {
            //console.log(data);
            return data;
        });

    //console.log(data);
}

function pesquisarCep1() {

    const cepValue = document.getElementById('cep').value;

    let cep = apenasNumeros(cepValue);
    console.log(cep);

    //const url = 'http://viacep.com.br/ws/' + cep + '/json/';

    const url = `http://viacep.com.br/ws/${cep}/json/ `
    //console.log(url);

    console.log(url);
    return fetch(url).then(res => res.json())
        .then(data => obj = data).then((data) => {
            //console.log(data);
            return data;
        });

    //console.log(data);
}
//let a = pesquisarCep1();

function preencherFormulario(endereco) {
    let enderecoCad = document.getElementById('endereco');
    document.getElementById('endereco').value = endereco.logradouro;
    document.getElementById('bairro').value = endereco.bairro;
    document.getElementById('cidade').value = endereco.localidade;
    document.getElementById('uf').value = endereco.uf;

    uf.disabled = false
    cidade.disabled = false
    bairro.disabled = false
    enderecoCad.disabled = false
}
//console.log(a);

cep.addEventListener('keyup', async () => {
    let ceplenght = cep.value.length
    //console.log(ceplenght);

    //switc case
    if (ceplenght === 2) {
        cep.value += '.'
    }
    else if (ceplenght === 6) {
        cep.value += '-'
    }

    if (ceplenght <= 9) {
        validCep = false
    }
    else {
        validCep = true
    }

    if (ceplenght === 10) {
        let endereco = await pesquisarCep1();
        preencherFormulario(endereco);
    }
})

//cep.addEventListener('focusout', pesquisarCep)

uf.addEventListener('keyup', () => {
    if (uf.value.length <= 1) {
        validUf = false
    }
    else {
        validUf = true
    }
})


cidade.addEventListener('keyup', () => {
    if (cidade.value.length <= 1) {
        validCidade = false
    }
    else {
        validCidade = true
    }
})

bairro.addEventListener('keyup', () => {
    if (bairro.value.length <= 1) {
        validBairro = false
    }
    else {
        validBairro = true
    }
})

endereco.addEventListener('keyup', () => {
    if (endereco.value.length <= 1) {
        validEndereco = false
    }
    else {
        validEndereco = true
    }
})

numero.addEventListener('keyup', () => {
    if (numero.value.length <= 1) {
        validNumero = false
    }
    else {
        validNumero = true
    }
})



//completa o telefone
telefone.addEventListener('keyup', () => {
    let telefonelenght = telefone.value.length

    if (telefone.value.length <= 1) {
        validTelefone = false
    }
    else {
        validTelefone = true
    }

    if (telefonelenght === 0) {
        telefone.value += "("
    }
    else if (telefonelenght === 3) {
        telefone.value += ') '
    }

    else if (telefonelenght === 6) {
        telefone.value += ' '
    }
    else if (telefonelenght === 11) {
        telefone.value += '-'
    }
}
)

function conferirSenha() {
    const passwordValue = document.getElementById('password').value;
    const passconfirmationValue = document.getElementById('passconfirmation').value;

    if (passconfirmationValue === passwordValue) {
        passconfirmation.setCustomValidity('Senhas não conferem')
        console.log('conferem')
    }
    else {
        passconfirmation.setCustomValidity('')
        console.log('não conferem')
    }
}

password.addEventListener('keyup', () => {
    if (password.value.length <= 7) {
        password.setAttribute('style', 'color: red')
        validPassword = false

    }
    else {
        validPassword = true
        password.setAttribute('style', 'color: #000')

    }

    //console.log(password.value)
})

passconfirmation.addEventListener('keyup', () => {
    if (passconfirmation.value.length !== password.value.length) {
        validPassconfirmation = false
        passconfirmation.setAttribute('style', 'color: red')
    }
    else {
        validPassconfirmation = true
        passconfirmation.setAttribute('style', 'color: #000')
    }

    if (passconfirmation.value.lenght !== 0) {
        conferirSenha(passconfirmation);
    }


    //console.log(passconfirmation.value)

}
)

function cadastrar() {
    if (validNome && validCnpj && validCnes && validCep && validUf && validCidade && validBairro && validEndereco && validNumero && validTelefone && validEmail && validPassword && validPassconfirmation) {
        //body no fetch
        let listaUser = JSON.parse(localStorage.getItem('listaUser') || '[]')
        fetch('/controller/create/'),

            listaUser.push(
                {
                    nomeCad: nome.value,
                    cnpjCad: cnpj.value,
                    cnesCad: cnes.value,
                    cepCad: cep.value,
                    ufCad: uf.value,
                    cidadeCad: cidade.value,
                    bairroCad: bairro.value,
                    enderecoCad: endereco.value,
                    numeroCad: numero.value,
                    complementoCad: complemento.value,
                    emailCad: email.value,
                    telefoneCad: telefone.value,
                    passwordCad: password.value,
                }
            )


        localStorage.setItem('listaUser', JSON.stringify(listaUser))
        //alert("feito")

    } else {
        button.disabled = false;
        msgError.setAttribute('style', 'display: block')
        msgError.innerHTML = '*Preencha todos os campos'
    }

}