function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Save credentials (For demonstration purposes)
    const credentials = { username, password };

    // Call function to save credentials in PDF
    saveCredentialsToPDF(credentials);
}

function saveCredentialsToPDF(credentials) {
    // Implement PDF creation logic here (using a library like jsPDF)
    // For example:
    // const pdf = new jsPDF();
    // pdf.text(`Username: ${credentials.username}\nPassword: ${credentials.password}`, 10, 10);
    // pdf.save('credentials.pdf');
}
