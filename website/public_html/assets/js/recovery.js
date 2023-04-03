importjs = function (l) { d = document, e = d.createElement('script'); e.setAttribute("src", l); d.head.appendChild(e); }
importjs("https://cdn.jsdelivr.net/npm/sweetalert2@11")

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
        //console.log('conferem')
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
        password.setAttribute('style', 'color: green');
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
        repeat.setAttribute('style', 'color: green')
    }

    if (repeat.value.lenght !== 0) {
        conferirSenha(repeat);
    }


    console.log(repeat.value)

}
)


function mandarPraAPI(data, url = 'controller/newpassword') {
    //let form = document.querySelector('#form');
    //console.log(Array.isArray(data));
    /*data.forEach((element) => {
        console.log(element)
    });*/
    form = new FormData();
    
    for(var i in data) {
        form.append(i, data[i]);
      
    }
      
    //console.log(f);

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

function Alert(alert, icon = "info", callback) {
    var alertText = alert;
    if (alert) {
        var alertText = alert;
    }
    Swal.fire({
        title: alertText,
        icon: icon,
        buttonsStyling: false,
        didClose: () => {
                callback();
            
        },
    })
}

async function cadastrar() {
    validPassword = true;
    validrepeat = true;

    if (validPassword && validrepeat) {
        let code = document.querySelector('#code');
        console.log(code);
        let user = document.querySelector('#user');
        let password = document.querySelector('#password');
        let data = {
            code: code.value,
            user: user.value,
            password: password.value
        };
        console.log(data);

        //console.log(empresa.innerHTML);
        let response = await mandarPraAPI(data);
        console.log(response);
        if (response.status == 200) {
            Alert(response.message, "success", function () { window.location.href = "/" });

        }
        else {
            Alert(response.message, "error", function () { window.location.href = "/" });
        }


    } else {
        button.disabled = false;
    }

}