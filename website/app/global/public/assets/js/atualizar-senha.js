let password = document.querySelector('#password')
let labelPassword = document.querySelector('#labelPassword')
let validPassword = false

let passconfirmation = document.querySelector('#passconfirmation')
let labelPassconfirmation = document.querySelector('#labelPassconfirmation')
let validPassconfirmation = false

function conferirSenha(){
    const passwordValue = document.getElementById('password').value;
    const passconfirmationValue = document.getElementById('passconfirmation').value;

    if(passconfirmationValue === passwordValue){
        passconfirmation.setCustomValidity('Senhas não conferem')
        console.log('conferem')
    }
    else{
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

function cadastrar() {
    if (validPassword && validPassconfirmation) {
        //body no fetch
        let listaUser = JSON.parse(localStorage.getItem('listaUser') || '[]')
        
        /*

MUDAR AQUI

        */
        fetch('/controller/create/'),

            listaUser.push(
                {
                    passwordCad: password.value,
                }
            )


        localStorage.setItem('listaUser', JSON.stringify(listaUser))
        alert("feito")

    } else {
        button.disabled = false;
    }

}