let password = document.querySelector('#password')
let labelPassword = document.querySelector('#labelPassword')
let validPassword = false

let passconfirmation = document.querySelector('#passconfirmation')
let labelPassconfirmation = document.querySelector('#labelPassconfirmation')
let validPassconfirmation = false

let empresa = document.querySelector('#empresa')
let logo = document.querySelector('#logo')



function conferirSenha() {
    const passwordValue = document.getElementById('password').value;
    const passconfirmationValue = document.getElementById('passconfirmation').value;
    //console.log(password);
    if (passconfirmationValue === passwordValue) {
        //console.log(password);
        password.setCustomValidity('')
        console.log('conferem')
    }
    else {
        password.setCustomValidity('Senhas não conferem')
        //password.setCustomValidity('')
        console.log('não conferem')
    }
}

password.addEventListener('keyup', () => {
    conferirSenha()
    if (password.value.length <= 5) {
        password.setAttribute('style', 'color: red')
        validPassword = false

    }
    else {
        validPassword = true
        password.setAttribute('style', 'color: #000')

    }

    console.log(password.value)
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


    console.log(passconfirmation.value)

}
)

function pegarTitulo(){
    var titulo = localStorage.getItem('listaTitulo');


    tituloHTML = document.getElementById('empresa'); 
    tituloHTML.value = titulo;
    tituloHTML.innerHTML = titulo;

    console.log(titulo);
    titulo.text = titulo;
    titulologo = titulo;
        console.log(titulologo);

    

    document.getElementById('logo').src =`/assets/img/logo-${titulologo}.png`
    //let img = document.createElement("logo"); 
    //img.src = 'assets/img/logo-' + titulo + '.png';
    //document.body.appendChild(img);

}

pegarTitulo()

function mandarPraAPI(data, url = 'controller/update/empresas') {
    let form = new FormData();
    form.append('data', data);
    //console.log(form);

    return fetch(url, { method: "POST", body: form })
        .then(response => response.json())

}

function toast(alert, icon = "info", callback) {
    if (alert) {
        alertText = alert;
    }
    const Toast = Swal.mixin({
        toast: true,
        position: 'top-end',
        showConfirmButton: false,
        timer: 2000,
        timerProgressBar: true,
        didOpen: (toast) => {
            toast.addEventListener('mouseenter', Swal.stopTimer)
            toast.addEventListener('mouseleave', Swal.resumeTimer)
        },
        didClose: () => {
            callback();
        },
    })

    Toast.fire({
        icon: icon,
        title: alertText
    })
}

async function cadastrar() {
    validPassword = true;
    validPassconfirmation = true;

    if (validPassword && validPassconfirmation) {
        let empresa = document.querySelector('#empresa');
        let user = document.querySelector('#user');
        let password = document.querySelector('#password');
        let data = JSON.stringify({
            empresa: empresa.innerHTML,
            user: user.value,
            password: password.value
        });

        //console.log(empresa.innerHTML);
        let response = await mandarPraAPI(data);

        if (response.status_code == 200) {
            toast(response.message, "success", function () { window.location.href = "/" });

        }


    } else {
        button.disabled = false;
    }

}