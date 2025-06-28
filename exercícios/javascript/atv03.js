const prompt = require('prompt-sync')();

function formulárioAluna() {
    const nome = prompt("Como você se chama? ");
    const idade = prompt("Qual a sua idade? ");
    const cidade = prompt("Qual a cidade em que você reside? ");

    return {
        nome,
        idade,
        cidade
    };
}

const dados = formulárioAluna();

console.log(`Olá! meu nome é ${dados.nome}, tenho ${dados.idade} anos e moro em ${dados.cidade}.`);
