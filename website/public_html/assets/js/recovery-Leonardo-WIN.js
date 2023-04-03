let password = document.querySelector('#password')
let labelPassword = document.querySelector('#labelPassword')
let validPassword = false

let repeat = document.querySelector('#repeat')
let labelrepeat = document.querySelector('#labelrepeat')
let validrepeat = false

let empresa = document.querySelector('#empresa')


function conferirSenha() {
    const passwordValue = document.getElementById('password').value;
    const repeatValue = document.getElementById('repeat').value;
    //console.log(password);
    if (repeatValue === passwordValue) {
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
    if (password.value.length <= 7) {
        password.setAttribute('style', 'color: red')
        validPassword = false

    }
    else {
        validPassword = true
        password.setAttribute('style', 'color: #000')

    }

    console.log(password.value)
})

repeat.addEventListener('keyup', () => {
    if (repeat.value.length !== password.value.length) {
        validrepeat = false
        repeat.setAttribute('style', 'color: red')
    }
    else {
        validrepeat = true
        repeat.setAttribute('style', 'color: #000')
    }

    if (repeat.value.lenght !== 0) {
        conferirSenha(repeat);
    }


    console.log(repeat.value)

}
)


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
    validrepeat = true;

    if (validPassword && validrepeat) {
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