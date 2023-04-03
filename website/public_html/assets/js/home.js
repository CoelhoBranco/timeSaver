class Home {

    mandarPraAPI(data, url = false, _method = 'POST') {
        let form = new FormData();
        form.append('data', data);
        //console.log(form);
    
        return fetch(url, { method: _method, body: form })
            .then(response => response.json())
    
    }

    async apiGET(url = false) {
        let path = `controller/read/${url}`
    
        return await fetch(path)
            .then(response => response.json())
    
    }


    async getData(){
        let result =  await this.apiGET('atividade');
        console.log(result.data);

        this.insertDataHTML(result.data);

        return result;

    }

    insertDataHTML(data){
        let HTML = document.querySelectorAll(" p.dado")
        /*user_total = 
        atendimentos = 
        ;*/
        console.log(HTML[0]);

        
        if (!data.atendimento_contador) {
            data.atendimento_contador = 0;
            console.log('aaaaaa');
        }
        if (!data.user_total) {
            data.user_total = 0;
            console.log('aaaaaa');
        }
        if (!data.atendimento) {
            data.atendimento = 0;
            console.log('aaaaaa');
        }
        HTML[0].innerHTML = data.atendimento_contador;
        HTML[1].innerHTML = data.user_total;
        HTML[2].innerHTML = data.atendimento;

    }




}

const home = new Home();
let r =  home.getData();
console.log(r);