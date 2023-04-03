let nome = document.querySelector('#nome')
let labelNome = document.querySelector('#labelNome')
let validNome = false

let cpf = document.querySelector('#cpf')
let labelCpf = document.querySelector('#labelCpf')

let validCpf = true

let email = document.querySelector('#email')
let labelEmail = document.querySelector('#labelEmail')
let validEmail = false

let telefone = document.querySelector('#telefone')
let labelTelefone = document.querySelector('#labelTelefone')
let validTelefone = false

let btnsubmit = document.querySelector('#btn-submit')

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

    if (cpf.value.length <= 13) {
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

    if (validarCPF(cpf.value)) {
        validCpf = true;
        alert
    }
}
)


//valida o email
function validarEmail(email) {
    var re = /\S+@\S+\.\S+/;
    return re.test(email);
}

email.addEventListener('keyup', () => {
    if (email.value.length <= 1) {
        validEmail = false
    }
    else {
        validEmail = true
    }

    if (validarEmail(email.value)) {
        validEmail = true;

    }
})

telefone.addEventListener('keyup', () => {
    if (telefone.value.length <= 1) {
        validTelefone = false
    }
    else {
        validTelefone = true
    }
})

//completa o telefone
telefone.addEventListener('keypress', () => {
    let telefonelenght = telefone.value.length

    if (telefonelenght <= 0) {
        telefone.value += '('
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

function cadastrar() {
    validNome = true;
    validCpf = true; validEmail = true;
    validTelefone = true;
    console.log(validNome && validCpf && validEmail && validTelefone);
    if (validNome && validCpf && validEmail && validTelefone) {
        //body no fetch

        /*
            localStorage.clear()
        */
        //let listaUser = localStorage.getItem('listaUser') || '[]';
        //fetch('/controller/create/'),
        //let listaUser; 
        //localStorage.clear();

        /* e aqui tambem */
        data = JSON.stringify(
            {
                'nomeCad': nome.value,
                'cpfCad': cpf.value,
                'emailCad': email.value,
                'telefoneCad': telefone.value
            }
        )
        console.log('to funcionando');


        localStorage.setItem('listaUser', data);
        //alert("feito")

    } else {
        alert('nem todos os parametros são true')
        button.disabled = false;
        msgError.setAttribute('style', 'display: block')
        msgError.innerHTML = '*Preencha todos os campos'
    }

}