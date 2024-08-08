function sendMessage() {
    const textInput = document.getElementById('textInput');
    const message = textInput.value;
    if (message) {
        const chatBox = document.querySelector('.chat-box');
        const messageBox = document.createElement('div');
        messageBox.className = 'message-box';
        messageBox.textContent = message;
        chatBox.appendChild(messageBox);
        textInput.value = '';
        chatBox.scrollTop = chatBox.scrollHeight;
    }
}

function uploadFile() {
    const fileInput = document.getElementById('fileInput');
    fileInput.click();
    fileInput.onchange = () => {
        const file = fileInput.files[0];
        if (file) {
            alert('File uploaded: ' + file.name);
        }
    };
}

function uploadImage() {
    alert('Upload Image button clicked');
    // Implement image upload functionality here
}

function recordVoice() {
    alert('Record Voice button clicked');
    // Implement voice recording functionality here
}