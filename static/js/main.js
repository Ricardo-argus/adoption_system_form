// script JAVASCRIPT

document.addEventListener("DOMContentLoaded", () => {
    console.log("Site Toca dos Peludos carregado!");

    // Exemplo: alerta ao enviar formulário
    const forms = document.querySelectorAll("form");
    forms.forEach(form => {
        form.addEventListener("submit", () => {
            alert("Informações enviadas com sucesso!");
        });
    });
});