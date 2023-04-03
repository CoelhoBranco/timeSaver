/*let nome = document.querySelector('#nome')

let cpf = document.querySelector('#cpf')

let email = document.querySelector('#email')

let telefone = document.querySelector('#telefone')*/

let btnsubmit = document.querySelector('#btn-submit')

function inserirDados() {
    var db = localStorage.getItem('listaUser');
    /* da uma olhada aqui */
    db = JSON.parse(db);
    console.log(db);
    nomeHTML = document.getElementById('nome'); 
    nomeHTML.value = nome;
    nomeHTML.innerHTML = 'Nome: ' + db.nomeCad;

    
    console.log(cpf);
    cpfHTML = document.getElementById('cpf'); 
    cpfHTML.value = cpf;
    cpfHTML.innerHTML = 'CPF: ' + db.cpfCad;
   
    console.log(email);
    emailHTML = document.getElementById('email'); 
    emailHTML.value = email;
    emailHTML.innerHTML = 'E-mail: ' + db.emailCad;

   

    console.log(telefone);
    telefoneHTML = document.getElementById('telefone'); 
    telefoneHTML.value = telefone;
    telefoneHTML.innerHTML = 'Telefone: ' + db.telefoneCad;

}

function mandarPraAPI(data, url = 'controller/newUser') {
   
    form = new FormData();
    
    for(var i in data) {
        form.append(i, data[i]);
    
    }    
    
    return fetch(url, { method: "POST", body: form})
        .then(response => response.json())
}

function apenasNumeros(data) 
{
    var numsStr = data.replace(/[^0-9]/g,'');
    return parseInt(numsStr);
}

function mandarPraAPI(data, url = 'controller/newUser') {
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

async function enviar() {
    var db = localStorage.getItem('listaUser');
    db = JSON.parse(db);
    db.cpfCad = apenasNumeros(db.cpfCad);
    db.telefoneCad = apenasNumeros(db.telefoneCad);

    console.log(db);
    let response = await mandarPraAPI(db);

    
    if (response.status == 201) {
        Alert(response.message, "success", function () { window.location.href = "/" });

    }
    else {
        Alert(response.message, "error", function () { window.location.href = "/" });
    }
    console.log(response);
}



inserirDados();

document.querySelector("#btn-submit").addEventListener('click', enviar)
