importjs = function (l) { d = document, e = d.createElement('script'); e.setAttribute("src", l); d.head.appendChild(e); }
importjs("https://cdn.jsdelivr.net/npm/sweetalert2@11")

class Register {
    constructor() {
        this.datatitle = "Register User";
        this.dataname = "register";
        this.urlinsert = `/controller/insert/${this.dataname}`;
    }

    alert(alert, icon = "info") {
        if (alert) {
            this.alertText = alert;
        }
        Swal.fire({
            title: this.alertText,
            icon: icon,
            buttonsStyling: false,
            didClose: () => {
                callback();
            },
        })
    }

    async send() {
        let form = new FormData(document.querySelector(`form#${this.dataname}`));
        const response = await fetch(this.urlinsert, {
            method: "POST", body: form
        })
        const result = await response.json();

        if (result.success) {
            this.alert(result.status, "success", function () { window.location.href = "/" });;
        } else {
            this.alert(result.status, "error");
        }
    }
}

var cadastro = new Register;


var submit = document.querySelector("#loginbutton");



function mandarPraAPI(data, url = 'controller/newpassword') {
    //let form = document.querySelector('#form');
    //console.log(Array.isArray(data));
    /*data.forEach((element) => {
        console.log(element)
    });*/
    url = 'controller/recovery';
    form = new FormData();
    
    for(var i in data) {
        form.append(i, data[i]);
    
    }
      
    //console.log(f);
    
    return fetch(url, { method: "POST", body: form})
        .then(response => response.json())

}



submit.addEventListener('click', async (e)=>{
    e.preventDefault();

    let user = document.querySelector("#user"),
    email = document.querySelector("#email")
    ;
    let data = {
        'user':user.value,
        'email':email.value
    }
    console.log(data);
    let = response = await mandarPraAPI(data);
    console.log(response);
    if (response.code == 200){
        cadastro.alert(response.status,'success')
    }

    else if (response.code == 400){
        cadastro.alert(response.status, "error");
    }
    
    
})