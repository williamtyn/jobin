// Autoclose the message to user after 3 sec
setTimeout(function() {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 3000)

// Show/Hide candidates in order
const toggleCandidates = (e) => {
    const sibling = e.target.closest('div');
    sibling.nextElementSibling.classList.toggle('toggle');
    }

