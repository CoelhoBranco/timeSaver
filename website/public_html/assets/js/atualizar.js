let selecionar = document.querySelector('#selecionar')

function atualizarUnimed() {
    var titulo = document.querySelector('#tituloUnimed').innerText;
    console.log(titulo)
    titulo.text = titulo

    data = JSON.stringify(
        {
            'tituloCad': titulo,
        })

    localStorage.setItem('listaTitulo', data);
    window.location.href = '/atualizar-senha'
    //alert("feito")
    //console.log('to funcionando');



}

selecionar.addEventListener('onclick', () => {
    atualizarUnimed()
}
)


function atualizarStenci() {
    var titulo = document.querySelector('#tituloStenci').innerText;
    console.log(titulo)
    titulo.text = titulo



    localStorage.setItem('listaTitulo', titulo);
    window.location.href = '/atualizar-senha'
    //alert("feito")
    //console.log('to funcionando');

}

selecionar.addEventListener('onclick', () => {
    atualizarStenci()
}
)
