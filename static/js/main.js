// script JAVASCRIPT

function uploadFoto() {
    const formData = new FormData(document.getElementById("uploadForm"));
    fetch("/upload_foto", {
        method: "POST",
        body: formData
    })
    .then(response => response.text())
    .then(path => {
        // Preenche automaticamente o campo ambiente com o caminho salvo no servidor
        document.getElementById("ambiente").value = path;

        // Mostra a pré-visualização
        document.getElementById("previewImg").src = "/" + path;
        document.getElementById("previewArea").style.display = "block";
    })
    .catch(error => {
        console.error("Erro no upload:", error);
        alert("Erro ao enviar a foto.");
    });
}

function voltarCadastro() {
    // Esconde a área de pré-visualização
    document.getElementById("previewArea").style.display = "none";
}