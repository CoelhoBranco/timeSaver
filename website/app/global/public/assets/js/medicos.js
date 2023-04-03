let nome = document.querySelector('#nome')
let labelNome = document.querySelector('#labelNome')
let validNome = false

let cpf = document.querySelector('#cpf')
let labelCpf = document.querySelector('#labelCpf')
let validCpf = false

let conselho = document.querySelector('#conselho')
let validConselho = false

let uf = document.querySelector('#uf')
let validUf = false

let registro = document.querySelector('#registro')
let labelRegistro = document.querySelector('#labelRegistro')
let validRegistro = false

let cbo = document.querySelector('#cbo')
let labelCbo = document.querySelector('#labelCbo')
let validCbo = false

let operaodra = document.querySelector('#operadora')
let validOperadora = false

let codigo = document.querySelector('#codigo')
let labelCodigo = document.querySelector('#labelCodigo')
let validCodigo = false


let msgError = document.querySelector('#msgError')

nome.addEventListener('keyup', () => {
    if (nome.value.length <= 1) {
        validNome = false
    }
    else {
        validNome = true
    }
})

//valida o cpf
function validarCPF(cpf) {
    var Soma = 0
    var Resto

    var strCPF = String(cpf).replace(/[^\d]/g, '')

    if (strCPF.length !== 11)
        return false

    if ([
        '00000000000',
        '11111111111',
        '22222222222',
        '33333333333',
        '44444444444',
        '55555555555',
        '66666666666',
        '77777777777',
        '88888888888',
        '99999999999',
    ].indexOf(strCPF) !== -1)
        return false

    for (i = 1; i <= 9; i++)
        Soma = Soma + parseInt(strCPF.substring(i - 1, i)) * (11 - i);

    Resto = (Soma * 10) % 11

    if ((Resto == 10) || (Resto == 11))
        Resto = 0

    if (Resto != parseInt(strCPF.substring(9, 10)))
        return false

    Soma = 0

    for (i = 1; i <= 10; i++)
        Soma = Soma + parseInt(strCPF.substring(i - 1, i)) * (12 - i)

    Resto = (Soma * 10) % 11

    if ((Resto == 10) || (Resto == 11))
        Resto = 0

    if (Resto != parseInt(strCPF.substring(10, 11)))
        return false

    return true
}


//completa o CPF
cpf.addEventListener('keyup', () => {
    let cpflenght = cpf.value.length

    if (cpf.value.length <= 14) {
        validCpf = false
    }
    else {
        validCpf = true
    }

    if (cpflenght === 3 || cpflenght === 7) {
        cpf.value += '.'
    }
    else if (cpflenght === 11) {
        cpf.value += '-'
    }

    if (validarCpf(cpf.value)) {
        validCpf = true;
        alert
    }
}
)

conselho.addEventListener('keyup', () => {
    if (conselho.value.length <= 1) {
        validConselho = false
    }
    else {
        validConselho = true
    }
})

registro.addEventListener('keypress', () => {
    if (registro.value.length <= 1) {
        validRegistro = false
    }
    else {
        validRegistro = true
    }
})

cbo.addEventListener('keyup', () => {
    if (cbo.value.length <= 1) {
        validCbo = false
    }
    else {
        validCbo = true
    }
})

operaodra.addEventListener('keyup', () => {
    if (operaodra.value.length <= 1) {
        validOperadora = false
    }
    else {
        validOperadora = true
    }
})

codigo.addEventListener('keyup', () => {
    if (codigo.value.length <= 1) {
        validCodigo = false
    }
    else {
        validCodigo = true
    }
})


function cadastrar() {
    if (validNome && validCpf && validConselho && validUf && validRegistro && validCbo && validOperadora && validCodigo) {
        //body no fetch
        let listaUser = JSON.parse(localStorage.getItem('listaUser') || '[]')
        fetch('/controller/create/'),

            listaUser.push(
                {
                    nomeCad: nome.value,
                    cpfCad: cpf.value,
                    conselhoCad: conselho.value,
                    ufCad: uf.value,
                    registroCad: registro.value,
                    cboCad: cbo.value,
                    operadoraCad: operadora.value,
                    codigoCad: codigo.value
                }
            )


        localStorage.setItem('listaUser', JSON.stringify(listaUser))
        alert("feito")

    } else {
        button.disabled = false;
        msgError.setAttribute('style', 'display: block')
        msgError.innerHTML = '*Preencha todos os campos'
    }

}