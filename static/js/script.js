// Autoclose the message to user after 3 sec
setTimeout(function() {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 3000);

// Show/Hide candidates in order
const toggleCandidates = (e) => {
    const sibling = e.target.closest('div');
    sibling.nextElementSibling.classList.toggle('toggle');
};

// Show footer when user are at bottom of page
const scrollFooter = document.getElementById('showfooter');
const handleScroll = () => {
    if (window.innerHeight + window.pageYOffset >= document.body.offsetHeight) {
       scrollFooter.style.display = 'block';
    } else {
        scrollFooter.style.display = 'none';
    }
};
    
window.addEventListener('scroll', handleScroll);

// Back to top with button
// Button that takes user back to top
const scrollBtn = document.getElementById('scrollbtn');

// When the user scrolls down 200px from the top of the document, show the button
window.onscroll = function() {scrollFunction();};

function scrollFunction() {
  if (document.body.scrollTop > 200 || document.documentElement.scrollTop > 200) {
    scrollBtn.style.display = 'block';
  } else {
    scrollBtn.style.display = 'none';
  }
}

// When the user clicks on the button, scroll to the top of the document
const toTheTop = () => window.scrollTo({top: 0, behavior:'smooth'});
