// Importando o Firebase
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.6.1/firebase-app.js";
import { getAuth, signInWithEmailAndPassword, createUserWithEmailAndPassword } from "https://www.gstatic.com/firebasejs/9.6.1/firebase-auth.js";

// Configuração do Firebase (substitua com suas credenciais)
const firebaseConfig = {
    apiKey: "AIzaSyBrAqUFcp0Gf-49_ciI2belK3UEQnKdvZg",
    authDomain: "Usuarios.firebaseapp.com",
    projectId: "usuarios-d5b71",
    storageBucket: "usuarios-d5b71.firebasestorage.app",
    messagingSenderId: "1028846007096",
    appId: "1:1028846007096:web:63affd10b2ae36aa3247cd",
};

// Inicializar Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

// Função de Login
function login() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const message = document.getElementById("message");

    signInWithEmailAndPassword(auth, email, password)
        .then(() => {
            window.location.href = "Forms.html"; // Redireciona para o Google Forms
        })
        .catch(error => {
            message.textContent = "Erro: " + error.message;
        });
}

// Função de Registro
function register() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const message = document.getElementById("message");

    createUserWithEmailAndPassword(auth, email, password)
        .then(() => {
            message.textContent = "Usuário registrado com sucesso!";
        })
        .catch(error => {
            message.textContent = "Erro: " + error.message;
        });
}

// Expondo as funções globalmente para que o HTML possa acessá-las
window.login = login;
window.register = register;