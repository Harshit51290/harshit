function generatePassword() {
    var length = document.getElementById("length").value;
    var characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@";
    var password = Array.from({ length: length }, () => characters[Math.floor(Math.random() * characters.length)]).join('');
    document.getElementById("result").innerText = "Generated Password: " + password;
}